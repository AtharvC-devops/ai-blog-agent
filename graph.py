from langgraph.graph import StateGraph
from state import BlogState
from agents import planner, researcher, writer, reducer

builder = StateGraph(BlogState)

builder.add_node("planner", planner)
builder.add_node("researcher", researcher)
builder.add_node("writer", writer)
builder.add_node("reducer", reducer)

builder.set_entry_point("planner")

builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "writer")
builder.add_edge("writer", "reducer")

graph = builder.compile()