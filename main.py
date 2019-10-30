from enum import Enum

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.status import HTTP_201_CREATED

from customized import fastapi_title, fastapi_description, fastapi_version, \
    fastapi_openapi_url, fastapi_docs_url, fastapi_redoc_url, \
    decorator_response_description, decorator_summary, decorator_description

class Item(BaseModel):
    """This is an item"""
    my_str: str


app = FastAPI(title=fastapi_title,
              description=fastapi_description,
              version=fastapi_version,
              openapi_url=fastapi_openapi_url,
              docs_url=fastapi_docs_url,
              redoc_url=fastapi_redoc_url,
              )


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/get_endpoint_showing_path_params/{path_id}/{model_name}",
         status_code=HTTP_201_CREATED,
         response_description=decorator_response_description,
         summary=decorator_summary,
         # description=decorator_description
)
async def a_get_function(path_id: int, model_name: ModelName):
    """
    Use either a docstring either description kwargs
    in the decorator, if both are set the decorator kwarg takes precedance
    """
    return path_id


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)