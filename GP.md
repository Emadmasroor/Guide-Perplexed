---
layout: page
title: Commentaries on GP
permalink: /GP
nav: true
---

This page should have a collection of the chapter commentaries

{% assign sorted_chapters = site.GP_chapters | sort:"order" %}
{% for entry in sorted_chapters %}
  <h2>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  </h2>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
