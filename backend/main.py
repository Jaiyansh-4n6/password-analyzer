from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from analyzer import analyze, rate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordRequest(BaseModel):
    password: str

@app.post("/analyze")
def analyze_password(data: PasswordRequest):

    password = data.password

    score, feedback, entropy = analyze(password)

    details = rate(score)

    return {
        "score": score,
        "feedback": feedback,
        "entropy": entropy,
        "strength": details["strength"],
        "risk": details["risk"],
        "crack_time": details["crack_time"],
        "crack_resistance": details["crack_resistance"]
    }