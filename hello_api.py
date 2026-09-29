from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/about")
def about():
    return {
        "name": "My First API",
        "version": "1.0",
        "author": "Vikram"
    }

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}