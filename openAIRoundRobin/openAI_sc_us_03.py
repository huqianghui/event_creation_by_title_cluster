import openai as openaiscus03
from langchain.chat_models import AzureChatOpenAI


openaiscus03.api_type = "azure"
openaiscus03.api_key = "XXX"
openaiscus03.api_base = "https://openai-demo-hu-sc-03.openai.azure.com/"
openaiscus03.api_version = "2023-05-15"

gpt4Openaiscus03 = AzureChatOpenAI(
    openai_api_base=openaiscus03.api_base,
    openai_api_version=openaiscus03.api_version,
    deployment_name="gpt-4-32k",
    openai_api_key=openaiscus03.api_key,
    openai_api_type=openaiscus03.api_type,
    temperature=0
)