#Async IO on specific function using Python
import asyncio

async def main():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(5)
    print("B")
    return_value = await task
    print(f'Return value was {return_value}')

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 5

asyncio.run(main())