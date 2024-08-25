import json 
from langchain_groq import ChatGroq
from agent_1.prompts.prompt import system_prompt
from langchain.prompts import ChatPromptTemplate


llm = ChatGroq(model='llama3-70b-8192', temperature=0.0,api_key="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")

def load_schema_to_mongodb(page):
    """
    Returns: Json with location and assets required
    """

    prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "{system_prompt}"),
        ("human", "{user_input}")
    ]
    )

    
    prompt = prompt_template.format_messages(system_prompt=system_prompt, user_input=page)
    
    result = llm.invoke(prompt)   

    return result
