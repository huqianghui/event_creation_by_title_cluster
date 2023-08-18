import openai as openaieastus03
from langchain.chat_models import AzureChatOpenAI


openaieastus03.api_type = "azure"
openaieastus03.api_key = "XXXX"
openaieastus03.api_base = "https://openai-demo3-east-us.openai.azure.com/"
openaieastus03.api_version = "2023-05-15"

gpt4Openaieastus03 = AzureChatOpenAI(
    openai_api_base=openaieastus03.api_base,
    openai_api_version=openaieastus03.api_version,
    deployment_name="gpt-4-32k",
    openai_api_key=openaieastus03.api_key,
    openai_api_type=openaieastus03.api_type,
    temperature=0
)
