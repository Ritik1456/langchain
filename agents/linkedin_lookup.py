import os
from dotenv import load_dotenv
# from langchain_ollama.llms import OllamaLLM
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import get_url_tavily
load_dotenv()

def lookup(input):

    llm = ChatOpenAI(model="gpt-4o-mini",
    temperature=0)

    prompt = """Given the name of the person, {linkedin_name}, i want you to give me the linkedin URL of the person.
    Your answer should contain only the url"""

    prompt_template = PromptTemplate(template = prompt, input_variables=['linkedin_name'])

    tools_for_agent = [Tool(
        name= 'linkedin url finder',
        func= get_url_tavily,
    description = 'useful when need to find linkedin page URL'
    )]

    react_prompt = hub.pull('hwchase17/react')

    agent = create_react_agent(tools = tools_for_agent, prompt = react_prompt, llm = llm)
    executer = AgentExecutor(agent = agent, tools = tools_for_agent, verbose=True)

    result = executer.invoke(input = {'input': prompt_template.format_prompt(linkedin_name = input)})

    url = result['output']

    return url

if __name__ == '__main__':
    url = lookup('Ritik Shrivastava Brainchip')
    print(url)
