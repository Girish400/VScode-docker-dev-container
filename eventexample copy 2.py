import eventkit as ev
from ib_insync.util import timeit,run as _run,sleep as _sleep
import asyncio

async def Event1(a, b):
    print("Start -Event 1")
    await asyncio.sleep(1)
    print("Running Event 1: ",a * b)

async def Event2(a, b):
    print("Start -Event 2")
    await asyncio.sleep(1)
    print("Running Event 2: ",a / b)

async def Eventn(a,b,n):
    print(f"Start -Event {n}")
    await asyncio.sleep(1)
    print(f"Running Event {n}",a+b)

event1 = ev.Event()
event1 += Event1

event2 = ev.Event()
event2 += Event2


with timeit():
    with timeit():
        event1.emit(10, 5) 
    event2.emit(10, 5)
    # _run(Eventn(10,5,3),Eventn(10,10,4))

# When the Last line of the above code is removed, None of the code runs, excepts the two timeit methods
# Does this mean futures(Event1 Event2) are running but are not waited hence they do not return and print
# anything?