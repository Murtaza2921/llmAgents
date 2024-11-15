from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from app.tools.weather_tool import fetch_weather
from app.tools.pdf_tool import extract_text_from_pdf
from app.tools.mongodb_tool import query_mongodb

# Define tools
weather_tool = Tool(
    name="WeatherAPI",
    func=lambda city: fetch_weather(city),
    description="Get the current weather for a given city."
)

pdf_tool = Tool(
    name="PDFReader",
    func=lambda query: extract_text_from_pdf("sample_data/sample.pdf", query=query),
    description="Extract text or answer queries from a PDF."
)

mongodb_tool = Tool(
    name="MongoDBQuery",
    func=lambda query_filter: query_mongodb(query_filter),
    description="Query data from a MongoDB database."
)

# Initialize LLM
llm = OpenAI(model="text-davinci-003")  # Replace with an open-source model if needed

# Create agent
tools = [weather_tool, pdf_tool, mongodb_tool]
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
