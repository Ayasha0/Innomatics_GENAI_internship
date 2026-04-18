from langchain_core.prompts import PromptTemplate

EXTRACTION_PROMPT = PromptTemplate.from_template(
    """You are an expert HR AI Assistant. Extract the candidate's skills, experience, and tools from the provided resume text.
    
    IMPORTANT RULES:
    - Do NOT hallucinate.
    - Do NOT assume skills not explicitly present in the resume.
    
    Resume Text:
    {resume_text}
    """
)