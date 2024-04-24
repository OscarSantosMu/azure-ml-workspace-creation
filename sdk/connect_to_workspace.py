import os

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

subscription_id = os.getenv("SUBSCRIPTION_ID")  # preferably using env variable
resource_group = os.getenv("RESOURCE_GROUP")  # preferably using env variable
workspace = os.getenv("WORKSPACE")  # preferably using env variable

if workspace is None:
    ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group)
else:
    ml_client = MLClient(
        DefaultAzureCredential(), subscription_id, resource_group, workspace
    )
