from langchain_community.tools.tavily_search import TavilySearchResults

def get_url_tavily(input: str):

    search = TavilySearchResults()
    result = search.run(f'{input}')
    return result
