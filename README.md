# fastapi_cheatsheet

The aim of this repo is to have a simple FastAPI application and show the various 
effects of such and such parameter in the code on the swagger UI generated in a visual way

# notes while doing this on potentially simplifying usage
1. in FastAPI object, pydantic type for `openapi_url`, `docs_url`, `redoc_url` could be stricter and impose having a forward slash imposed.
2. in route decorator, the order of kwargs makes no sense, group them in sensible buckets, ie for instance `status_code` should be with `response_description`
3. in route decorator the kwarg `summary` is not explicit enough imho
4. explain precedance of various elements better in the docs


# FastAPI title, description
Generated using LucidChart, save as png with transparent background, 300dpi

You can comment here:

https://www.lucidchart.com/invitations/accept/b36921b1-7ffc-47bd-8487-fb2ca40e1e7e

![alt text](/home/lotso/PycharmProjects/fastapi_cheatsheet/FastAPI_cheatsheet_1.png "Logo Title Text 1")



