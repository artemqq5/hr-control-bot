from aiogram.fsm.state import StatesGroup, State


class CreateInformState(StatesGroup):
    Employee = State()
    Describe = State()

