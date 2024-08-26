import tensorflow as tf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

# Load the pre-trained model
try:
    model_predict = tf.keras.models.load_model("model_predict.h5")
except Exception as e:
    print(f"Error loading model: {e}")
    raise

# Define a FastAPI app
app = FastAPI()


# Define the request body schema
class SentenceRequest(BaseModel):
    sentence: str


# Define the response body schema
class PredictionResponse(BaseModel):
    sentence: str
    predicted_label: int
    probability: float
    disaster_status: str


# Define the predict_on_sentence function
def predict_on_sentence(sentence: str):
    # Preprocess sentence if needed
    # processed_sentence = preprocess_sentence(sentence)

    # Convert sentence to the format required by the model
    # For example, if the model requires tokenized input
    # processed_sentence = tokenizer.texts_to_sequences([sentence])
    # processed_sentence = pad_sequences(processed_sentence, maxlen=MAX_SEQUENCE_LENGTH)

    # Assuming the model expects a numpy array
    input_data = np.array([sentence])  # Adjust based on preprocessing needs
    pred_prob = model_predict.predict(input_data)
    pred_label = np.argmax(pred_prob, axis=1)[0]
    disaster_status = "real disaster" if pred_label > 0 else "not real disaster"

    return {
        "sentence": sentence,
        "predicted_label": int(pred_label),
        "probability": float(pred_prob[0][pred_label]),
        "disaster_status": disaster_status
    }


# Define the API endpoint
@app.post("/predict", response_model=PredictionResponse)
def predict(request: SentenceRequest):
    try:
        prediction = predict_on_sentence(request.sentence)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
