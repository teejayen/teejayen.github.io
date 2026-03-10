---
title: Books
permalink: books/
layout: page
published: true
sitemap:
  lastmod: 2020-06-10
  priority: 0.7
  changefreq: 'weekly'
---

>"The more that you read, the more things you will know. The more that you learn, the more places you'll go."
>
>— Dr. Seuss

{% assign book_pages = site.pages | where_exp: "p", "p.url contains '/books/'" %}
{% assign books_by_year = site.data.books | group_by: "year" | sort: "name" | reverse %}

{% for year_group in books_by_year %}
{% if year_group.name != "" %}

## {{ year_group.name }}

{% assign sorted_books = year_group.items | sort: "title" %}
{% for book in sorted_books %}
{% assign book_url = "/books/" | append: book.slug | append: "/" %}
{% assign note_page = book_pages | where_exp: "p", "p.url == book_url" | first %}
{% if note_page %}- [**{{ book.title }}**]({{ book_url }}) ({{ book.author }})
{% else %}- **{{ book.title }}** ({{ book.author }})
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
