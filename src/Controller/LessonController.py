from fastapi import APIRouter

app = APIRouter()


@app.get("/")
async def lessons_by_course():
    return {"lessons": []}
