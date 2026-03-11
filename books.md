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
> - Dr. Seuss

{% assign book_pages = site.pages | where_exp: "p", "p.url contains '/books/'" | sort: "title" %}
{% for page in book_pages %}{% if page.url != "/books/" %}- [**{{ page.title }}**]({{ page.url }})
{% endif %}{% endfor %}
