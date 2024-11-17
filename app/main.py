from fastapi import FastAPI, Query
from app.routes import router

app = FastAPI(title="Q&A Bot")

# Include routes
app.include_router(router)

# Run this app using `uvicorn app.main:app --reload`
