# ...existing code...
import csv
import json
import random
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]  # project root
DATA_DIR = BASE / "data" / "exercises"
DATA_DIR.mkdir(parents=True, exist_ok=True)

def write_sample_text(path: Path):
    text = """Hello Dika!
This is a sample text file.
Line three has some words.
line four is short."""
    with path.open("w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote sample text to {path}")

def read_text_summary(path: Path):
    try:
        with path.open("r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return {"path": str(path), "error": "File not found"}
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        return {"path": str(path), "error": str(e)}

    lines = content.splitlines()
    words = content.split()
    summary = {
        "path": str(path),
        "lines": len(lines),
        "words": len(words),
        "first_line": lines[0] if lines else None
    }
    return summary

def csv_example(csv_path: Path, n: int = 5):
    """
    Write sample CSV with `n` random scores (50-100), then read back and compute average score.
    Returns: dict with 'rows' and 'average'
    """
    sample_names = ["Alice", "Bob", "Charlie", "Dika", "Eve", "Frank", "Grace"]
    rows = [["name", "score"]]
    for i in range(n):
        name = sample_names[i % len(sample_names)]
        score = random.randint(50, 100)
        rows.append([name, score])

    # write CSV
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Wrote sample CSV to {csv_path}")

    # read & compute average
    scores = []
    read_rows = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                s = int(r["score"])
            except Exception:
                continue
            scores.append(s)
            read_rows.append({"name": r.get("name"), "score": s})

    avg = round(sum(scores) / len(scores), 2) if scores else 0.0
    return {"rows": read_rows, "average": avg}

def json_example(json_path: Path):
    data = {
        "project": "file-handling",
        "items": [{"id": 1, "name": "sample"}]
    }
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote sample JSON to {json_path}")

    # read + update
    with json_path.open("r", encoding="utf-8") as f:
        loaded = json.load(f)

    loaded["last_updated"] = "now"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(loaded, f, indent=2)
    return loaded

def save_summary(summary_path: Path, summary: dict):
    with summary_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"Saved summary to {summary_path}")

def main():
    txt = DATA_DIR / 'input.txt'
    csvp = DATA_DIR / "sample.csv"
    js = DATA_DIR / "sample.json"
    summary_out = DATA_DIR / "file_handling_summary.json"

    write_sample_text(txt)
    txt_summary = read_text_summary(txt)
    csv_filtered = csv_example(csvp, n=6)
    js_loaded = json_example(js)

    overall = {
        "text_summary": txt_summary,
        "csv_filtered": csv_filtered,
        "json_loaded": js_loaded
    }
    save_summary(summary_out, overall)
    print("\nSummary (terminal):")
    print(json.dumps(overall, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
# ...existing code...

# guitherezsinaga@Guitherezs-MacBook-Air 2_basic % cd exercises            
# guitherezsinaga@Guitherezs-MacBook-Air exercises % python3 file_handling.py