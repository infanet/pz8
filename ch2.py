import asyncio


servers = [
    ("server-1", 1),
    ("server-2", 5),
    ("server-3", 2),
    ("server-4", 4),
]

TIMEOUT = 3


async def request_server(name, delay):
    """Имитация запроса. Возвращает True, если успел, False — если timeout."""
    try:
        await asyncio.wait_for(asyncio.sleep(delay), timeout=TIMEOUT)
        print(f"{name} OK")
        return True
    except asyncio.TimeoutError:
        print(f"{name} TIMEOUT")
        return False


async def main():
    tasks = [
        request_server(name, delay)
        for name, delay in servers
    ]
    results = await asyncio.gather(*tasks)

    successful = sum(results)
    failed = len(results) - successful

    print(f"Successful: {successful}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    asyncio.run(main())