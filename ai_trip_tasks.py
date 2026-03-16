from crewai import Task
from agents import researcher_agent, writer_agent


def research_task(destination, days):
    return Task(
        description=f"""
        Research travel information for {destination}.

        Find:
        - Top attractions
        - Famous landmarks
        - Budget restaurants
        - Local transport options
        - Best season or months to visit
        - Special highlights

        Provide enough attractions for at least {days} days
        so that the itinerary planner can avoid repeating places.
        """,

        expected_output="""
        List of attractions, restaurants, transport options
        and best months to visit.
        """,

        agent=researcher_agent
    )


def writer_task(destination, days, budget):
    return Task(
        description=f"""
        Create a detailed travel itinerary for {destination}.

        Number of Days: {days}
        TOTAL TRIP BUDGET: ₹{budget}

        VERY IMPORTANT RULES:

        1. The entire trip must cost LESS THAN OR EQUAL TO ₹{budget}.
        2. ₹{budget} is the TOTAL trip budget, not per category.
        3. Divide the total budget across {days} days.
        4. Allocate estimated costs for hotel, food, transport and attractions.
        5. Prefer budget hotels, street food, public transport and low-cost attractions.
        6. Each day must contain DIFFERENT attractions.
        7. Do NOT repeat locations across days.

        OUTPUT FORMAT:

        Best Time to Visit {destination}

        Generate itinerary for ALL days from Day 1 to Day {days}.

        For each day include:
        - Attractions to visit
        - Food suggestions
        - Transport suggestion
        - Estimated cost for the day

        Example format:

        Day 1
        - Activities
        - Estimated cost

        Day 2
        - Activities
        - Estimated cost

        Continue this format until Day {days}.

        FINAL BUDGET SUMMARY
        - Hotel total
        - Food total
        - Transport total
        - Attraction total
        - TOTAL TRIP COST (must be ≤ ₹{budget})

        Travel Tips

        Do NOT include Google Maps links.
        """,

        expected_output=f"A structured itinerary for {days} days where the total trip cost stays within ₹{budget}.",

        agent=writer_agent
    )