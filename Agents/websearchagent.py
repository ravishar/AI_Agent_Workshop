from litellm import completion
import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
from huggingface_hub import login, InferenceClient
#from asyncio import sleep
from time import sleep
import litellm
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()


class SearchAgent:
    def __init__(self, delay=0):
        ## set ENV variables
        os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
        os.environ["XAI_API_KEY"] = os.getenv("XAI_API_KEY")
        self.delay=delay
        self.model_name=["groq/llama3-8b-8192", "xai/grok-2-latest"]

        self.model = LiteLLMModel(
            self.model_name[1],
            temperature=0.2,
            api_key=os.environ["XAI_API_KEY"]
        )

        response = completion(
            model="groq/llama3-8b-8192",
            messages=[
            {"role": "user", "content": "hello from litellm"}
        ],
        )
        print(response)

    def call(self, query):

        def add_delay(*args, **kwargs):
            for i in tqdm(range(self.delay)):
                sleep(1)

        litellm._turn_on_debug()
        litellm.success_callback = [add_delay] # set custom callback function

        agent = CodeAgent(tools=[DuckDuckGoSearchTool(max_results=20)], model=self.model)


        agent.run(query)
        return agent

