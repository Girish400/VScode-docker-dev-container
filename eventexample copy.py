import eventkit as ev
from time import sleep 
from ib_insync.util import timeit
from ib_insync.util import run as _run
import asyncio

def Event1(a, b):
    sleep(1)
    print("Running Event 1: ",a * b)

def Event2(a, b):
    sleep(1)
    print("Running Event 2: ",a / b)

async def test():
    print("Printing test")
    await asyncio.sleep(1)
    print("Girish")

event1 = ev.Event()
event1 += Event1

event2 = ev.Event()
event2 += Event2



with timeit():
    with timeit():
        event1.emit(10, 5)
    event2.emit(10, 5)

with timeit():
    _run(test(),test())