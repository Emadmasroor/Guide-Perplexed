---
layout: page
title: Summaries
permalink: /summaries
nav: true
---

<h2> Part I </h2>

{% assign sorted_chapters = site.GPI_chapters | sort:"chapter" %}
{% for entry in sorted_chapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  {{ entry.highlights }}
  </h3>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}

<h2> Part II </h2>

{% assign sortedchapters = site.GPII_chapters | sort:"chapter" %}
{% for entry in sortedchapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  </h3>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
