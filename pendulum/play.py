import asyncio
import time

"""
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


"""



some_list = []

def pop_item():
    while True:
        tick = time.perf_counter()
        item = '1'
        #print(1/25 - (time.perf_counter() - tick))
        #time.sleep(1/25 - (time.perf_counter() - tick))
        if 1/25 - (time.perf_counter() - tick) > 0:
            time.sleep(1/25 - (time.perf_counter() - tick))
        yield item

"""

async def fill_list():

    while True:
        if len(some_list)<10:
            some_list.append('some_item')
            print('item_added')
        await asyncio.sleep(0.00001)

"""

"""

tick = time.perf_counter()
gen = pop_item()

for i in range(250):
    next(gen)
    print(i, time.perf_counter() - tick)
    if time.perf_counter() - tick == 10:
        break
"""
"""
async def main():

    #blocking_task = asyncio.create_task(pop_item())
    non_blocking_task = asyncio.create_task(fill_list())

    async for item in pop_item():
        await non_blocking_task
        yield item


    #while True:
    #    await blocking_task
    #    await non_blocking_task

#asyncio.run(main())

async def mainer():

    async for item in main():
        print(item)
        
asyncio.run(mainer())

"""

def gen():
    i=0
    print(i)
    

    while True:
        i+=1
        yield i

if __name__=='__main__':

    gen = gen()

    print(next(gen))
    print(next(gen))
    print(next(gen))