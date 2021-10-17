import asyncio
import eventkit as ev

async def ait(r):
    for i in r:
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for t in ev.Zip(ait('XYZ'), ait('123')):
        print(t)

asyncio.get_event_loop().run_until_complete(main())  # in Jupyter: await main()