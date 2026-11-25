import os
import sys

ENTRY = "ERROR 409: Bread ejected successfully; toast remains a matter of opinion."

if not 1 <= len(ENTRY) <= 120:
    sys.exit("entry length out of range: %d" % len(ENTRY))

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

with open("/output/entry.txt", "rb") as f:
    written = f.read()
if written != ENTRY.encode("utf-8"):
    sys.exit("entry.txt does not match ENTRY byte for byte")
