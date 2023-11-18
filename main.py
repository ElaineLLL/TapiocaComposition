from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from starlette.responses import JSONResponse

from CafeService import CafeService

app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
service = CafeService()


@app.get("/")
def hello_world():
    return 'Hello, this is Tapioca Cafe'


@app.get("/product_async")
async def async_call():
    IDList = ["1"]
    result = await service.getProductAsync(IDList)
    return JSONResponse(content={"products": result})

@app.get("/product_sync")
async def async_call():
    IDList = ["1"]
    result = await service.getProductSync(IDList)
    return JSONResponse(content={"products": result})

@app.get("/customer_async")
async def async_call():
    IDList = ["1"]
    result = await service.getCustomerAsync(IDList)
    return JSONResponse(content={"customers": result})

@app.get("/customer_sync")
async def async_call():
    IDList = ["1","2"]
    result = await service.getCustomerSync(IDList)
    return JSONResponse(content={"customers": result})

@app.get("/staff_async")
async def async_call():
    IDList = ["1"]
    result = await service.getStaffAsync(IDList)
    return JSONResponse(content={"staffs": result})

@app.get("/order_sync")
async def async_call():
    IDList = ["1","2"]
    result = await service.getOrderAsync(IDList)
    return JSONResponse(content={"orders": result})

@app.get("/order_sync")
async def async_call():
    IDList = ["1","2"]
    result = await service.getOrderSync(IDList)
    return JSONResponse(content={"orders": result})

@app.get("/meeting_sync")
async def async_call():
    IDList = ["1","2"]
    result = await service.getOrderSync(IDList)
    return JSONResponse(content={"meetings": result})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
