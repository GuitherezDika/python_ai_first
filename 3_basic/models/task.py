from dataclasses import dataclass, asdict

@dataclass
class Task:
    week: int
    day: int
    title: str
    est_hours: float
    done: bool = False

    def mark_done(self):
        self.done = True

    def to_json(self):
        return asdict(self)

class PracticeTask(Task):
    def summary(self) -> str:
        status = 'DONE' if self.done else 'PENDING'
        return (
          f"W{self.week}D{self.day} "
          f"-{self.title} " 
          f"[{self.est_hours}h "
          f" - {status}"
        )