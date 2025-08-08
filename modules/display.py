import textwrap
from tabulate import tabulate
from collections import defaultdict

def wrap_text(text, width=40):
    if not text:
        return ""
    return textwrap.fill(text, width=width)

def print_grouped_table(data, show_specifications=False):
    grouped = defaultdict(list)
    for row in data:
        grouped[row['Type']].append(row)

    for group, items in grouped.items():
        print(f"\033[1;34m\n=== Type: {group} ===\033[0m")

        if show_specifications:
            headers = ["Name", "Type", "Specifications", "Location", "Coordinates", "Google Maps Search"]
        else:
            headers = ["Name", "Type", "Location", "Coordinates", "Google Maps Search"]

        table_data = []
        for item in items:
            if show_specifications:
                row = [
                    item["Name"],
                    item["Type"],
                    wrap_text(item["Specifications"]),
                    wrap_text(item["Location"]),
                    item["Coordinates"],
                    item["Google_Maps_Search"]
                ]
            else:
                row = [
                    item["Name"],
                    item["Type"],
                    wrap_text(item["Location"]),
                    item["Coordinates"],
                    item["Google_Maps_Search"]
                ]
            table_data.append(row)

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", stralign="left"))
        print()
