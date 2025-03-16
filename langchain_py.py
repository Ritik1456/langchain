from black.trans import StringParser
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama.llms import OllamaLLM
instruction = """Given this content {information}, please provide a summary of it by explaining
                1. what is this information about
                2. what is the key take away from it
               """

information = """ A healthy diet may contain fruits, vegetables, and whole grains, and may include little to no ultra-processed foods or sweetened beverages. The requirements for a healthy diet can be met from a variety of plant-based and animal-based foods, although additional sources of vitamin B12 are needed for those following a vegan diet.[4] Various nutrition guides are published by medical and governmental institutions to educate individuals on what they should be eating to be healthy. Advertising may drive preferences towards unhealthy foods. To reverse this trend, consumers should be informed, motivated and empowered to choose healthy diets.[5] Nutrition facts labels are also mandatory in some countries to allow consumers to choose between foods based on the components relevant to health"""


if __name__ == "__main__":
    load_dotenv()
    print("langchain")
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=information
    )
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = OllamaLLM(model="llama3.2")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)