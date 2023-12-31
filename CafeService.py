import requests
import asyncio
import aiohttp


class CafeService:

    @classmethod
    async def fetch(cls, session, name, url):
        async with session.get(url) as response:
            t = await response.json()
            result = {
                "name": name,
                "data": t
            }
        print(result)
        return result

    async def getProductAsync(self, IDlist):
        urlpre = "http://ec2-13-58-188-11.us-east-2.compute.amazonaws.com:5001/cafe/products?ProductID="
        urls = {}
        for ID in IDlist:
            urls[ID]= urlpre+ID
        result = None
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.ensure_future(
                CafeService.fetch(session, "product "+ID, urls[ID])) for ID in urls.keys()]
            responses = await asyncio.gather(*tasks)
            result = {}
            for response in responses:
                result[response["name"]] = response["data"]

            return result

    async def getProductSync(self):
        url = "http://ec2-13-58-188-11.us-east-2.compute.amazonaws.com:5001/cafe/products?ProductID="
        result = []
        ID = 1
        while True:
            try:
                response = requests.get(url + str(ID))
                if not response.json():
                    break
                temp = response.json()
                temp["id"] = ID
                result.append(temp)
                ID = ID + 1
            except Exception as e:
                print(e)
                break
        return result

    async def getStaffAsync(self, IDlist):
        urlpre = "http://ec2-13-58-188-11.us-east-2.compute.amazonaws.com:5001/cafe/staffs?StaffID="
        urls = {}
        for ID in IDlist:
            urls[ID] = urlpre + ID
        result = None
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.ensure_future(
                CafeService.fetch(session, "Staff "+ID, urls[ID])) for ID in urls.keys()]
            responses = await asyncio.gather(*tasks)
            result = {}
            for response in responses:
                result[response["name"]] = response["data"]

            return result

    async def getStaffSync(self, IDlist):
        url = "http://ec2-13-58-188-11.us-east-2.compute.amazonaws.com:5001/cafe/staffs?StaffID="
        result = {}
        for ID in IDlist:
            response = requests.get(url + ID)
            result[ID] = response.json()

        return result

    async def getCustomerAsync(self, IDlist):
        urlpre = "https://tapioca-402619.an.r.appspot.com/api/customer/"
        urls = {}
        for ID in IDlist:
            urls[ID] = urlpre + ID
        result = None
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.ensure_future(
                CafeService.fetch(session, "Customer "+ID, urls[ID])) for ID in urls.keys()]
            responses = await asyncio.gather(*tasks)
            result = {}
            for response in responses:
                result[response["name"]] = response["data"]

            return result

    async def getCustomerSync(self, IDlist):
        url = "https://tapioca-402619.an.r.appspot.com/api/customer/"
        result = {}
        for ID in IDlist:
            response = requests.get(url + ID)
            result[ID] = response.json()

        return result

    async def getOrderAsync(self, IDlist):
        urlpre = "http://18.119.213.218:8011/orders/"
        urls = {}
        for ID in IDlist:
            urls[ID] = urlpre + ID
        result = None
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.ensure_future(
                CafeService.fetch(session, "Order "+ID, urls[ID])) for ID in urls.keys()]
            responses = await asyncio.gather(*tasks)
            result = {}
            for response in responses:
                result[response["name"]] = response["data"]

            return result

    async def getOrderSync(self):
        url = "http://18.119.213.218:8011/orders/"
        result = []
        ID = 1
        while True:
            try:
                response = requests.get(url + str(ID))
                if not response.json():
                    break
                result.append(response.json())
                ID = ID + 1
            except Exception as e:
                print(e)
                break
        return result

    async def getMeetingSync(self, IDlist):
        url = "http://ec2-13-58-188-11.us-east-2.compute.amazonaws.com:5001/cafe/meetings?MeetingID="
        result = {}
        for ID in IDlist:
            response = requests.get(url + ID)
            result[ID] = response.json()

        return result
