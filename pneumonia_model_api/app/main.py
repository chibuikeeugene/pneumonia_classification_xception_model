import sys, os
# append current directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import FastAPI, APIRouter, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from app.controller import api_router

from app import __version__ as api_version

import loguru as logger 

# Global variables
title: str = "Pneumonia model api"
desc: str = "Pneumonia model Inference endpoint"

app = FastAPI(
    title=title,
    description= desc,
    version= api_version,
)

root_router =  APIRouter()

@root_router.get('/', status_code= 200)
async def index(request: Request):
    """Basic HTML response."""
    body = (
            "<html>"
            "<body style='padding: 10px;'>"
            "<h1>Welcome to the API</h1>"
            "<div>"
            "Check the docs: <a href='/docs'>here</a>"
            "</div>"
            "</body>"
            "</html>"
        )

    return HTMLResponse(content=body)


app.include_router(root_router)
app.include_router(
    api_router,
    prefix="/api/v1",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)