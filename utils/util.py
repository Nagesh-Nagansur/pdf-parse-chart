import json
from pymongo import MongoClient,UpdateOne
from langchain_community.document_loaders import PDFPlumberLoader


def pdf_reader(path):

    loader = PDFPlumberLoader(path)

    data = loader.load()

    return data


def insert_into_mongo(data):

    # Connect to MongoDB
    connection_string = (
        "mongodb+srv://nageshnagansur:wwrSX9rVRz6lm3qE@database.cwlqa.mongodb.net/"
    )
    client = MongoClient(connection_string)  # Replace with your MongoDB URI
    db = client["bank_statements"]  # Replace with your database name
    collection = db["statement"]  # Replace with your collection name

    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

    print("Data imported successfully.")


def insert_or_update_into_mongo(data):
    # Connect to MongoDB
    connection_string = (
        "mongodb+srv://nageshnagansur:wwrSX9rVRz6lm3qE@database.cwlqa.mongodb.net/"
    )
    client = MongoClient(connection_string)
    db = client["bank_statements"]  # Replace with your database name
    collection = db["statement"]  # Replace with your collection name

    if isinstance(data, list):
        for record in data:
            # Unpack all transactions and push them into the transactions array
            collection.update_many(
                {"account_number": record.get("account_number")},
                {"$push": {"transactions": {"$each": record.get("transactions", [])}}},
                upsert=True
            )
    else:
        # Unpack all transactions and push them into the transactions array
        collection.update_many(
            {"account_number": data.get("account_number")},
            {"$push": {"transactions": {"$each": data.get("transactions", [])}}},
            upsert=True
        )

    print("Data upserted successfully.")



def read_from_mongo():
    connection_string = (
        "mongodb+srv://nageshnagansur:wwrSX9rVRz6lm3qE@database.cwlqa.mongodb.net/"
    )
    client = MongoClient(connection_string)  # Replace with your MongoDB URI
    db = client["bank_statements"]  # Replace with your database name
    collection = db["statement"]  # Replace with your collection name
    data = collection.find()
    return data
