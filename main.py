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
    IDList = ["1","2"]
    result = await service.getProductAsync(IDList)
    return JSONResponse(content={"message": "This is from async get.","products": result})

@app.get("/product_sync")
async def async_call():
    IDList = ["1","2"]
    result = await service.getProductSync(IDList)
    return JSONResponse(content={"message": "This is from sync get.","products": result})

@app.get("/customer_async")
async def async_call():
    IDList = list(range(1,6))
    IDList = map(str,IDList)
    result = await service.getCustomerAsync(IDList)
    return JSONResponse(content={"message": "This is from async get.","customers": result})

@app.get("/customer_sync")
async def async_call():
    IDList = ["1","2","3"]
    result = await service.getCustomerSync(IDList)
    return JSONResponse(content={"message": "This is from sync get.","customers": result})

@app.get("/staff_async")
async def async_call():
    IDList = ["1","2","3","4","5"]
    result = await service.getStaffAsync(IDList)
    return JSONResponse(content={"message": "This is from sync get.","message": "This is from async get.","staffs": result})

@app.get("/staff_sync")
async def async_call():
    IDList = ["1","2"]
    result = await service.getStaffSync(IDList)
    return JSONResponse(content={"message": "This is from sync get.","staffs": result})

@app.get("/order_async")
async def async_call():
    IDList = ["1","2","3","4","5"]
    result = await service.getOrderAsync(IDList)
    return JSONResponse(content={"message": "This is from async get.","orders": result})

@app.get("/order_sync")
async def async_call():
    IDList = ["1","2","3","4","5"]
    result = await service.getOrderSync(IDList)
    return JSONResponse(content={"message": "This is from sync get.","orders": result})

@app.get("/meeting_sync")
async def async_call():
    IDList = ["1","2"]
    result = await service.getOrderSync(IDList)
    return JSONResponse(content={"message": "This is from sync get.","meetings": result})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
