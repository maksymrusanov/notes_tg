from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import db.database as db
from bot.keyboards import general_actions as ga
from bot.keyboards import note_actions as na
from bot.states import Notes

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("What you want to do?", reply_markup=ga)
    await db.create_table()


@router.callback_query(F.data == "New")
async def add_note(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Notes.name)
    await callback_query.message.answer(text="Write your note name")


@router.message(Notes.name)
async def save_name(message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Notes.description)
    await message.answer("write your note description")


@router.message(Notes.description)
async def save_note(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.update_data(user_id=message.from_user.id)
    data = await state.get_data()
    await db.add_note(
        user_id=data["user_id"], name=data["name"], description=data["description"]
    )
    await message.answer(
        "Your note was added\nWhat else you want to do? ", reply_markup=ga
    )


@router.callback_query(F.data == "All")
async def get_all(callback: CallbackQuery):
    all_notes = await db.get_all_notes()
    if not all_notes:
        await callback.message.answer(
            text="No notes found.\nWhat else you want to do?", reply_markup=ga
        )
    else:
        for i in all_notes:
            await callback.message.answer(
                text=f"ID:{i[0]} \nName:{i[1]}\nDescription: {i[2]}\nStatus: {i[3]}",
                reply_markup=na,
            )


@router.callback_query(F.data == "In progress")
async def get_in_progress(callback: CallbackQuery):
    notes = await db.get_notes(status="In progress")
    if not notes:
        await callback.message.answer(
            text="No 'in progress' notes found.\nwhat you want to do?", reply_markup=ga
        )
    else:
        for note in notes:
            await callback.message.answer(
                text=f"ID:{note[0]}\nName:{note[1]}\nDescription: {note[2]}\nStatus: {note[3]}",
                reply_markup=na,
            )
    await callback.answer(text="what you want to do?", reply_markup=ga)


@router.callback_query(F.data == "mark_done")
async def mark_as_done(callback: CallbackQuery):
    note_id = int(callback.message.text.split()[0][3:])
    await db.change_note_status(note_id=note_id, new_status="Done")
    await callback.message.answer("Note marked as done", reply_markup=ga)


@router.callback_query(F.data == "Back")
async def back(callback: CallbackQuery):
    await callback.message.answer(text="what you want to do?", reply_markup=ga)


@router.callback_query(F.data == "Delete")
async def delete_note(callback: CallbackQuery):
    note_id = int(callback.message.text.split()[0][3:])
    await db.delete_note(note_id=note_id)
    await callback.message.answer("Note deleted", reply_markup=ga)
