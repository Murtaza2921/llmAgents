from pymongo import MongoClient

def query_mongodb(query_filter):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test_database"]
    collection = db["users"]

    # Execute query
    results = collection.find(query_filter)
    output = [doc for doc in results]
    client.close()
    return output if output else "No matching records found."
