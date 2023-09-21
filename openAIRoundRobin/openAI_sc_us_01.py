import openai as openaiscus01

from langchain.chat_models import AzureChatOpenAI

openaiscus01.api_type = "azure"
openaiscus01.api_key = "XXXX"
openaiscus01.api_base = "https://open-ai-demo-south-central.openai.azure.com/"
openaiscus01.api_version = "2023-05-15"


gpt4Openaiscus01 = AzureChatOpenAI(
    openai_api_base=openaiscus01.api_base,
    openai_api_version=openaiscus01.api_version,
    deployment_name="gpt-4-32k",
    openai_api_key=openaiscus01.api_key,
    openai_api_type=openaiscus01.api_type,
    temperature=0
)