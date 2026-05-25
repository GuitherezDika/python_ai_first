import json
import sys #modul untuk membaca argumen dari command line
from pathlib import Path
from typing import Optional

BASE = Path(__file__).resolve().parents[1]  # project root
PLAN_PATH = BASE / 'data' / 'learning_plan_full.json'

def load_plan():
  return json.loads(PLAN_PATH.read_text(encoding="utf-8"))

def save_plan(data):
  PLAN_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def next_task():
  data = load_plan()
  for item in data.get("plan", []):
    if not item.get("status"):
      return item
  return None

def mark_done(week: int, day: int):
  data = load_plan()
  for item in data.get("plan", []):
    if item.get("week") == week and item.get("day") == day:
      if item.get("status") == "DONE":
        return False, "alrady DONE"
      item["status"] = "DONE"
      save_plan(data)
      return True, item
  return False, "not found"

def progress_summary():
  data = load_plan()
  total = len(data.get("plan", []))
  done = sum(1 for it in data.get("plan", []) if it.get("status") == 'DONE')
  percent = round(done / total * 100, 1) if total else 0.0
  return {"done": done, "total": total, "percent": percent}


def usage():
    print("Usage: python3 scripts/learning_tracker.py [next|done <week> <day>|summary]")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        usage()
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "next":
        t = next_task()
        if not t:
            print("All tasks done.")
        else:
            print(f"Next: Week {t.get('week')} Day {t.get('day')} - {t.get('focus')} / {t.get('topics')} (Est {t.get('estimated_hours')}h)")
    elif cmd == "done":
        if len(sys.argv) < 4:
            usage()
            sys.exit(1)
        week = int(sys.argv[2]); day = int(sys.argv[3])
        ok, info = mark_done(week, day)
        if ok:
            print(f"Marked DONE: Week {week} Day {day}")
        else:
            print(f"Not updated: {info}")
    elif cmd == "summary":
        s = progress_summary()
        print(f"Progress: {s['done']}/{s['total']} ({s['percent']}%)")
    else:
      usage()