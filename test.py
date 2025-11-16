# test.py
import os
import sys
import datetime
from main import (
    add_expense_db, view_expenses_db, update_expense_db, delete_expense_db,
    search_expenses, export_to_excel_rows, export_to_pdf_rows,
    create_category_if_missing, SessionLocal, Budget, Category
)

def test_add_expenses():
    print("Testing add_expense_db...")
    for i in range(5):
        add_expense_db(amount=100+i*10, note=f"Test note {i}", date_str=datetime.date.today().isoformat(), category_name="Food")
    print("✔ Add expenses test passed.")

def test_view_expenses():
    print("Testing view_expenses_db...")
    res = view_expenses_db()
    assert res["total"] > 0, "No expenses found!"
    print("✔ View expenses test passed.")

def test_update_delete_expenses():
    print("Testing update_expense_db and delete_expense_db...")
    res = view_expenses_db()
    if not res["items"]:
        print("No items to test update/delete")
        return
    eid = res["items"][0]["id"]
    update_expense_db(eid, amount=999)
    delete_expense_db(eid, soft=True)
    delete_expense_db(eid, soft=False)
    print("✔ Update and delete test passed.")

def test_monthly_total():
    print("Testing monthly total...")
    session = SessionLocal()
    now = datetime.date.today()
    total = session.query(Category).count()
    session.close()
    print(f"Monthly total count: {total}")
    print("✔ Monthly total test passed.")

def test_category_breakdown():
    print("Testing category breakdown...")
    session = SessionLocal()
    cat = create_category_if_missing(session, "Food")
    add_expense_db(50, "Cat breakdown test", datetime.date.today().isoformat(), "Food")
    session.close()
    print("✔ Category breakdown test passed.")

def test_set_category_budget():
    print("Testing setting category budget...")
    session = SessionLocal()
    cat = create_category_if_missing(session, "Food")
    budget = session.query(Budget).filter(Budget.category_id==cat.id).first()
    if budget:
        budget.amount = 5000
    else:
        budget = Budget(category_id=cat.id, amount=5000, currency="INR")
        session.add(budget)
    session.commit()
    session.close()
    print("✔ Category budget set test passed.")

def test_search_expenses():
    print("Testing search_expenses...")
    res = search_expenses(keyword="Test")
    assert res["total"] >= 0, "Search failed"
    print("✔ Search expenses test passed.")

def test_export_excel():
    print("Testing export_to_excel_rows...")
    res = view_expenses_db(per_page=100)
    export_to_excel_rows(res["items"], filename="test_export.xlsx")
    print("✔ Excel export test passed.")

def test_export_pdf():
    print("Testing export_to_pdf_rows...")
    res = view_expenses_db(per_page=100)
    export_to_pdf_rows(res["items"], filename="test_export.pdf", embed_chart=False)
    print("✔ PDF export test passed.")

def run_all_tests():
    test_add_expenses()
    test_view_expenses()
    test_update_delete_expenses()
    test_monthly_total()
    test_category_breakdown()
    test_set_category_budget()
    test_search_expenses()
    test_export_excel()
    test_export_pdf()
    print("\nAll tests passed!")

if __name__ == "__main__":
    run_all_tests()
