from streamlit import  as st

from google import genai
from dotenv import load_dotenv
import os,io
from gtts import gTTS

# loding the  enviroment variable
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# initializing a client
client = genai.Client(api_key=api_key)

# note generator
def note_generator(images):

    prompt = """Summarize the picture in note format at mx 100 words in languge bangla
    make sure to add necessary markdown to differentiate different section"""


    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompt]
    )

    return response.text



def generate_audio(text):
    speech = gTTS(text,lang="bn",slow=False)
    audio_buffer = io.BytesIO()
    audio_buffer.seek(0)
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def generator_quiz(images,difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate options and language bangla. Add correct answer too, after the quiz"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompt]
    )

    return response.text
