---
layout: page
title: Resources
permalink: /resources
nav: true
---

This is a test page. List all the resources

{% assign sorted_chapters = site.GPI_chapters | sort:"order" %}
{% for entry in site.Resources %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  </h3>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
