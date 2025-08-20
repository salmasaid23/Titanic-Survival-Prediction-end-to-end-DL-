import os
from dotenv import load_dotenv
import joblib
import tensorflow as tf


# Load .env file
load_dotenv(override=True)


# Load variables from .env file
APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")


# SRC folder path
SRC_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

# Artifacts folder path
ARTIFCATS_FOLDER_PATH = os.path.join(SRC_FOLDER_PATH, "artifacts")


# Load models
preprocessor = joblib.load(os.path.join(ARTIFCATS_FOLDER_PATH, "preprocessor.joblib"))
model = tf.keras.models.load_model(os.path.join(ARTIFCATS_FOLDER_PATH, "best_model.keras"))