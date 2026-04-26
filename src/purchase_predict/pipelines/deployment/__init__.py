"""
This is a boilerplate pipeline 'deployment'
generated using Kedro 1.3.1
"""

from .pipeline import create_pipeline
from dotenv import load_dotenv


load_dotenv()
__all__ = ["create_pipeline"]

__version__ = "0.1"
