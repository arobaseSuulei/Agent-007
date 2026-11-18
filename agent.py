class Orchestrator:
    def __init__(self):
        self.agents=[]
    def create_agent(self,name:int,role:str,instr:str):
        agent=Agent(name,role,instr)
        self.agents.append(agent)
        return agent

class Agent:
    def __init__(self,name:int,role:str,instr:str):
        self.name=name
        self.role=role
        self.instr=instr


orchestrator=Orchestrator()

agent0=orchestrator.create_agent(
    "001",
    "chief",
    "read only the files"
)

print(agent0.role)

    