#!/usr/bin/env python3
"""Fetch books from Goodreads RSS feed and generate _data/books.yml."""

import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.request import Request, urlopen

GOODREADS_USER_ID = os.environ.get("GOODREADS_USER_ID", "84711341")
RSS_URL = f"https://www.goodreads.com/review/list_rss/{GOODREADS_USER_ID}?shelf=read"


def slugify(text):
    """Match Jekyll's default slugify behavior."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text.strip("-")


def yaml_escape(s):
    """Escape a string for YAML output."""
    if not s:
        return '""'
    if any(c in s for c in ":'\"{}[],&*?|<>=!%@#`"):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def fetch_rss(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def parse_year(date_str):
    """Extract year from Goodreads date string."""
    if not date_str:
        return None
    try:
        dt = datetime.strptime(date_str.strip(), "%a, %d %b %Y %H:%M:%S %z")
        return dt.year
    except ValueError:
        pass
    match = re.search(r"\b(20\d{2})\b", date_str)
    return int(match.group(1)) if match else None


def get_text(item, tag):
    el = item.find(tag)
    return el.text.strip() if el is not None and el.text else ""


def parse_books(xml_data):
    root = ET.fromstring(xml_data)
    books = []
    for item in root.findall(".//item"):
        title = get_text(item, "title")
        if not title:
            continue
        author = get_text(item, "author_name")
        rating = get_text(item, "user_rating")
        date_read = get_text(item, "user_read_at")
        date_added = get_text(item, "user_date_added")
        book_id = get_text(item, "book_id")
        isbn = get_text(item, "isbn")

        year = parse_year(date_read) or parse_year(date_added)

        books.append({
            "title": title,
            "author": author,
            "rating": int(rating) if rating else 0,
            "year": year,
            "slug": slugify(title),
            "goodreads_id": book_id,
            "isbn": isbn,
        })
    return books


def write_yaml(books, path):
    books.sort(key=lambda b: (-(b["year"] or 0), b["title"].lower()))
    with open(path, "w") as f:
        f.write("# Auto-generated from Goodreads RSS — do not edit by hand.\n")
        f.write("# To fix a slug mismatch with a notes page, override the slug field.\n\n")
        for book in books:
            f.write(f"- title: {yaml_escape(book['title'])}\n")
            f.write(f"  author: {yaml_escape(book['author'])}\n")
            f.write(f"  rating: {book['rating']}\n")
            f.write(f"  year: {book['year'] or 'null'}\n")
            f.write(f"  slug: {yaml_escape(book['slug'])}\n")
            f.write(f"  goodreads_id: {yaml_escape(book['goodreads_id'])}\n")
            f.write(f"  isbn: {yaml_escape(book['isbn'])}\n")


def main():
    os.makedirs("_data", exist_ok=True)

    all_books = []
    page = 1
    while True:
        url = f"{RSS_URL}&page={page}&per_page=200"
        print(f"Fetching page {page}...")
        try:
            xml_data = fetch_rss(url)
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break
        books = parse_books(xml_data)
        if not books:
            break
        all_books.extend(books)
        page += 1
        if page > 20:  # safety limit
            break

    if not all_books:
        print("No books returned from Goodreads — keeping existing data.")
        return

    write_yaml(all_books, "_data/books.yml")
    print(f"Updated _data/books.yml with {len(all_books)} books")


if __name__ == "__main__":
    main()
