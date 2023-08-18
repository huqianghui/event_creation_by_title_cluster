import openai as openaieastus01
from langchain.chat_models import AzureChatOpenAI

openaieastus01.api_type = "azure"
openaieastus01.api_key = "XXXX"
openaieastus01.api_base = "https://openaidemo-hu.openai.azure.com/"
openaieastus01.api_version = "2023-05-15"

gpt4Openaieastus01 = AzureChatOpenAI(
    openai_api_base=openaieastus01.api_base,
    openai_api_version=openaieastus01.api_version,
    deployment_name="gpt-4-32k",
    openai_api_key=openaieastus01.api_key,
    openai_api_type=openaieastus01.api_type,
    temperature=0
)
