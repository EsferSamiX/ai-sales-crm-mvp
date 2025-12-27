from .llm import llm

def email_writer_agent(state: dict) -> str:
    lead = state["lead"]

    prompt = f"""
    You are a professional B2B sales assistant.

    RULES:
    - Write a short cold outreach email (4–6 lines)
    - Personalize based on persona and industry
    - Do NOT use emojis
    - Do NOT use marketing buzzwords
    - Do NOT add a signature
    - Tone: friendly, professional, concise

    Context:
    Name: {lead['name']}
    Company: {lead['company']}
    Persona: {lead['persona']}
    Industry: {lead['industry']}
    """

    response = llm.invoke(prompt)
    return response.content.strip()
