# DASAR ASYNC & AWAIT
import asyncio
import random

# ======= ASYNCIO BASIC CONCEPTS ===========
# async def hello():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("World")

# asyncio.run(hello());
# Hello + 2 detik + World

# async def task11():
#     print("Task started")
#     await asyncio.sleep(3)
#     print("Task completed")
# asyncio.run(task11());
# python3 basic.py

# async def task(name):
#     print(f"Start {name}")
#     await asyncio.sleep(2)
#     print(f"Done {name}")

# async def main():
#     await task("A")
#     await task("B")

# asyncio.run(main());
# berjalan sequential task A selesai dulu baru task B jalan, total waktu 4 detik

# =========== CONCURRENT CONCEPT =============
# async def task2(name):
#     print(f"Start {name}")
#     await asyncio.sleep(2)
#     print(f"Done {name}")

# async def main2():
#     await asyncio.gather(
#         task2("A"),
#         task2("B")
#     )

# asyncio.run(main2());
# berjalan bersama dan selesai dalam 2 detik

# ========= ASYNCIO CREATE_TASK() ==============
# async def worker():
#   await asyncio.sleep(2)
#   print("Worker done")

# async def main3():
#   asyncio.create_task(worker())
#   print("Main jalan terus")
#   await asyncio.sleep(3)  # Menunggu worker selesai

# asyncio.run(main3());
# Main Jalan Terus: + 2 detik -> Worker done
# -> asyncio.sleep(3) juga sedang berjalan 

# ========= HANDLE ERROR ==============
# async def task3():
#   try:
#     await asyncio.sleep(1)
#     print(10/0)
#   except Exception as e:
#     print(f"Error: {e}")

# asyncio.run(task3());
# Error: division by zero

# ========= SIMULASI API CALL ==============
# async def fetch_user():
#     await asyncio.sleep(2)
#     return {"name": "Dika"}

# async def fetch_posts():
#     await asyncio.sleep(4)
#     return ["Post 1", "Post 2"]

# async def main4():
#     user, posts = await asyncio.gather( # TUNGGU SEMUA SELESAI DULU
#       fetch_user(),
#       fetch_posts()
#     )
#     print(user)
#     print(posts)

# asyncio.run(main4());
# 0s: main4 -> run fetch_user(), fetch_posts() bersamaan
# 2s: fetch_user() selesai, fetch_posts() masih berjalan
# 4s: fetch_posts() selesai, main4 lanjut print user dan posts
# 4s: gather selesai total
# 4s: print dijalankan

# ========= ASYNC DOWNLOADER SIMULATOR ==============
async def download(file):
    delay = random.randint(1, 5)
    print(f"Downloading {file}...")
    await asyncio.sleep(delay)
    print(f"Finished ${file}")

async def main5():
    tasks = []
    for i in range(5):
        tasks.append(download(f"file-{i}"))
    
    await asyncio.gather(*tasks)

asyncio.run(main5());