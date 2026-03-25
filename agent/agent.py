# LabControlPro Agent Code

class LabControlPro:
    def __init__(self, agent_name):
        self.agent_name = agent_name

    def start(self):
        print(f"{self.agent_name} is starting...")

    def stop(self):
        print(f"{self.agent_name} is stopping...")

    def status(self):
        print(f"{self.agent_name} is currently running.")

# Example instantiation
if __name__ == '__main__':
    agent = LabControlPro('Agent1')
    agent.start()
    agent.status()  
    agent.stop()