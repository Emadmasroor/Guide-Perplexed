---
layout: page
title: Resources
permalink: /resources
nav: true
---

This is a test page. List all the resources

{% assign orderedlist = site.Resources | sort:"order" %}
{% for entry in orderedlist %}
  <p>
    <a href="{{site.baseurl}}{{entry.url}}">
      {{ entry.title }}
    </a>
  </p>
{% endfor %}
