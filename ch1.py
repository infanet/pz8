import asyncio
import time


jobs = [
    ("task-1", 2),
    ("task-2", 1),
    ("task-3", 3),
    ("task-4", 2),
    ("task-5", 1),
]

MAX_CONCURRENT = 2


async def process_job(name, delay, semaphore):
    async with semaphore:
        print(f"{name} started")
        await asyncio.sleep(delay)
        print(f"{name} finished")


async def main():
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    start = time.perf_counter()

    tasks = [
        process_job(name, delay, semaphore)
        for name, delay in jobs
    ]
    await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start
    print("Все задания выполнены")
    print(f"Общее время: {elapsed:.2f} секунд")


if __name__ == "__main__":
    asyncio.run(main())