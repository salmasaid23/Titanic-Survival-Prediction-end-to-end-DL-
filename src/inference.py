import pandas as pd
from typing import List
from src.models.schemas import PssengerData, PassengerPrediction, PredictionResponse 
from src.config import model, preprocessor


def predict_surival(passengers: List[PssengerData]) -> PredictionResponse:
    """_summary_

    Args:
        passengers (List[PssengerData]): _description_

    Returns:
        PredictionResponse: _description_
    """

    # base data list of dicts
    base_data = [p.model_dump() for p in passengers]
    
    for i, p in enumerate(passengers):
        base_data[i]["family_size"] = p.family_size
        base_data[i]["is_alone"] = p.is_alone
    
    # To DF
    df = pd.DataFrame(base_data)
    
    # Transform data
    df_processed = preprocessor.transform(df)
    
    # Predict
    predictions = (model.predict(df_processed) > 0.5).astype("int32")

    # Pydantic response
    pred_response = PredictionResponse(predictions=[
        PassengerPrediction(
        passenger_id=passenger.passenger_id,
        prediction="survived" if prediction == 1 else "not survived"
    )
    for passenger, prediction in zip(passengers, predictions.flatten())
    ])
    
    return pred_response
  
    