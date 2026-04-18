from langchain_groq import ChatGroq
from prompts.scoring_prompt import SCORING_PROMPT
from pydantic import BaseModel, Field

class ScoringResult(BaseModel):
    fit_score: int = Field(description="Calculated fit score out of 100")
    explanation: str = Field(description="Detailed explanation reasoning for the assigned score based on the match")

def get_scoring_chain(llm: ChatGroq):
    """Returns the LCEL chain for candidate evaluation using structured output."""
    structured_llm = llm.with_structured_output(ScoringResult)
    return SCORING_PROMPT | structured_llm