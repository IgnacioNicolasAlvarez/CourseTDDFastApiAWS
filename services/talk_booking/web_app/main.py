from fastapi import FastAPI

app = FastAPI()


@app.get("/health_check")
def healthcheck():
    return {"status": "ok"}
