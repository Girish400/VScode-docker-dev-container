import eventkit as ev
from time import sleep 
from ib_insync.util import timeit,run as _run
import asyncio

async def Event1(a, b):
    sleep(1)
    print("Running Event 1: ",a * b)

async def Event2(a, b):
    sleep(1)
    print("Running Event 2: ",a / b)

async def Event3():
    print("Start -Event 3")
    await asyncio.sleep(1)
    print("End - Event 3")

event1 = ev.Event()
event1 += Event1

event2 = ev.Event()
event2 += Event2



with timeit():
    with timeit():
        event1.emit(10, 5)
    event2.emit(10, 5)

with timeit():
    _run(Event3(),Event3())