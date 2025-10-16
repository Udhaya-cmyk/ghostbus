import asyncio
import json
import random
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Initial 5 Delhi buses ---
buses = [
    {"vehicle_id": 1, "route_id": "Delhi-Route-1", "lat": 28.645, "lon": 77.235, "ghost_score": 0.3, "is_ghost": False},
    {"vehicle_id": 2, "route_id": "Delhi-Route-2", "lat": 28.652, "lon": 77.242, "ghost_score": 0.7, "is_ghost": True},
    {"vehicle_id": 3, "route_id": "Delhi-Route-3", "lat": 28.660, "lon": 77.228, "ghost_score": 0.2, "is_ghost": False},
    {"vehicle_id": 4, "route_id": "Delhi-Route-4", "lat": 28.670, "lon": 77.240, "ghost_score": 0.8, "is_ghost": True},
    {"vehicle_id": 5, "route_id": "Delhi-Route-5", "lat": 28.655, "lon": 77.250, "ghost_score": 0.4, "is_ghost": False},
]

def move_buses():
    for bus in buses:
        # small random move
        bus["lat"] += (random.random() - 0.5) * 0.001
        bus["lon"] += (random.random() - 0.5) * 0.001
        # ghost score can change slowly
        bus["ghost_score"] = min(1, max(0, bus["ghost_score"] + (random.random() - 0.5) * 0.1))
        bus["is_ghost"] = bus["ghost_score"] > 0.6
    return buses

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        buses_data = move_buses()
        for bus in buses_data:
            await ws.send_text(json.dumps(bus))
        await asyncio.sleep(5)  # send updates every 5 sec
