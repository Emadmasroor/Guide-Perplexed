---
layout: page
title: Topics
permalink: /topics
nav: true
---

Hello, world

{% assign tags =  site.GPI_chapters | map: 'keywords' | uniq %}
{% for tag in tags %}
  <h3>{{ tag }}</h3>
  {% for page in site.GPI_chapters %}
    {% if page.keywords contains tag %}
    <li><a href="{{ site.baseurl }}{{ note.url }}">{{ page.title }}</a></li>
    {% endif %}
  {% endfor %}
{% endfor %}
