from typing import Dict, List, Tuple
from langchain_core.messages import SystemMessage, HumanMessage

CHAIN_OF_THOUGHT_PROMPT = {
    "system": """You are a precise question-answering assistant. Follow these steps:
1. First, carefully read and understand the provided context
2. Identify the key information relevant to the question
3. Structure your reasoning step by step
4. Provide a concise answer based ONLY on the context
5. If information is missing, clearly state what you don't know

Remember: Never make assumptions or add information not present in the context.""",
    
    "human": """Context: {context}

Question: {query}

Let's solve this step by step:
1. What specific information from the context is relevant?
2. How does this information answer the question?
3. What is the precise answer based solely on the context?

Answer:"""
}

FEW_SHOT_PROMPT = {
    "system": """You are a precise question-answering assistant. Answer questions based ONLY on the provided context.""",
    
    "human": """Here are some examples of good responses:

Context: The Eiffel Tower was completed in 1889. It stands 324 meters tall.
Question: When was the Eiffel Tower built?
Answer: The Eiffel Tower was completed in 1889.

Context: The Eiffel Tower was completed in 1889. It stands 324 meters tall.
Question: What is its color?
Answer: I cannot answer this question as the context does not contain any information about the Eiffel Tower's color.

Now please answer the following:
Context: {context}
Question: {query}"""
}

STRUCTURED_OUTPUT_PROMPT = {
    "system": """You are a precise question-answering assistant. Answer questions based ONLY on the provided context.""",
    
    "human": """Context: {context}

Question: {query}

Please provide your answer in this format:
RELEVANT CONTEXT: [Quote the specific parts of the context that are relevant]
REASONING: [Explain your step-by-step thought process]
CONFIDENCE: [High/Medium/Low - based on how directly the context answers the question]
FINAL ANSWER: [Concise answer based only on the context]"""
}

CONSTRAINED_PROMPT = {
    "system": """You are a precise question-answering assistant. Answer questions based ONLY on the provided context.""",
    
    "human": """Important constraints:
1. Maximum answer length: 50 words
2. Use only information explicitly stated in the context
3. If multiple interpretations are possible, list them
4. For numerical answers, include units if provided
5. Express uncertainty when context is ambiguous

Context: {context}
Question: {query}"""
}

ROLE_BASED_PROMPT = {
    "system": """You are an expert research assistant with these key traits:
1. Extreme precision in citing information
2. Strong analytical skills for understanding context
3. Honest about knowledge limitations
4. Clear and concise communication
5. Methodical in analyzing questions

Answer questions based ONLY on the provided context.""",
    
    "human": """Context: {context}
Question: {query}"""
}

SELF_VERIFICATION_PROMPT = {
    "system": """You are a precise question-answering assistant. Answer questions based ONLY on the provided context.""",
    
    "human": """Context: {context}
Question: {query}

After formulating your answer, please:
1. Verify that every statement is supported by the context
2. Check if any assumptions were made
3. Confirm the answer directly addresses the question
4. Ensure no external knowledge was used
5. Validate confidence level assessment

Your response:"""
}

# Default basic prompt
BASIC_PROMPT = {
    "system": """Just answer queries based on the provided context.""",
    
    "human": """Answer the query: {query} based uniquely on the context: {context}, don't make up anything, just say what the context contains. If the information is not in the context, you must say you don't know. You must answer only the specified question and nothing else."""
}

PROMPT_TEMPLATES = {
    "basic": BASIC_PROMPT,
    "cot": CHAIN_OF_THOUGHT_PROMPT,
    "few_shot": FEW_SHOT_PROMPT,
    "structured": STRUCTURED_OUTPUT_PROMPT,
    "constrained": CONSTRAINED_PROMPT,
    "role": ROLE_BASED_PROMPT,
    "self_verify": SELF_VERIFICATION_PROMPT
}

def get_prompt_messages(prompt_type: str, context: str, query: str) -> List[SystemMessage | HumanMessage]:
    """
    Get the appropriate prompt messages based on the specified prompt type.
    
    Args:
        prompt_type: The type of prompt to use (basic, cot, few_shot, structured, constrained, role, self_verify)
        context: The context to use in the prompt
        query: The query to answer
        
    Returns:
        List of message dictionaries for the LLM
    """
    if prompt_type not in PROMPT_TEMPLATES:
        raise ValueError(f"Unknown prompt type: {prompt_type}. Available types: {list(PROMPT_TEMPLATES.keys())}")
        
    template = PROMPT_TEMPLATES[prompt_type]
    
    return [
        SystemMessage(content=template["system"]),
        HumanMessage(content=template["human"].format(context=context, query=query))
    ] 
