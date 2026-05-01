

---

🌾 Agri-Nutrition Sim: Adaptive Farming + Barter Economy Engine

A modular, prompt-driven simulation system that teaches food growth, nutrition balance, and cooperative survival economics through a dynamic Oregon Trail–style progression model.

This project combines:

Agricultural simulation

Nutrition tracking

Adaptive AI event generation

Multi-user barter economy

Game-like survival progression



---

🚀 Core Concept

Users (individuals or families) manage crops, nutrition, and survival decisions across evolving difficulty tiers. The system generates adaptive events and forces trade-based interdependence between players through assigned barter crops.

The goal is not just survival—but optimization of nutrition, yield efficiency, and economic cooperation.


---

🎮 Gameplay Structure

🟢 Tier 1: Homestead (Learning Phase)

Stable farming conditions

Guided crop growth cycles

Low-risk environment

Introduction to nutrition balancing


🟡 Tier 2: Frontier (Stress Phase)

Weather variability introduced

Partial crop failure possible

Forced trading begins

Resource optimization required


🔴 Tier 3: Collapse Economy (Survival Phase)

Scarcity-driven system

Extreme environmental volatility

Mandatory barter dependency

Specialized survival strategies required



---

🌱 Core Systems

🌾 Crop Simulation Engine

Time-based or turn-based crop growth

Environmental modifiers (season, soil, water)

Yield prediction + failure states


🧠 Nutrition Engine

Maps crops → macronutrients & micronutrients

Tracks dietary diversity

Generates nutrition stability score


🔁 Barter Economy Engine

Dynamic trade valuation system

User surplus/deficit matching

Forced interdependency via assigned crops


🎲 Event / Curveball Engine

AI-generated disruptions such as:

Droughts

Pest outbreaks

Market crashes

Nutritional deficiencies

Trade opportunities


🤖 Prompt Orchestration Layer

All simulation logic is driven through structured prompts:

Event generation

Difficulty scaling

Adaptive balancing

Narrative consistency



---

🔄 Barter System Rules

Each family unit is assigned:

1 Export Crop → must be traded outward

1 Import Crop → must be acquired via trade


Assignment Logic:

Export crop = highest surplus efficiency crop

Import crop = nutritional deficiency or scarcity need


This ensures:

Cross-user dependency

Functional trade economy

Strategic specialization



---

📊 Core Data Models

Crop

{
  "name": "corn",
  "growth_time": 6,
  "calories": 120,
  "nutrients": {
    "carbs": 0.8,
    "protein": 0.1,
    "fiber": 0.3
  },
  "trade_value": 1.0,
  "risk": "medium"
}


---

User / Family State

{
  "id": "family_001",
  "inventory": ["corn", "beans"],
  "nutrition_score": 72,
  "export_crop": "wheat",
  "import_crop": "lentils",
  "risk_level": 0.4
}


---

Event

{
  "type": "drought",
  "impact": {
    "corn_yield": -0.35
  },
  "choices": [
    "ration water",
    "trade for drought-resistant seeds",
    "risk irrigation collapse"
  ]
}


---

🧠 AI Prompt System

The system uses structured prompts to generate gameplay state transitions:

Example Prompt

Generate a farming survival event based on:
- current season
- user crop inventory
- nutrition score
- difficulty tier

The event must:
- affect crop yield
- introduce a decision
- influence barter economy


---

🌐 Tech Stack

Frontend

React / Svelte

Real-time dashboard UI

Crop grid visualization

Nutrition tracking panel

Trade marketplace


Backend

FastAPI / Node.js

Modular service architecture:

crop-engine

nutrition-engine

barter-engine

event-engine

prompt-engine



Database

PostgreSQL

Event + state history tracking

Trade logs

User progression tracking



---

📁 Repository Structure

/agri-nutrition-sim
  /frontend
  /backend
    /crop_engine
    /nutrition_engine
    /barter_engine
    /event_engine
    /prompt_engine
  /database
  /docs
  docker-compose.yml
  README.md


---

🧪 Key Features

Adaptive survival simulation

Nutrition-aware gameplay mechanics

AI-generated environmental events

Forced cooperative barter system

Dynamic crop value economy

Multi-tier difficulty scaling



---

🔮 Future Extensions

Regional climate simulation maps

Multiplayer trade networks

AI-controlled NPC farming villages

Real-world agricultural data integration

Seasonal global economic shocks

Educational mode for nutrition learning



---

🧭 Philosophy

This system is designed as:

a simulation of survival economics

a nutrition literacy engine

a cooperative dependency model

a testbed for adaptive AI game systems


It explores how resource scarcity, food systems, and trade networks shape decision-making under pressure.


---

📜 License

MIT License (or customize depending on your intent)


---
