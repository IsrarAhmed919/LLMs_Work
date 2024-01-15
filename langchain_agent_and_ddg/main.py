import os
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents.initialize import initialize_agent
from langchain.agents import Tool
from langchain import OpenAI
from dotenv import load_dotenv
load_dotenv()




class AGENT:
    def __init__(self):
        self.openai_api_key = os.environ["OPENAI_API_KEY"] =os.getenv('OPENAI_API_KEY')

    
    def create_tools(self):
        engine = DuckDuckGoSearchRun()
        tool = Tool(
            name = "DuckDuckGo Search",
            func=engine.run,
            description="When you need to search something from internet, this tool will be useful, try to be precise and specific with your input."
        )
        return tool
    
    def create_agent(self,  agent="zero-shot-react-description"):
        llm = OpenAI(temperature=0)
        tools = [self.create_tools()]
        agent = initialize_agent(
            agent=agent,
            tools=tools,
            llm=llm,
            # max_iterations=3
        )
        return agent
    
