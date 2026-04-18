from langchain_core.prompts import PromptTemplate

SCORING_PROMPT = PromptTemplate.from_template(
    """You are an expert HR evaluator. Evaluate the candidate against the job description based on the extracted resume details.
    
    Extracted Resume Details Tools & Skills:
    {extracted_details}
    
    Job Description:
    {job_description}
    
    You must assign a "fit_score" from 0 to 100 based on how well the candidate's extracted details match the job description.
    You must also provide an "explanation" detailing why this score was assigned.

    Make sure your evaluation is strict, objective, and clearly reasoned.
    """
)