---
layout: page
title: Chapter Summaries
permalink: /summaries
nav: true
---

<h2> Part 1 </h2>

{% assign sorted_chapters = site.GPI_chapters | sort:"chapter" %}
{% for entry in sorted_chapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      Part 1, {{ entry.title }}
    </a>
  </h3>
  <p style="font-weight: bold; font-size: 20px">
    {% if entry.highlights %}
      {{ entry.highlights }}
  {% endif %}
  </p>
  <p style="text-align:left;"> 
  <a href="{{site.baseurl}}{{page.url}}#top">
      :arrow_up:
  </a>
  <span style="float:right;">
        <p style="text-align:right; font-size:10px">
    Read it in Arabic:
        <a href="https://archive.org/details/DelalatolHaerin_201804/page/n{{ entry.pnum }}"><img src="/Guide-Perplexed/assets/internetarchive_icon.svg" height=24em></a>
  </p>
  <p style="text-align:right; font-size:10px">
    Read it in English & Hebrew:
        <a href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=en"><img src="/Guide-Perplexed/assets/sefaria_icon.svg" height=12em></a>
  </p>
    </span>
  </p>
  <p>{{ entry.content | markdownify }}</p>
  <p style="font-size: 10px;text-align:right">
      <a href="https://github.com/Emadmasroor/Guide-Perplexed/blob/main/{{ entry.path }}">Edit this page on GitHub</a>
    </p>
{% endfor %}

<h2> Part 2 </h2>

{% assign sortedchapters = site.GPII_chapters | sort:"chapter" %}
{% for entry in sortedchapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      Part 2, {{ entry.title }}
    </a>
  </h3>
  <p style="font-weight: bold; font-size: 20px">
    {% if entry.highlights %}
      {{ entry.highlights }}
  {% endif %}
  </p>
  <p style="text-align:left;"> 
  <a href="{{site.baseurl}}{{page.url}}#top">
      :arrow_up:
  </a>
  <span style="float:right;">
       Arabic: 
        <a href="https://archive.org/details/DelalatolHaerin_201804/page/n{{ entry.pnum }}"><img src="/Guide-Perplexed/assets/internetarchive_icon.svg" height=24em></a>
        |English & Hebrew: 
        <a href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=en"><img src="/Guide-Perplexed/assets/sefaria_icon.svg" height=12em></a>
    </span>
  </p>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}

<h2> Part 3 </h2>

{% assign sortedchapters = site.GPIII_chapters | sort:"chapter" %}
{% for entry in sortedchapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      Part 1, {{ entry.title }}
    </a>
  </h3>
  <p style="font-weight: bold; font-size: 20px">
    {% if entry.highlights %}
      {{ entry.highlights }}
  {% endif %}
  </p>
  <p style="text-align:left;"> 
  <a href="{{site.baseurl}}{{page.url}}#top">
      :arrow_up:
  </a>
  <span style="float:right;">
        Arabic: 
        <a href="https://archive.org/details/DelalatolHaerin_201804/page/n{{ entry.pnum }}"><img src="/Guide-Perplexed/assets/internetarchive_icon.svg" height=24em></a>
        |English & Hebrew: 
        <a href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=en"><img src="/Guide-Perplexed/assets/sefaria_icon.svg" height=12em></a>
    </span>
  </p>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
