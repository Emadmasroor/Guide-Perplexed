---
layout: page
title: Commentary on GP
permalink: /GP
nav: true
---

This is a personal commentary on _Guide for the Perplexed_ (دلالة الحائرين  or דלאלת אלחאירין‎), the philosophical magnum opus of Moses Maimonides written in the 12th century.

' _Guide for the Perplexed_, written in Arabic in the 12th century as دلالة الحائرين 

{% assign sorted_chapters = site.GP_chapters | sort:"order" %}
{% for entry in sorted_chapters %}
  <h2>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  </h2>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
