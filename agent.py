import os
from dotenv import load_dotenv
from groq import Groq
from hindsight_client import Hindsight

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
hindsight = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)
BANK_ID = os.getenv("HINDSIGHT_BANK_ID", "deal_intelligence_bank")

def recall_context(query: str) -> str:
    try:
        memories = hindsight.recall(bank_id=BANK_ID, query=query)
        if not memories:
            return "No prior context found."
        
        # Clean bullet formatting for UI presentation
        formatted_text = []
        for m in memories:
            text_content = getattr(m, 'text', getattr(m, 'content', str(m)))
            formatted_text.append(f"• {text_content}")
        return "\n".join(formatted_text)
    except Exception as e:
        return f"Memory recall notice: {str(e)}"

def retain_fact(text: str):
    try:
        hindsight.retain(bank_id=BANK_ID, content=text)
    except Exception as e:
        print(f"Memory retention error: {e}")

def get_completion_with_fallback(prompt: str) -> str:
    candidate_models = [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "llama3-70b-8192",
        "mixtral-8x7b-32768",
        "gemma2-9b-it"
    ]
    try:
        models_page = groq_client.models.list()
        active_ids = [m.id for m in models_page.data if hasattr(m, 'id')]
        if active_ids:
            candidate_models = active_ids + candidate_models
    except Exception:
        pass

    for model_name in candidate_models:
        try:
            response = groq_client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception:
            continue
    return "Error generating response from active model providers."

def calculate_deal_risk(context: str) -> int:
    if "pricing" in context.lower() or "salesforce" in context.lower():
        return 65
    elif "security" in context.lower() or "sla" in context.lower():
        return 45
    return 20

def run_agent(user_input: str, persona: str = "VP of Sales") -> dict:
    past_context = recall_context(user_input)
    risk_score = calculate_deal_risk(past_context)
    
    prompt = f"""You are an Enterprise B2B Sales & Deal Intelligence Agent tailoring responses for a {persona}.
Prior Deal Context & Client History:
{past_context}

Calculated Deal Risk Score: {risk_score}%
Current Prospect Input: {user_input}

Instructions:
1. Provide a high-impact, context-aware sales pitch.
2. Directly address objections from prior context.
3. Include 2 actionable next steps to derisk this deal."""

    output_text = get_completion_with_fallback(prompt)
    retain_fact(f"Client Query: {user_input} | Persona: {persona} | Risk: {risk_score}% | Strategy: {output_text[:200]}")
    
    return {
        "response": output_text,
        "recalled_context": past_context,
        "risk_score": risk_score
    }