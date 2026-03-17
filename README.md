# ✈️ AI Multi-Agent Travel Planner

An AI-powered travel planning system built using a **multi-agent architecture**.  
The system automatically generates a **day-wise travel itinerary** based on destination, budget, and number of days.

---

## 🚀 Features

- Multi-agent system using **CrewAI**
- Travel Research Agent
- Itinerary Writer Agent
- Budget-based travel planning
- Day-wise itinerary generation
- Streamlit interactive frontend
- MySQL database integration
- LLM powered by **Groq**

---

## 🧠 How It Works

The system uses two AI agents:

### 1️⃣ Travel Researcher Agent
- Finds attractions
- Suggests restaurants
- Recommends transport options
- Determines the best season to visit

### 2️⃣ Travel Itinerary Planner
- Creates day-wise travel plan
- Suggests budget hotels
- Calculates trip budget
- Generates travel tips

---

## 🛠 Tech Stack

- Python
- CrewAI
- LangChain
- Groq LLM
- Streamlit
- MySQL
- Tavily API

---

## 📂 Project Structure
MultiAgentHospitality
│
├── agents.py
├── ai_trip_engine.py
├── ai_trip_tasks.py
├── app.py
├── db.py
├── requirements.txt
├── README.md
└── .env