---

# Expense Tracker CLI

![Release](https://img.shields.io/badge/release-v1.0.0-blue)

A **Python CLI application** for managing personal expenses with **SQLite** + **SQLAlchemy**, featuring budgets, analytics, Excel/PDF exports, encrypted notes, and interactive CLI via Rich.

---

## **Features**

* Add, update, and soft-delete expenses
* Categorize expenses and track monthly budgets
* View monthly totals per category
* Filter/search expenses by category, date, amount, or keyword
* Export to **Excel (.xlsx)** and **PDF (.pdf)**
* Optional **note encryption** using Fernet
* Spending trend visualization (ASCII + chart embedded in PDF)
* Rich interactive CLI with tables, prompts, and panels

---

## **Tech Stack**

* **Python 3.10+**
* **SQLite** via **SQLAlchemy ORM**
* CLI UI: [`rich`](https://github.com/Textualize/rich)
* PDF export: [`fpdf`](https://pypi.org/project/fpdf/)
* Excel export: [`openpyxl`](https://pypi.org/project/openpyxl/)
* Charting: [`matplotlib`](https://matplotlib.org/)
* Optional encryption: [`cryptography`](https://cryptography.io/)

---

## **Setup**

1. **Clone repo**

```bash
git clone https://github.com/CPS7/Expense-Tracker-CLI
cd Expense-Tracker-CLI
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Optional: Enable note encryption**

Create a `.env` file with:

```
EXPENSE_ENCRYPT_NOTES=1
EXPENSE_KEY=<your_32byte_base64_key>
```

> Key must be **32 url-safe base64 bytes**. Encryption can be disabled by setting `EXPENSE_ENCRYPT_NOTES=0` or leaving `EXPENSE_KEY` empty.

---

## **Usage**

Run the CLI app:

```bash
python main.py
```

You’ll see a menu like:

```
1. Add Expense
2. View Expenses
3. Soft Delete Expense
...
14. Exit
```

* Navigate with number input
* Follow prompts for amount, date, note, category, etc.
* Export options available for Excel and PDF reports

---

## **Examples**

**Add an expense:**

```text
Amount (₹): 500
Note: Groceries
Date (YYYY-MM-DD): 2025-11-15
Category: Food
Currency: INR
✔ Expense saved (id: 1)
```

**View monthly category totals:**

```text
Category Totals - November 2025
-------------------------------
Food          1500.00
Transport      800.00
Utilities      300.00
-------------------------------
Total all categories: 2600.00
```

**Export filtered expenses to PDF with trend chart**

```
Search & Export -> Export as PDF -> Embed trend chart: Yes
✔ PDF exported: expenses_report_20251115_221530.pdf
```

---

## **Database Schema**

* `categories` → Expense categories
* `expenses` → Stores individual expenses
* `budgets` → Monthly budgets per category
* `expense_history` → Tracks create/update/delete actions
* `meta_info` → Schema version info

---

## **Notes**

* Soft delete sets `deleted=True`; hard delete removes record.
* Notes cannot be searched reliably if encryption is enabled.
* Budgets trigger warnings at **80% spent** and **100% exceeded**.
* Trend charts are embedded in PDF; temporary files are cleaned automatically.

---

## **License**

MIT License © 2025 CPS7

---
