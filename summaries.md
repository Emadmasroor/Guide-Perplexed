---
layout: page
title: Chapter Summaries
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
  {% if entry.highlights %}
    ({{ entry.highlights }})
  {% endif %}
  </h3>
  <p> 
  <a href="{{site.baseurl}}{{page.url}}#top">
      :arrow_up:
  </a>
  <span style="float:right;">
        <a href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ page.part }}.{{ page.chapter }}?lang=en">read on Sefaria</a>
    </span>
  </p>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}

<h2> Part II </h2>

{% assign sortedchapters = site.GPII_chapters | sort:"chapter" %}
{% for entry in sortedchapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  {% if entry.highlights %}
    ({{ entry.highlights }})
  {% endif %}
  </h3>
  <p> 
  <a href="{{site.baseurl}}{{page.url}}#top">
      :arrow_up:
  </a>
  <span style="float:right;">
        <a href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ page.part }}.{{ page.chapter }}?lang=en">read on Sefaria</a>
    </span>
  </p>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
