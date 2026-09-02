"""
Application entry point for the FastAPI Todo application.

"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    """
    Root endpoint that returns a greeting message.
    """
    return {'message': 'Olá Mundo!'}
