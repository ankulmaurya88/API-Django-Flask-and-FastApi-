
                                #  🔹 LEVEL 1 — Coroutine Mechanics (Foundation)
import asyncio

# async def greet():
#     print("Start")
#     await asyncio.sleep(1)
#     print("End")

# coro = greet()
# print(type(coro))

# async def task():
#     print("A")
#     await asyncio.sleep(3)
#     print("B")
#     await asyncio .sleep(1)
#     print("c")


# async def task():
#     print("A")
#     await asyncio.sleep(1)
#     print("B")
#     await asyncio.sleep(1)
#     print("C")

# asyncio.run(task())


                                                # 🔹 LEVEL 2 — Concurrency Understanding

# async def work(n):
#     await asyncio.sleep(2)
#     return n

# # async def main():
# #     for i in range(3):
# #         await work(i)

# async def main():
#     tasks =[work(i) for i in range(3)]
#     await asyncio.gather(*tasks)


                                                # LEVEL 3 — Understand create_task




# async def worker():
#     print("start worker")

#     await asyncio.sleep(2)
#     print("End worker")



# async def main():
#     asyncio.create_task(worker())
#     print("main continues")
#     # await asyncio.sleep (3)
#     await asyncio

                                         # 🔹 LEVEL 4 — Blocking vs Non-Blocking (CRITICAL)


# import time

# async def bad():
#     # time.sleep(2)   # blocking
#     await asyncio.sleep(2)
#     print("Done")

# async def main():
#     await asyncio.gather(bad(), bad())



                                                # 🔹 LEVEL 5 — Real Backend Simulation
# async def fetch_data(n):
#     print(f"Fetching {n}")
#     await asyncio.sleep(2)
#     print(f"Done {n}")

                                                    # 🔹 LEVEL 6 — Advanced Control


import asyncio

async def slow():
    print("Started slow task")
    await asyncio.sleep(5)
    print("Finished slow task")

async def main():
    try:
        await asyncio.wait_for(slow(), timeout=2)
    except asyncio.TimeoutError:
        print("Task timed out!")

asyncio.run(main())


print(asyncio.get_running_loop())

if __name__ == "__main__":
    # level-1
    # asyncio.run(task())
    # # await task()
    # asyncio.run(task())
    # asyncio.run(task())

    # level-2
    # asyncio.run(main())


    # levele-3

    # asyncio.run(main())

    # level-4

    # asyncio.run(main())
    # level-5
    # asyncio.run(fetch_data(5))

    # level-6

    asyncio.run(slow())


