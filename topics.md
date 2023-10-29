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
      <a href="{{site.baseurl}}{{page.url}}">{{ page.title }}</a>
      {{ page.content }}
    {% endif %}
  {% endfor %}
{% endfor %}
