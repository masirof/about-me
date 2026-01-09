import csv
import json
import os
from pathlib import Path
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen

CSV_PATH = Path("items.csv")
IMAGES_DIR = Path("images") / "original"
HEADER = ["id", "title", "url", "image", "genre1", "genre2", "comment"]


def fetch_oembed(soundcloud_url: str) -> dict:
    query = urlencode({"format": "json", "url": soundcloud_url})
    oembed_url = f"https://soundcloud.com/oembed?{query}"
    req = Request(oembed_url, headers={"User-Agent": "about-me-script"})
    with urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_image(image_url: str, dest_path: Path) -> None:
    req = Request(image_url, headers={"User-Agent": "about-me-script"})
    with urlopen(req, timeout=30) as resp:
        data = resp.read()
    dest_path.write_bytes(data)


def get_extension_from_url(url: str) -> str:
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext in {".jpg", ".jpeg", ".png", ".webp"}:
        return ext
    return ".jpg"


def main() -> None:
    if not CSV_PATH.exists():
        raise SystemExit(f"Missing {CSV_PATH}")

    rows = []
    max_id = 0
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, skipinitialspace=True)
        header_row = None
        for row in reader:
            if not row:
                continue
            if header_row is None and row[0].strip().lower() == "id":
                header_row = [cell.strip() for cell in row]
                continue
            while len(row) < len(HEADER):
                row.append("")
            if row[0].strip().isdigit():
                max_id = max(max_id, int(row[0].strip()))
            rows.append(row)

    next_id = max_id + 1
    output_rows = []

    for row in rows:
        raw_id = row[0].strip()
        if "soundcloud.com" in raw_id:
            soundcloud_url = raw_id
            comment = row[6].strip() if len(row) > 6 else ""
            try:
                data = fetch_oembed(soundcloud_url)
                title = (data.get("title") or "").strip()
                thumbnail_url = (data.get("thumbnail_url") or "").strip()
                if not thumbnail_url:
                    raise ValueError("Missing thumbnail_url in oembed response")
                ext = get_extension_from_url(thumbnail_url)
                filename = f"{next_id}{ext}"
                IMAGES_DIR.mkdir(parents=True, exist_ok=True)
                download_image(thumbnail_url, IMAGES_DIR / filename)
                new_row = [
                    str(next_id),
                    title,
                    soundcloud_url,
                    filename,
                    "music",
                    "",
                    comment,
                ]
                output_rows.append(new_row)
                next_id += 1
            except (HTTPError, URLError, ValueError, TimeoutError, json.JSONDecodeError) as exc:
                print(f"Failed to fetch {soundcloud_url}: {exc}")
                output_rows.append(row)
        else:
            output_rows.append(row)

    temp_path = CSV_PATH.with_suffix(".csv.tmp")
    with temp_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header_row or HEADER)
        writer.writerows(output_rows)
    temp_path.replace(CSV_PATH)


if __name__ == "__main__":
    main()
