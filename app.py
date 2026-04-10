from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI on Render!"}

@app.get("/health")
def health():
    return {"status": "ok"}
