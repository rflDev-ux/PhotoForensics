import marshal

with open("forensic.program", "rb") as f:
    code = marshal.load(f)

exec(code, {"__name__": "__main__"})
