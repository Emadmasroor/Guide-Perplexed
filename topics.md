---
layout: page
title: Topics
permalink: /topics
nav: true
---

Hello, world

{% assign tags =  site.GPI_chapters | map: 'keywords' | join: ','  | split: ',' | uniq %}
{% for tag in tags %}
  {{ tag }}
  {% for page in site.GPI_chapters %}
    {% if page.keywords contains tag %}
      {{ page.title }}
        {{ page.content }}
    {% endif %}
  {% endfor %}
{% endfor %}
