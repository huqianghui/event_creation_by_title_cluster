from openAIRoundRobin.openAI_east_us_01 import gpt4Openaieastus01
from openAIRoundRobin.openAI_east_us_02 import gpt4Openaieastus02
from openAIRoundRobin.openAI_east_us_03 import gpt4Openaieastus03


from openAIRoundRobin.openAI_sc_us_01 import gpt4Openaiscus01
from openAIRoundRobin.openAI_sc_us_02 import gpt4Openaiscus02
from openAIRoundRobin.openAI_sc_us_03  import gpt4Openaiscus03



openai=[gpt4Openaieastus01,gpt4Openaieastus02,gpt4Openaieastus03,gpt4Openaiscus01,gpt4Openaiscus02,gpt4Openaiscus03]

from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=('''You are a financial journalist who, based on the financial news headlines provided by the user, Summarize into a simple, clear, easily understandable sentence that grabs attention in fewer than 15 words. 
            if the language of headlines is Chinses,please answer in Chinese. ''')
        ),
        HumanMessagePromptTemplate.from_template("The corresponding financial news headlines are as follows: {event_Source}"),
    ]
)

openAICallCount = 0

def eventCreateByTitle(event_Source:str):
    global openAICallCount
    global openai

    index = openAICallCount % 6
    currentOpenAI=openai[index]
    print("openai index:",index)
    

    try:
        response = currentOpenAI(template.format_messages(event_Source=event_Source))
        result = response.content
        print(result)
        openAICallCount = openAICallCount + 1
        return result
    except Exception as e :
        print("Call error:", e)
        index = (openAICallCount+1) % 6
        currentOpenAI=openai[index]
        print("after exception openai index:",index)
        response = currentOpenAI(template.format_messages(event_Source=event_Source))
        result = response.content
        openAICallCount = openAICallCount + 2
        print(result)
        return result
