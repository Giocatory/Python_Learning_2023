import asyncio


async def first_def():
    await asyncio.sleep(5)
    print(first_def.__name__)


async def second_def():
    await asyncio.sleep(3)
    print(second_def.__name__)


loop = asyncio.get_event_loop()
task1 = loop.create_task(first_def())
task2 = loop.create_task(second_def())
loop.run_until_complete(asyncio.wait([task1, task2]))

# second_def
# first_def
