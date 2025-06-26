from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from agent.tools import check_calendar, book_calendar
from langchain.tools import Tool
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ FREE OpenRouter model instead of OpenAI GPT
llm = ChatOpenAI(
    temperature=0.3,
    model="mistralai/mistral-7b-instruct",  # ✅ Fast + free model
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

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
    try:
        if not message.strip():
            return "⚠️ Please enter a valid message to book a meeting."

        if " and " in message or "then" in message:
            return "⚠️ I can only book one meeting at a time. Please ask for one slot per message."

        return agent.run(message)
    except Exception as e:
        return f"❌ Something went wrong: {str(e)}"
