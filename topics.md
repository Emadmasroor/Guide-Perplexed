---
layout: page
title: Topics
permalink: /topics
nav: true
---

Hello, world

{% assign tags =  site.GPI_chapters map: 'keywords' | join: ','  | split: ',' | uniq %}
{% for tag in tags %}
  <h1>{{ tag }}</h1>
  {% for page in site.GPI_chapters %}
    {% if page.keywords contains tag %}
      <h2>{{ page.title }}</h2>
      {{page.title}} contains keyword {{ tag }}. We reproduce the text of this chapter below:
      {{ page.content }}
    {% endif %}
  {% endfor %}
{% endfor %}
