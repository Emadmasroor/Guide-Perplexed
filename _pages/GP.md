---
layout: page
title: Commentaries on GP
permalink: /test/
nav: false
---

Sandbox for trying out Jekyll, Markdown, Liquid, HTML, etc.

{% for entry in site.GP_chapters %}
  <h2>
    <a href="{{entry.url }}">
      {{ entry.title }}
  </h2>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
