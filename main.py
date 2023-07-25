import asyncio

import aiohttp


async def check():
    while True:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get('https://v4.api.weeat.kr/order/calendar-menu/?f_st=DELIGHT',) as resp:
                    if resp.status == 200:
                        result = await resp.json()
                        result = result['calendar'][4]["rest"]
                        # 돌리는 주 일요일이 0임
                        # 다음주 월요일은 8
                        print(f"A코스 {result['6900A']['rest']}")
                        print(f"B코스 {result['6900B']['rest']}")
                        print('----------------')

                        if result['6900A']['rest'] > 0 or result['6900B']['rest'] > 0:
                            print("떳다!!!!")
                            return
                        else:
                            print("아직 안떳다")

            except aiohttp.ClientConnectorError:
                print('fail')
        await asyncio.sleep(1)

prc = [check()]
asyncio.run(asyncio.wait(prc))
