import json

def get_json(file_path : str) -> dict:
    try:
        with open(file_path, 'r') as f: return json.load(f)
    except: return None