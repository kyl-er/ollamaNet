#Import llm-axe
from llm_axe import OnlineAgent, OllamaChat

#Select model (Ollama server must be running, and you will have needed to pull desired model)
llm = OllamaChat(model="qwen:0.5b")
online_agent = OnlineAgent(llm)

#Prompt
prompt = "You are a large language model running locally, that is currently endowed with the capability to search the web with a package called llm-axe. I would like you to tell me the current weather of Honolulu, Hawaii date: 2/19/25"
resp = online_agent.search(prompt)
print(resp)