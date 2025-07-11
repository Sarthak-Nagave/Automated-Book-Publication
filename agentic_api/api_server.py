from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class ChapterRequest(BaseModel):
    content: str

@app.post("/spin")
def spin_chapter_api(req: ChapterRequest):
    return {"spun_content": f"[SPUN VERSION] {req.content[:100]}..."}

@app.post("/review")
def review_chapter_api(req: ChapterRequest):
    return {"reviewed_content": f"[REVIEWED VERSION] {req.content[:100]}..."}