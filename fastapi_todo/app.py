"""
Application entry point for the FastAPI Todo application.

"""

from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_todo.schemas import Message

app = FastAPI(
    title='FastAPI Todo',
    description='A simple Todo application built with FastAPI',
    version='1.0.0',
)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """
    Root endpoint that returns a greeting message.
    """
    return {'message': 'Olá Mundo!'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    """
    Endpoint that returns a simple HTML response.
    """
    return """
    <html>
        <head>
            <title>FastAPI Todo</title>
        </head>
        <body>
            <h1>Welcome to FastAPI Todo!</h1>
            <p>Olá Mundo</p>
        </body>
    </html>
    """
