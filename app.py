

# from agents import Runner, Traces, 
# import 
#   Agent,
#   Runner,
#   setTracingDisabled,
#   tool,
#   OpenAIProvider,
#   setDefaultOpenAIClient,
#   setOpenAIAPI,
#   setDefaultOpenAIKey,
# from agents;


from agents import Agent, Runner, trace
from dotenv import load_dotenv
import os
from openai import OpenAI
from agentsdk_gemini_adapter import config

load_dotenv(override=True)

# print(os.getenv("BASE_URL"))
# print(os.getenv("GOOGLE_API_KE"))
# print(os.getenv("MODEL_NAME"))

model= os.getenv("MODEL_NAME")
api_key=os.getenv("GOOGLE_API_KEY")

def agent_worker():
 model= OpenAI(base_url= os.getenv("BASE_URL"), api_key=os.getenv("GOOGLE_API_KEY"))
 res= model.chat.completions.create(
    model= os.getenv("MODEL_NAME"),
    messages=[{"role": "user", "content": "Hello!"}]
 )
 print(res.choices[0].message.content)


# def agent_worker_main():
#    agnet= new Agent(model=model, intstructions=" act like a hindi joke teller " , name="joke_teller")
#    with trace():
      
   
#     runner= await Runner.run(agnet, "tell me a joke in hindi")


# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner


# Load .env variables
# load_dotenv()

# Create an agent
agent = Agent(
    name="SalesEmailAgent",
    instructions="You are a helpful assistant that writes short, persuasive sales emails."
)

# Run the agent with Gemini
result = Runner.run_sync(
    agent,
    "Write a short cold email to a CTO about a new AI-powered CRM tool.",
    run_config=config  # config comes from the gemini adapter
)

print(result.final_output)

#some changes

if __name__ == "__main__":
    # agent_worker()
    pass