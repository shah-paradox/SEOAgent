from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

topic = input('Kindly enter a topic. Include any sub-details if reuqired\n')



client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Context: Generate a list of Reddit channels that related to the following topic:"+topic,
)


print(response.text)
