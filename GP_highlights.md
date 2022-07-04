---
layout: page
title: Highlights
permalink: /highlights
nav: true
---

<h4> Part I </h4>

{% assign sorted_chapters = site.GPI_chapters | sort:"chapter" %}
{% for entry in sorted_chapters %}
  <a>"{{site.baseurl}}{{entry.permalink}}" {{ entry.title }} </a>: {{ entry.highlights }}
{% endfor %}

<h4> Part II </h4>

{% assign sorted_chapters = site.GPII_chapters | sort:"chapter" %}
{% for entry in sorted_chapters %}
  <a>"{{site.baseurl}}{{entry.permalink}}" {{ entry.title }} </a>: {{ entry.highlights }}
{% endfor %}
