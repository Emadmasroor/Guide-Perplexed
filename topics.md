---
layout: page
title: Topics
permalink: /topics
nav: true
---

{% assign tags =  site.GPI_chapters | map: 'keywords' | join: ','  | split: ',' | uniq %}
{% for tag in tags %}
  <h1>{{ tag }}</h1>
  {% for page in site.GPI_chapters %}
  {% if page.keywords contains tag %}
  <h4>{{ page.title }}</h4>
  {{ page.content }}
  {% endif %}
  {% endfor %}
{% endfor %}
