import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.tavily_search import tavily_search
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("AIzaSyB9aUKTsR9Bamt8jBvRSzLvpB6F4JNZRRo"),
    temperature=0.3
)

def planner(state):

    topic = state["topic"]

    prompt = f"""
    Create a blog outline for the topic: {topic}
    Generate 5 sections.
    """

    result = llm.invoke(prompt)

    outline = result.content.split("\n")

    return {"outline": outline}


def researcher(state):

    topic = state["topic"]

    research = tavily_search(topic)

    return {"research": research}


def writer(state):

    outline = state["outline"]
    research = state["research"]

    sections = []

    for section in outline:

        prompt = f"""
        Write a detailed blog section titled: {section}

        Use the following research:
        {research}
        """

        result = llm.invoke(prompt)

        sections.append(result.content)

    return {"sections": sections}


def reducer(state):

    topic = state["topic"]
    sections = state["sections"]

    blog = f"# {topic}\n\n"

    for section in sections:
        blog += section + "\n\n"

    return {"final_blog": blog}