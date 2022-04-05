---
layout: page
title: Commentaries on GP
permalink: /GP
nav: true
---

This page should have a collection of the chapter commentaries

{% for entry in site.GP_chapters %}
  <h2>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  </h2>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
