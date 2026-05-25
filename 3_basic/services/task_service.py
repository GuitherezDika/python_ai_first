import json
from typing import List

from models.task import PracticeTask
from utils.paths import OUTPUT_DIR

def save_one_task(task: PracticeTask):
    filename = f"week{task.week}_day{task.day}.json"
    path = OUTPUT_DIR / filename

    with open(path, 'w') as f:
        json.dump(task.to_json(), f, indent=2)
        # r = read, w = write, a = append, x = create, rb = read binary, wb = write binary
        # json.dump = simpan data Python ke file JSON

def save_tasks(tasks: List[PracticeTask]):
    data = [task.to_json() for task in tasks]
    path = OUTPUT_DIR / "all_tasks.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)