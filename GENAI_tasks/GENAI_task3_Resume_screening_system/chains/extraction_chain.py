from langchain_groq import ChatGroq
from prompts.extraction_prompt import EXTRACTION_PROMPT
from pydantic import BaseModel, Field
from typing import List

class ExtractionResult(BaseModel):
    skills: List[str] = Field(description="List of extracted skills from the resume")
    experience: str = Field(description="Summary of extracted experience from the resume")
    tools: List[str] = Field(description="List of extracted tools and software from the resume")

def get_extraction_chain(llm: ChatGroq):
    """Returns the LCEL chain for skill extraction with structured output."""
    structured_llm = llm.with_structured_output(ExtractionResult)
    return EXTRACTION_PROMPT | structured_llm