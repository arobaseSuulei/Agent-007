from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

class Memory(self):
    self.global_context=""

    def __init__(self):
        self.global_context=""
    
    def set_global_context(self,context):
        self.global_context=context
    
    def get_global_context(self):
        return self.global_context

class Orchestrator:
    def __init__(self):
        self.agents=[]
    def create_agent(self,name:int,role:str,instr:str,client):
        agent=Agent(name,role,instr,client)
        self.agents.append(agent)
        return agent

class Agent:
    def __init__(self,name:int,role:str,instr:str,client):
        self.name=name
        self.role=role
        self.instr=instr
        self.client=client
    
    def think(self,message):
        response = self.client.responses.create(
            input=message,
            instructions=self.instr,
            model="openai/gpt-oss-20b",
        )
        return response.output_text


orchestrator=Orchestrator()

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

agent001=orchestrator.create_agent(
    "001",
    "chief",
    "You only read the quest memory and all context in the codebase",
    client
)

agent002=orchestrator.create_agent(
    "002",
    "parallel task",
    "You execute the tasks alone in your side",
    client
)

agent003=orchestrator.create_agent(
    "003",
    "parallel task",
    "You execute the tasks alone in your side",
    client
)

agent004=orchestrator.create_agent(
    "004",
    "parallel task",
    "You execute the tasks alone in your side",
    client
)

agent005=orchestrator.create_agent(
    "005",
    "reviewer",
    "You check what all the third parallel agent did and you review the code",
    client
)

agent006=orchestrator.create_agent(
    "006",
    "tester",
    "You test the code before submitting once its done you submit to agent 007",
    client
)

agent007=orchestrator.create_agent(
    "007",
    "submitter",
    "Your only tasks is to submit",
    client
)

print(agent001.think("Who are you ? I mean your role"))



    