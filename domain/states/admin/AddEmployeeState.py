from aiogram.fsm.state import StatesGroup, State


class AddEmployeeState(StatesGroup):
    Name = State()
    Position = State()
