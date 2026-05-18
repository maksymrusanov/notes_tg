from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

general_actions = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Create new note", callback_data="New")],
        [InlineKeyboardButton(text="Check 'in progress'",
                              callback_data="In progress")],
        [InlineKeyboardButton(text="All notes", callback_data="All")],
    ]
)
note_actions = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Mark as done", callback_data="mark_done")],
        [InlineKeyboardButton(text="Set time", callback_data="set_time")],
        [InlineKeyboardButton(text="Delete", callback_data="Delete")],
        [InlineKeyboardButton(text="Back", callback_data="Back")],
    ]
)
