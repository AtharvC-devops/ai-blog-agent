import os
from tavily import TavilyClient

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def tavily_search(topic):

    results = client.search(
        query=topic,
        search_depth="advanced",
        max_results=5
    )

    research_data = ""

    for r in results["results"]:
        research_data += r["content"] + "\n"

    return research_data