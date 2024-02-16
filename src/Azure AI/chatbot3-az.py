#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://open-ai-gabriel-0598.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt='An abstract painting of the seattle skyline featuring the space needle and mount rainier',
    size='1024x1024',
    n=1
)

image_url = response["data"][0]["url"]