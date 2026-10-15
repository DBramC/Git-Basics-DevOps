from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"This is the root of the API"}


@app.get("/hello")
def root():
    return {"Hello"}


@app.get("/world")
def root():
    return {"World"}
