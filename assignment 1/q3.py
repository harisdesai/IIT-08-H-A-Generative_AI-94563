import csv
import os
from typing import List, Dict


def load_products(csv_path: str) -> List[Dict[str, str]]:
    """Load products from a CSV and return a list of dict rows.

    The CSV is expected to have headers: product_name, price, category, quantity
    """
    with open(csv_path, newline='', encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def print_products(rows: List[Dict[str, str]]) -> None:
    print("Products:")
    for r in rows:
        print(f"- {r.get('product_name','')} | Price: {r.get('price','')} | Category: {r.get('category','')} | Qty: {r.get('quantity','')}")


def count_above_price(rows: List[Dict[str, str]], threshold: float) -> int:
    return sum(1 for r in rows if safe_float(r.get('price')) > threshold)


def average_price(rows: List[Dict[str, str]]) -> float:
    prices = [safe_float(r.get('price')) for r in rows]
    return sum(prices) / len(prices) if prices else 0.0


def products_in_category(rows: List[Dict[str, str]], category: str) -> List[str]:
    c = (category or '').strip().lower()
    return [r.get('product_name','') for r in rows if (r.get('category') or '').strip().lower() == c]


def total_quantity(rows: List[Dict[str, str]]) -> int:
    return sum(int(float(r.get('quantity') or 0)) for r in rows)


def safe_float(value: str) -> float:
    try:
        return float(value)
    except Exception:
        return 0.0


def main():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'Products.csv')

    if not os.path.exists(csv_path):
        print(f"Products file not found: {csv_path}")
        return

    rows = load_products(csv_path)

    print_products(rows)

    print(f"Total rows: {len(rows)}")
    print(f"Products with price > 500: {count_above_price(rows, 500)}")
    print(f"Average price: {average_price(rows):.2f}")

    category = input("Enter a category to list products (or press Enter to skip): ")
    if category.strip():
        cats = products_in_category(rows, category)
        print(f"Products in '{category}': {', '.join(cats) if cats else 'None found'}")

    print(f"Total quantity in stock: {total_quantity(rows)}")


if __name__ == '__main__':
    main()
