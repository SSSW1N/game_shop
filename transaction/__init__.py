from pydantic import BaseModel, Field


# class PopolnitBalanceModel(BaseModel):
#     cart_from: int = Field(gt=8600_0000_0000_0000)
#     balance: float
#     status: bool = False
#     user_id: int

class BuyGameModel(BaseModel):
    user_id: int
    balance: float
    game_id: int
    game_price: float
