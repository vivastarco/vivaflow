def by_name(db, name_query):
    name_query = name_query.lower()
    return [row for row in db.get_all() if name_query in row['Name'].lower()]

def by_type(db, type_query):
    type_query = type_query.lower()
    return [row for row in db.get_all() if type_query in row['Type'].lower()]
