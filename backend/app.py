from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "Lux app": "Welcome to Lux app" }