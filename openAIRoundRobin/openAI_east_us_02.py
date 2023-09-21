import openai as openaieastus02
from langchain.chat_models import AzureChatOpenAI

openaieastus02.api_type = "azure"
openaieastus02.api_key = "XXXX"
openaieastus02.api_base = "https://azure-search-openai-demo.openai.azure.com/"
openaieastus02.api_version = "2023-05-15"

gpt4Openaieastus02 = AzureChatOpenAI(
    openai_api_base=openaieastus02.api_base,
    openai_api_version=openaieastus02.api_version,
    deployment_name="gpt-4-32k",
    openai_api_key=openaieastus02.api_key,
    openai_api_type=openaieastus02.api_type,
    temperature=0
)