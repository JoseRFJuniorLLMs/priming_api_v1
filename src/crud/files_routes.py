import io

from pydub import AudioSegment
from google.oauth2 import service_account
from google.cloud import speech
from fastapi import APIRouter, HTTPException, UploadFile, File
from src.config.crendential import CREDENTIAL

api = APIRouter(prefix='/files')


credentials = service_account.Credentials.from_service_account_info(CREDENTIAL)
client = speech.SpeechClient(credentials=credentials)


@api.post('/audio')
async def read_audio(file: UploadFile = File(...)):
    try:
        content = await file.read()

        audio = AudioSegment.from_file(io.BytesIO(content))
        audio = audio.set_channels(1)

        with io.BytesIO() as output:
            audio.export(output, format="wav")
            content_mono = output.getvalue()

        audio_mono = speech.RecognitionAudio(content=content_mono)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="en-US",
        )

        response = client.recognize(config=config, audio=audio_mono)
        return response.results[0].alternatives[0].transcript

    except Exception as e:
        raise HTTPException(status_code=400, detail='Error reading audio file')
