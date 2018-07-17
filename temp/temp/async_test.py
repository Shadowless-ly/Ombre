import asyncio

async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)

def done_callback(work):
    print('Done')

# print(asyncio.iscoroutinefunction(do_some_work(3)))

work = asyncio.ensure_future(do_some_work(3))
work.add_done_callback(done_callback)
loop = asyncio.get_event_loop()
loop.run_until_complete(work)