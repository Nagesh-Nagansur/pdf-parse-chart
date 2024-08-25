import json
from agent_1.agent import load_schema_to_mongodb
from utils.util import insert_into_mongo, pdf_reader, insert_or_update_into_mongo


if __name__ == "__main__":
    input_pdf_path = "documents/data.pdf"
    all_pages = pdf_reader(input_pdf_path)
    
    for page in all_pages:
        json_data = load_schema_to_mongodb(page)
        dict_data = json.loads(json_data.content)
        dict_data["account_number"] = "8180933388"
        insert_or_update_into_mongo(dict_data)

