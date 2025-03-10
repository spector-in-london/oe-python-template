"""FastAPI application with REST API endpoints.

This module provides a FastAPI application with several endpoints:
- A hello-world endpoint that returns a greeting message
- An echo endpoint that echoes back the provided text

The endpoints use Pydantic models for request and response validation.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

from oe_python_template import Service

app = FastAPI(
    version="1.0.0",
    terms_of_service="https://oe-python-template.readthedocs.io/en/latest/",
    title="OE Python Template - API",
    summary="Copier template to scaffold Python projects compliant with best practices and modern tooling.",
    contact={
        "name": "Helmut Hoffer von Ankershoffen",
        "email": "helmuthva@gmail.com",
        "url": "https://github.com/helmut-hoffer-von-ankershoffen",
    },
)


class HelloWorldResponse(BaseModel):
    """Response model for hello-world endpoint."""

    message: str = Field(
        ...,
        description="The hello world message",
        examples=["Hello, world!"],
    )


class EchoResponse(BaseModel):
    """Response model for echo endpoint."""

    message: str = Field(
        ...,
        min_length=1,
        description="The message content",
        examples=["Hello, world!"],
    )


class EchoRequest(BaseModel):
    """Request model for echo endpoint."""

    text: str = Field(
        ...,
        min_length=1,
        description="The text to echo back",
        examples=["Hello, world!"],
    )


@app.get("/hello-world", tags=["Basics"])
async def hello_world() -> HelloWorldResponse:
    """
    Return a hello world message.

    Returns:
        HelloWorldResponse: A response containing the hello world message.
    """
    return HelloWorldResponse(message=Service.get_hello_world())


@app.post("/echo", tags=["Basics"])
async def echo(request: EchoRequest) -> EchoResponse:
    """
    Echo back the provided text.

    Args:
        request (EchoRequest): The request containing the text to echo back.

    Returns:
        EchoResponse: A response containing the echoed text.

    Raises:
        422 Unprocessable Entity: If text is not provided or empty.
    """
    return EchoResponse(message=request.text)
