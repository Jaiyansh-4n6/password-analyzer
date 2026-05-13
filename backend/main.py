from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from analyzer import analyze, rate

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request format
class PasswordRequest(BaseModel):
    password: str


@app.post("/analyze")
def analyze_password(data: PasswordRequest):

    password = data.password

    score, feedback = analyze(password)

    return {
        "score": score,
        "feedback": feedback,
        "rating": rate(score)
    }