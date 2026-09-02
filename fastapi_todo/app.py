"""
Application entry point for the FastAPI Todo application.

"""

from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI(
    title='FastAPI Todo',
    description='A simple Todo application built with FastAPI',
    version='1.0.0',
)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    """
    Root endpoint that returns a greeting message.
    """
    return {'message': 'Olá Mundo!'}
