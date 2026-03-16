from crewai import Crew
from agents import researcher_agent, writer_agent
from ai_trip_tasks import research_task, writer_task


def run_crew(destination, days, budget):

    research = research_task(destination, days)
    write = writer_task(destination, days, budget)

    crew = Crew(
        agents=[researcher_agent, writer_agent],
        tasks=[research, write],
        verbose=True
    )

    result = crew.kickoff()

    return str(result)