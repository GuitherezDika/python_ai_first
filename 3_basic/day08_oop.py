from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import List

BASE = Path(__file__).resolve().parents[1]
# __file__ = "/AI_ENGINEER/three_basic/day08_oop.py"
# resolve = absolute path
# parents[1] = /AI_ENGINEER
OUT = BASE/"outputs" #/AI_ENGINEER/outputs
OUT.mkdir(parents=True, exist_ok=True)
# buat folder outputs jika belum ada; dan kalau sudah ada, tidak akan error

# kalau tanpa @dataclass, kita harus buat __init__ sendiri dan pemanggilan denga self.property
@dataclass 
class Task:
    week: int
    day: int
    title: str
    est_hours: float
    done: bool = False

    def mark_done(self): # self refers to the instance of Task
        self.done = True

    def to_json(self):
        return asdict(self)

    def save_one_task(self):
        filename = f"week{self.week}_day{self.day}.json"
        path = OUT / filename

        with open(path, 'w') as f: # buka file -> operasi pada file -> tutup file (wajib pakai with)
            json.dump(self.to_json(), f, indent=2)
        # r = read, w = write, a = append, x = create, rb = read binary, wb = write binary
        # json.dump = simpan data Python ke file JSON

class PracticeTask(Task):
    def summary(self) -> str: #self = instance dari Task # akan return string
        status = 'DONE' if self.done else 'PENDING'
        return f"W{self.week}D{self.day} - {self.title} [{self.est_hours}h] - {status}"
        # f = function  

def save_tasks(tasks: List[PracticeTask]):
    data = [t.to_json() for t in tasks]
    path = OUT/"all_tasks.json"
    with open(path, "w") as f: # f = file
        json.dump(data, f, indent=2)

task1 = PracticeTask(week=1, day=1, title="Learn Python Basics", est_hours=2.0)
# W1D1 - Learn Python Basics [2.0h] - PENDING
task1.mark_done()
# W1D1 - Learn Python Basics [2.0h] - DONE
# task1.save_task(task1) # simpan task1 ke file JSON
print(task1.to_json()) # {'week': 1, 'day': 1, 'title': 'Learn Python Basics', 'est_hours': 2.0, 'done': True}
task1.save_one_task()

# ==== LIST ==== 
tasks: List[PracticeTask] = []
task2 = PracticeTask(week=1, day=2, title="Learn and practice Data Structures", est_hours=2.0)
task3 = PracticeTask(week=1, day=3, title="Learn and practice Functions", est_hours=2.0)
task4 = PracticeTask(week=1, day=4, title="Learn and practice File Handling", est_hours=2.0)
task5 = PracticeTask(week=1, day=5, title="Learn and practice Mini Practice", est_hours=2.0)
task6 = PracticeTask(week=1, day=6, title="Learn and practice Light Review", est_hours=2.0)
task7 = PracticeTask(week=1, day=7, title="Learn and practice Rest", est_hours=2.0)
tasks.extend([task1, task2, task3, task4, task5, task6, task7])

for t in tasks:
    t.mark_done()
    t.to_json()
    t.save_one_task()

save_tasks(tasks)