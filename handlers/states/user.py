from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    waiting_name = State()

class AddPlanState(StatesGroup):
    waiting_title = State()
    waiting_date = State()
    waiting_time = State()
