from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from agent.tools import check_calendar, book_calendar
from langchain.tools import Tool
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0.3, model="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))

tools = [
    Tool.from_function(
        func=check_calendar,
        name="check_calendar",
        description="Check if a calendar time slot is free between start_time and end_time."
    ),
    Tool.from_function(
        func=book_calendar,
        name="book_calendar",
        description="Book a meeting in the calendar using start_time, end_time, and summary."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(message: str) -> str:
    return agent.run(message)
