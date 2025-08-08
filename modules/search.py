def by_name(db, name):
    return [r for r in db.get_all() if name.lower() in r["Name"].lower()]

def by_type(db, wtype):
    return [r for r in db.get_all() if wtype.lower() in r["Type"].lower()]
