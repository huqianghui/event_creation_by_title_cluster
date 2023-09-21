import openai as openaiscus02
from langchain.chat_models import AzureChatOpenAI


openaiscus02.api_type = "azure"
openaiscus02.api_key = "XXX"
openaiscus02.api_base = "https://openai-demo-sc2.openai.azure.com/"
openaiscus02.api_version = "2023-05-15"

gpt4Openaiscus02 = AzureChatOpenAI(
    openai_api_base=openaiscus02.api_base,
    openai_api_version=openaiscus02.api_version,
    deployment_name="gpt-4-32k",
    openai_api_key=openaiscus02.api_key,
    openai_api_type=openaiscus02.api_type,
    temperature=0
)