from dotenv import dotenv_values
config = dotenv_values(".env") 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompt_template import prompt_template

def generate_marp_deck(topic:str, additional_guidelines:str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Output Marp presentation only. No extra text. Start with front matter."),
        ("user", prompt_template)
    ])

    llm = ChatOpenAI(api_key=config["OPENAI_API_KEY"], model='gpt-4o')

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    return chain.invoke({"topic": topic, "additional_guidelines": additional_guidelines})