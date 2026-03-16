from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_groq import ChatGroq


# LLM
llm = ChatGroq(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3,
)

# -------- Research Agent --------
researcher_agent = Agent(
    role="Travel Researcher",
    goal="Find attractions, landmarks, restaurants and travel tips.",
    backstory="""
    You are an expert travel researcher who finds the best attractions,
    food places, and highlights of a destination.
    """,
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# -------- Writer Agent --------
writer_agent = Agent(
    role="Travel Itinerary Planner",
    goal="Create a structured day-wise itinerary with hotels and budget.",
    backstory="""
    You are a professional travel planner who designs structured
    travel itineraries with hotels, restaurants, and attractions.
    """,
    verbose=True,
    allow_delegation=False,
    llm=llm
)