import os
import agentninjas
import crewai
import langchain
import openai

# Obtenha a chave do agente a partir das variáveis de ambiente
agent_key = os.getenv('AGENT_KEY')

# Configure a chave secreta para o agentNinjas
agentninjas.Secret(agent_key)

# Inicialize e execute o monitor de agentes
agent_monitor = agentninjas.AgentMonitor()
agent_monitor.run()

# Função para parar o monitor de agentes
def stop_agent_monitor():
    agent_monitor.stop()

# Código para teste
if __name__ == "__main__":
    try:
        # Execute o monitor por um tempo determinado, por exemplo, 10 segundos
        import time
        time.sleep(10)
    finally:
        stop_agent_monitor()
