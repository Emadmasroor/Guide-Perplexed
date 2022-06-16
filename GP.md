---
layout: page
title: Chapter Summaries
permalink: /summaries
nav: true
---

This is a personal commentary on _Guide for the Perplexed_ (_dalalat al-haa'ireen_ دلالة الحائرين  or _moreh nebuchim_ מורה נבוכים), the philosophical magnum opus of Moses Maimonides written in the 12th century. It will take the form of chapter summaries with quotations from the original text, using the [English translation](https://www.sefaria.org/Guide_for_the_Perplexed){:target="_blank"} of Michael Friedländer. Phrases from the Arabic are taken from the publicly available [transliteration](http://sepehr.mohamadi.name/download/DelalatolHaerin.pdf){:target="_blank"} by Hussein Attai.

<h2> Part I </h2>

{% assign sorted_chapters = site.GPI_chapters | sort:"chapter" %}
{% for entry in sorted_chapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
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
