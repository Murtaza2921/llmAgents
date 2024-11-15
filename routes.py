from fastapi import APIRouter
from app.tools.weather_tool import fetch_weather
from app.tools.pdf_tool import extract_text_from_pdf
from app.tools.mongodb_tool import query_mongodb
from app.agents.qna_agent import agent

router = APIRouter()

@router.get("/weather/")
async def get_weather(city: str):
    return {"response": fetch_weather(city)}

@router.post("/pdf/")
async def query_pdf(query: str):
    return {"response": extract_text_from_pdf("sample_data/sample.pdf", query=query)}

@router.get("/database/")
async def query_database(field: str, value: str):
    filter_query = {field: value}
    return {"response": query_mongodb(filter_query)}

@router.post("/qna/")
async def ask_agent(query: str):
    return {"response": agent.run(query)}
