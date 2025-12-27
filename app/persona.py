from typing_extensions import TypedDict
from typing import Optional
from .llm import llm

class State(TypedDict):
    lead: dict
    persona: Optional[str]
    priority: Optional[str]

def persona_agent(state: State) -> State:
    lead = state["lead"]

    prompt = f"""
    You are a classification function.

    RULES:
    - Output ONLY ONE value
    - Choose EXACTLY one from:
      Founder, CTO, Marketing Manager, Sales Manager, Product Owner, Operations Manager
    - NO explanation
    - NO extra text

    Input:
    Company: {lead['company']}
    Job Title: {lead.get('job_title', '')}
    Industry: {lead['industry']}
    Company Size: {lead['company_size']}
    """

    response = llm.invoke(prompt)
    state["persona"] = response.content.strip().split("\n")[0]
    return state
