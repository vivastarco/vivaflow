#!/usr/bin/env python3
import argparse
from modules import database, search, display

DEFAULT_DATA = "data/Springs_and_Wetlands_East_Azerbaijan.csv"

def main():
    parser = argparse.ArgumentParser(
        description="Water Information CLI - Springs, Wetlands, and Lakes Database"
    )
    parser.add_argument("--list", action="store_true", help="List all records")
    parser.add_argument("--search", metavar="NAME", help="Search by name")
    parser.add_argument("--filter", metavar="TYPE", help="Filter by type (e.g., چشمه آبگرم, تالاب)")
    parser.add_argument("--file", metavar="CSV_FILE", default=DEFAULT_DATA, help="Path to CSV file")
    parser.add_argument("--full", action="store_true", help="Show full details including Specifications")

    args = parser.parse_args()

    db = database.Database(args.file)

    if args.list:
        data = db.get_all()
        display.print_grouped_table(data, show_specifications=args.full)
    elif args.search:
        results = search.by_name(db, args.search)
        display.print_grouped_table(results, show_specifications=args.full)
    elif args.filter:
        results = search.by_type(db, args.filter)
        display.print_grouped_table(results, show_specifications=args.full)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
