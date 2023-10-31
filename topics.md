---
layout: page
title: Topics
permalink: /topics
nav: true
---

{% assign tags =  site.GPI_chapters | map: 'keywords' | join: ','  | split: ',' | uniq %}
{% for tag in tags %}
  <h4>{{ tag }}</h4>
  {% for page in site.GPI_chapters %}
  {% if page.keywords contains tag %}
  <h2>{{ page.title }}</h2>
  {{ page.content }}
  {% endif %}
  {% endfor %}
{% endfor %}
