# 💧 vivaflow



A **lightweight command-line tool** to explore and manage detailed information about **springs, wetlands, and lakes** in East Azerbaijan — all based on an open CSV database.


---

## 🚀 Features

- ✅ List all water sources with clear, categorized output  
- 🔍 Search by name (supports partial matches)  
- 🎯 Filter by type (e.g., hot spring, wetland, mineral spring)  
- 🗂️ Display full details including water specifications and locations  
- 🛠️ Modular design for easy expansion and community contributions  

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/vivastarco/vivaflow.git
cd vivaflow
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

---

## 🎯 Usage

```bash
# List all records (basic info)
python3 main.py --list

# List all records with full details
python3 main.py --list --full

# Search water sources by name
python3 main.py --search "Allah Hagh"

# Filter by type (e.g., "چشمه آبگرم")
python3 main.py --filter "چشمه آبگرم"

# Use custom CSV file
python3 main.py --list --file data/yourfile.csv
```

---

## 🎨 Output Preview

```
=== Type: چشمه آبگرم ===

╔═══════════════════════════════╤═══════════════╤═══════════════════════════════════════╤═══════════════════════╤══════════════════════════════════════════════╗
║ Name                          │ Type          │ Location                              │ Coordinates           │ Google Maps Search                            ║
╠═══════════════════════════════╪═══════════════╪═══════════════════════════════════════╪═══════════════════════╪══════════════════════════════════════════════╣
║ چشمه آبگرم الله‌حق             │ چشمه آبگرم   │ شمال شرقی آبگرم سراب، دره شمالی-جنوبی... │ 37.94° N, 47.53° E    │ چشمه آبگرم الله‌حق یا Allah Hagh Hot Spring   ║
╚═══════════════════════════════╧═══════════════╧═══════════════════════════════════════╧═══════════════════════╧══════════════════════════════════════════════╝
```

---

## 🤝 Contributing

Contributions are welcome!
Add new water sources or extend functionalities.
Just fork, edit/add, and submit a pull request.

---

## 📄 License

MIT License © 2025 Koosha Yeganeh

---

**Enjoy exploring the waters of East Azerbaijan, right from your terminal!** 💧

