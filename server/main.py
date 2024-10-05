from typing import Union
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    df = pd.read_csv('market.csv')    
    json_result = df.to_json(orient='records', lines=True)
    
    return {"status":500}



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}