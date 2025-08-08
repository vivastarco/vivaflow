def show_table(records):
    if not records:
        print("No results found.")
        return
    
    for r in records:
        print(f"{r['Name']} | {r['Type']} | {r['Location']} | {r['Coordinates']}")
