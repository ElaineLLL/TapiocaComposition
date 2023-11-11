from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from typing import List, Union
import uvicorn
import requests
import json
import httpx
import asyncio

from CafeService import CafeService

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def hello_world():
    return 'Hello, this is the composition for Tapioca Cafe'


@app.get("/sync")
async def get_services():
    cafemanagement = {}
    ordermangement = {}
    customerservice = {}

    ## Get cafe management
    url_cafe = f""
    response_cafe = requests.get(url_cafe)
    if response_cafe.status_code == 200:
        cafemanagement = json.loads(response_cafe.content.decode('utf-8'))

    ## Get order management
    url_order = f""
    response_order = requests.get(url_order)
    if response_order.status_code == 200:
        ordermangement = json.loads(response_order.content.decode('utf-8'))

    ## Get customer service
    url_customer = f""
    response_customer = requests.get(url_customer)
    if response_customer.status_code == 200:
        customerservice = json.loads(response_customer.content.decode('utf-8'))

    cafe = CafeService("Tapioca", cafemanagement, ordermangement, customerservice)
    cafe.display()


@app.get("/async")
async def async_get_services():
    url_cafemangement = f""
    url_ordermangement = f""
    url_customerservice = f""

    async with httpx.AsyncClient() as client:
        response_cafe = client.get(url_cafemangement)
        response_order = client.get(url_ordermangement)
        response_customer = client.get(url_customerservice)

        # Use asyncio.gather to wait for all responses
        responses = await asyncio.gather(response_cafe, response_order, response_customer)

    cafemanagement = responses[0].json()
    ordermangement = responses[1].json()
    customerservice = responses[2].json()

    cafe = CafeService("Tapioca", cafemanagement, ordermangement, customerservice)
    cafe.display()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
