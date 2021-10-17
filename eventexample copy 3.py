import eventkit as ev
from ib_insync.util import timeit,run as _run
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


async def main():
    await asyncio.sleep(0)
    with timeit():
        with timeit():
            event1.emit(10, 5) 
        event2.emit(10, 5)


## Block 1
## This will start the coroutines(Event1,Event2), but since they are not awaited on emit, will not execute all the coroutines print statememts
# Question 1: Does this mean the coroutines will keep exeucting, finish in background and never return to event loop? 
# Quesition 2: Will the emit work as Non-Blocking callbacks?
# if __name__ == '__main__':
#     with timeit():
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(main())


# Block 2
# This will start the coroutines(Event1, Event2) and since the loop will run forverever, the coroutines are returned
# to the event loop and all print statements will get executed in the coroutine 
# Question 3: Correct?
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.run_forever()
    

## Block 3
# This will start the coroutines(Event1,Event2). 
# Question 4: Introducing a new coroutine and running it with asyncio, why does the coroutines(Event1 and Event2)  
# print statements get executed?
# if __name__ == '__main__':
#     with timeit():
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(main())
#         _run(Eventn(10,5,3),Eventn(10,10,4))
