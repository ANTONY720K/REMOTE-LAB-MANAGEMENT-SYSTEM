import requests
import json


def deploy_agents(agent_list):
    for agent in agent_list:
        response = requests.post(f"https://api.example.com/deploy", json=agent)
        if response.status_code == 200:
            print(f"Successfully deployed agent: {agent['name']}")
        else:
            print(f"Failed to deploy agent: {agent['name']}, Status Code: {response.status_code}")


if __name__ == '__main__':
    agents = [
        {'name': 'agent1', 'ip': '192.168.1.10'},
        {'name': 'agent2', 'ip': '192.168.1.11'},
        {'name': 'agent3', 'ip': '192.168.1.12'},
    ]
    deploy_agents(agents)