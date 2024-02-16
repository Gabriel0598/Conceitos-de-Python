import os
import openai
openai.api_type = "azure"
openai.api_base = "https://open-ai-gabriel-0598.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt_text1 = "Provide a summary of the text below that captures its main idea.\n\nAt Microsoft, we have been on a quest to advance AI beyond existing techniques, by taking a more holistic, human-centric approach to learning and understanding. As Chief Technology Officer of Azure AI Services, I have been working with a team of amazing scientists and engineers to turn this quest into a reality. In my role, I enjoy a unique perspective in viewing the relationship among three attributes of human cognition: monolingual text (X), audio or visual sensory signals, (Y) and multilingual (Z). At the intersection of all three, there’s magic—what we call XYZ-code as illustrated in Figure 1—a joint representation to create more powerful AI that can speak, hear, see, and understand humans better. We believe XYZ-code will enable us to fulfill our long-term vision: cross-domain transfer learning, spanning modalities and languages. The goal is to have pre-trained models that can jointly learn representations to support a broad range of downstream AI tasks, much in the way humans do today. Over the past five years, we have achieved human performance on benchmarks in conversational speech recognition, machine translation, conversational question answering, machine reading comprehension, and image captioning. These five breakthroughs provided us with strong signals toward our more ambitious aspiration to produce a leap in AI capabilities, achieving multi-sensory and multilingual learning that is closer in line with how humans learn and understand. I believe the joint XYZ-code is a foundational component of this aspiration, if grounded with external knowledge sources in the downstream AI tasks."

response = openai.Completion.create(
  engine="chatbot_yt_data",
  prompt=prompt_text1,
  temperature=0.3,
  max_tokens=250,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)