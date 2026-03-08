from typing import TypedDict, List

class BlogState(TypedDict):
    topic: str
    outline: List[str]
    research: str
    sections: List[str]
    final_blog: str