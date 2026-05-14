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
async def add_note(message: Message, state: FSMContext):
    await state.set_state(Notes.name)
    await message.answer(text="Write your note name")


@router.message(Notes.name)
async def save_name(message: Message, state: FSMContext):
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
    await message.answer("Your note was added")


@router.callback_query(F.data == "In progress")
async def get_in_progress(callback: CallbackQuery):
    notes = await db.get_notes(status="In progress")
    if not notes:
        await callback.message.answer("No 'in progress' notes found.")
    else:
        for note in notes:
            await callback.message.answer(
                text=f"Name: {note[0]}, Description: {note[1]}", reply_markup=na
            )
