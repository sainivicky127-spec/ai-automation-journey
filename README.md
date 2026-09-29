# AI Automation Journey

My journey learning AI automation from scratch.

## Day 1 — FastAPI Basics (29 Sep 2026)

- Set up Python environment + virtual env
- Built first FastAPI with 5 endpoints
- Server running with Uvicorn
- Tested in browser with `/docs` (Swagger UI)

### Endpoints
- `GET /` — Home message
- `GET /health` — Health check
- `GET /about` — API info
- `GET /greet/{name}` — Personalized greeting
- `GET /add/{a}/{b}` — Add two numbers

## Commands
```bash
python -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn
uvicorn hello_api:app --reload
