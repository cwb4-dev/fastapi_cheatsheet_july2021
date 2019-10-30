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

https://www.lucidchart.com/invitations/accept/8a6a16f3-8c3e-4ed1-8f3f-7444e8f2a882

![alt text](/home/lotso/PycharmProjects/fastapi_cheatsheet/FastAPI_cheatsheet_1.png "Logo Title Text 1")



