import speech_recognition as sr
from fastapi import APIRouter, HTTPException, UploadFile, File

api = APIRouter(prefix='/files')


@api.post('/audio')
async def create_file(file: UploadFile = File(...)):
    try:
        recognizer = sr.Recognizer()
        # Read the file asynchronously
        file_bytes = await file.read()
        from io import BytesIO
        with BytesIO(file_bytes) as source:
            with sr.AudioFile(source) as audio_source:
                audio_data = recognizer.record(audio_source)
                text = recognizer.recognize_google(audio_data, language='pt-BR')
                return text
    except sr.UnknownValueError as e:
        raise HTTPException(400, e)
