#!/usr/bin/env python3
import argparse
import sys
from modules import database, search, display

DEFAULT_DATA = "data/Springs_and_Wetlands_East_Azerbaijan.csv"

def main():
    parser = argparse.ArgumentParser(
        description="Water Information CLI - Springs, Wetlands, and Lakes Database"
    )

    parser.add_argument("--list", action="store_true", help="List all records")
    parser.add_argument("--search", metavar="NAME", help="Search by name")
    parser.add_argument("--filter", metavar="TYPE", help="Filter by type (e.g., spring, wetland)")
    parser.add_argument("--file", metavar="CSV_FILE", default=DEFAULT_DATA, help="Path to CSV file")
    
    args = parser.parse_args()

    db = database.Database(args.file)

    if args.list:
        display.show_table(db.get_all())
    elif args.search:
        results = search.by_name(db, args.search)
        display.show_table(results)
    elif args.filter:
        results = search.by_type(db, args.filter)
        display.show_table(results)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
