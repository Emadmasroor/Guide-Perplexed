---
layout: page
title: Highlights
permalink: /GP-highlights
nav: true
---

<h4> Part I </h4>

{% assign sorted_chapters = site.GP_chapters | sort:"chapter" %}
{% for entry in sorted_chapters %}
  {{ entry.title }} : {{ entry.highlights }}
{% endfor %}

<h4> Part II </h4>
