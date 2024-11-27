from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml import PipelineModel
from pyspark.ml.linalg import Vectors
from django.conf import settings
import os

spark = SparkSession.builder.appName("DjangoAPI").getOrCreate()

# Usar BASE_DIR do settings.py
BASE_DIR = settings.BASE_DIR

# Construir os caminhos absolutos para os modelos
pipeline_model_path = os.path.join(BASE_DIR, 'notebook', 'pipeline')
model_path = os.path.join(BASE_DIR, 'notebook', 'spark-model')

# Verificar se os caminhos existem
if not os.path.exists(pipeline_model_path):
    raise FileNotFoundError(f"Pipeline model not found at {pipeline_model_path}")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at {model_path}")
pipeline_model = PipelineModel.load(pipeline_model_path)
model = LogisticRegressionModel.load(model_path)

def predict_credit_score(user_data):
    df = spark.createDataFrame([user_data])
    df_transformed = pipeline_model.transform(df)
    predictions = model.transform(df_transformed)
    credit_score = predictions.select('prediction').collect()[0][0]
    
    return credit_score
