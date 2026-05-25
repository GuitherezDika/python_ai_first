from pathlib import Path
import csv, json, statistics

BASE = Path(__file__).resolve().parents[1]  # project root
CSV_PATH = BASE / "data" / "exercises" / "sample.csv"
REPORT_PATH = BASE / "data" / "exercises" / "mini_practice_report.json"
PLAN_PATH = BASE/'data'/'learning_plan_full.json'

def read_scores(csv_path: Path):
    if not csv_path.exists():
      raise FileNotFoundError(f"CSV file not found: {csv_path}")
    rows = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                s = int(r.get("score", 0))
            except Exception:
                s = 0
            rows.append({"name": r.get('name'), 'score': s})
    return rows

def summarize(rows):
    scores = [r['score'] for r in rows]
    avg = round(statistics.mean(scores), 2) if scores else 0.0
    med = round(statistics.median(scores), 2) if scores else 0.0 # 2 = pembulatan ke 2 desimal
    top3 = sorted(rows, key=lambda r: r['score'], reverse=True)[:3] # ambil 3 teratas berdasarkan score
    # a = [5,4,3,2,1] # print(a[:3]) # [5,4,3] # index 0,1,2
    return {"average": avg, "median": med, "top3": top3, 'count': len(rows)}

def save_report(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"Saved report to {path}")


def mark_plan_done(plan_path: Path, week: int, day: int):
    plan_path = Path(plan_path)
    print(f"Debug: marking plan at {plan_path.resolve()}")
    data = json.loads(plan_path.read_text())
    modified = False
    for idx, it in enumerate(data.get("plan", [])):
        # skip entries that don't have week/day
        if "week" not in it or "day" not in it:
            continue
        if int(it.get("week")) == week and int(it.get("day")) == day:
            if it.get("status") == "DONE":
                print(f"Entry already DONE at index {idx}: week={week} day={day}")
                return
            it["status"] = "DONE"
            modified = True
            print(f"Marked index {idx} as DONE (week={week} day={day})")
            break
    if modified:
        plan_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        print(f"Saved updated plan to {plan_path}")
    else:
        print("Plan entry not found or already DONE.")

def main():
    try:
        rows = read_scores(CSV_PATH)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    summary = summarize(rows)
    report = {'csv_path': str(CSV_PATH), 'summary': summary, 'rows': rows}
    save_report(REPORT_PATH, report)

    mark_plan_done(PLAN_PATH, week=1, day=5) # untuk pemanggilan function
    print("\nSummary:")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    #json.dumps -> ubah objek menjadi string JSON

if __name__ == "__main__":
    main()

    # python3 file_handling_statistic.py