from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_groq import ChatGroq


#Creating an LLM Agent
llm = ChatGroq(
    model = "groq/llama-3.1-8b-instant",
    temperature = 0.3
)

# ---------- RESEARCHER AGENT ----------
researcher_agent = Agent(
    role="Travel Researcher",
    goal="Find attractions, landmarks, restaurants and transport options.",
    backstory="Expert travel researcher with deep local insights.",
    verbose=True,
    allow_delegation=False,
    llm="groq/llama-3.1-8b-instant"   # <-- valid Groq model
)

# ---------- WRITER AGENT ----------
writer_agent = Agent(
    role="Travel Writer",
    goal="Create structured itinerary with hotels and budget breakdown.",
    backstory="Professional itinerary planner and storyteller.",
    verbose=True,
    allow_delegation=False,
    llm="groq/llama-3.1-8b-instant"   # <-- same model
)