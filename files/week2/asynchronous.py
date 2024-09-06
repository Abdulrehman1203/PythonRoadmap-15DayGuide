import asyncio


async def fibonacci(n):
    a, b = 0, 1
    while True:
        c = a + b
        if c >= n:
            break
        await asyncio.sleep(1)
        yield c
        a, b = b, c
    return


async def main():
    f = fibonacci(10)
    async for num in f:
        print(num)


asyncio.run(main())