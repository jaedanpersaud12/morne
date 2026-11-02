#!/usr/bin/env python3
"""Rename the cast across every .md in the project. Word-boundary safe. Idempotent.
Usage: python3 scripts/rename-cast.py [project_root]
"""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
MAP = {
  # the six + Jem
  "Imani":"Juno","Danny":"Tock","Micah":"Olli","Kai":"Fen","Asha":"Lyra","Tori":"Sol","Nia":"Kit",
  # surnames (singular and possessive-plural forms)
  "Clarke":"Vale","Clarkes":"Vales","Mohan":"Quill","Mohans":"Quills","Achong":"Finch","Achongs":"Finches",
  "Baptiste":"Hale","Baptistes":"Hales","Pierre":"Wick","Ramkissoon":"Pell","Ramkissoons":"Pells",
  "Ali":"Moss","Alis":"Mosses","Lall":"Nettle","Lalls":"Nettles","Charles":"Lark","Mohammed":"Harker",
  # compound kids
  "Jaylen":"Bix","Troy":"Cass","Farah":"Ida","Vashti":"Velora",
  # the road
  "Janelle":"Wren","Jaden":"Pip","Devon":"Tam","Pauline":"Orla",
  # harbour
  "Jerome":"Cole","Keisha":"Nell","Dev":"Dax","Keon":"Ludo","Shanice":"Mira","Javon":"Zeb","Shawn":"Hob","Renee":"Lux",
  # hills and shore
  "Ezra":"Moth","Cyril":"Tobit","Bernadette":"Hesper","Shakira":"Zuzu","Shak":"Zu",
  # adults
  "Winston":"Ambrose","Pearl":"Dot","Yvonne":"Tilda","Sunita":"Prue",
}
FILES = {"imani":"juno","danny":"tock","micah":"olli","kai":"fen","asha":"lyra","tori":"sol","nia":"kit"}
pat = re.compile(r"\b(" + "|".join(sorted(MAP, key=len, reverse=True)) + r")\b")
changed = 0
for p in (root / "bible").rglob("*.md"):
    s = p.read_text(encoding="utf-8")
    t = pat.sub(lambda m: MAP[m.group(1)], s)
    t = t.replace("Dr. H. Moss", "Dr. Hollis Moss")
    for a, b in FILES.items():
        t = t.replace(f"cast/{a}.md", f"cast/{b}.md").replace(f"({a}.md", f"({b}.md")
    if t != s:
        p.write_text(t, encoding="utf-8"); changed += 1
cast = root / "bible" / "cast"
if cast.exists():
    for a, b in FILES.items():
        src, dst = cast / f"{a}.md", cast / f"{b}.md"
        if src.exists() and not dst.exists():
            src.rename(dst); print("renamed", src.name, "->", dst.name)
print("files changed:", changed)
