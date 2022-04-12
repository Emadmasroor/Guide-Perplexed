---
layout: page
title: Commentary on GP
permalink: /GP
nav: true
---

This is a personal commentary on _Guide for the Perplexed_ (دلالة الحائرين  or מורה נבוכים), the philosophical magnum opus of Moses Maimonides written in the 12th century. It will take the form of chapter summaries with quotations from the original text, using the [English translation](https://oll4.libertyfund.org/title/friedlaender-a-guide-for-the-perplexed){:target="_blank"} of Michael Friedländer. Phrases from the Arabic are taken from the publicly available [transliteration](http://sepehr.mohamadi.name/download/DelalatolHaerin.pdf){:target="_blank"} by Hussein Attai.

{% assign sorted_chapters = site.GP_chapters | sort:"order" %}
{% for entry in sorted_chapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  </h3>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
{:toc}
