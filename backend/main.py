from fastapi import FastAPI
from crop_engine.simulator import simulate_growth
from nutrition_engine.scoring import compute_nutrition
from barter_engine.trade import match_trades
from event_engine.events import generate_event

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Agri-Nutrition Sim Running"}

@app.post("/simulate-turn")
def simulate_turn(state: dict):
    crops = simulate_growth(state)
    nutrition = compute_nutrition(crops)
    event = generate_event(state)
    trades = match_trades(state)

    return {
        "crops": crops,
        "nutrition": nutrition,
        "event": event,
        "trades": trades
    }
