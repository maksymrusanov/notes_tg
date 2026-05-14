from aiogram.fsm.state import State, StatesGroup


class Notes(StatesGroup):
    name = State()
    user_id = State()
    description = State()
    user_id = State()
