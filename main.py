from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    """
    Function for a GET request to the /
    Returns:
        dict: Dictionary with message "Hello World".
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """
    Function for a POST request to /predict/
    Args:
        item (Item): Text for sentiment analysis.
    Returns:
        dict: Dictionary with predicted mood of the text.
    """
    return classifier(item.text)[0]
