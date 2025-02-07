from aiogram.fsm.state import StatesGroup, State


class GenerateAccessState(StatesGroup):
    RealName = State()
