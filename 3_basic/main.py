from models.task import PracticeTask
from services.task_service import (save_one_task, save_tasks)

def main():
    task1 = PracticeTask(week=1, day=1, title="Learn Python Basics", est_hours=2.0)
    print(task1.summary())
    task1.mark_done()
    print(task1.summary())
    save_one_task(task1)

    tasks = [
        task1,
        PracticeTask(week=1, day=2, title="Learn and practice Data Structures", est_hours=2.0),
        PracticeTask(week=1, day=3, title="Learn and practice Functions", est_hours=2.0),
    ]

    for task in tasks:
        task.mark_done()
        save_one_task(task)
    
    save_tasks(tasks)

if __name__ == "__main__":
    main()