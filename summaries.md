---
layout: page
title: Chapter Summaries
permalink: /summaries
nav: true
---

<h2> Part 1 </h2>

{% assign sorted_chapters = site.GPI_chapters | sort:"chapter" %}
{% for entry in sorted_chapters %}
<div class="chapter-wrapper">
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      Part 1, {{ entry.title }}
    </a>
  </h3>
  
  {% if entry.highlights %}
  <p style="font-size: 20px">{{ entry.highlights }}</p>
  {% endif %}

  <p style="text-align:left;"> 
    <a href="{{site.baseurl}}{{page.url}}#top"> :arrow_up: </a>
  </p>

  <p style="text-align:right; font-size:11px">
    <a target="_blank" rel="noopener noreferrer" href="https://archive.org/details/DelalatolHaerin_201804/page/n{{ entry.pnum }}">Arabic (Huseyin Attai, 1962)</a> | 
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=en">English (Michael Friedländer, 1885)</a> |
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=bi">Hebrew (Ibn Tibbon, 1204)</a> | 
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?vhe=Judeo_Arabic,_Paris,_1856_(ar)&lang=bi">Arabic (Munk, 1856)</a>
  </p>

  <div class="chapter-summary-text">
    {{ entry.content | markdownify }}
  </div>

  <div class="translations-section">
    <h4 class="translations-heading">Translations</h4>

    {% assign part_key = "part" | append: entry.part %}
    {% assign ch_key = "ch" | append: entry.chapter %}
    {% assign trans_data = site.data.translations[part_key][ch_key] %}

    {% if trans_data %}
      <div class="tabs-container">
        <div class="tab-nav">
          {% for translation in trans_data %}
            {% assign t_name = translation[0] %}
            <button class="tab-button {% if forloop.first %}active{% endif %}" 
                    onclick="openTab(event, '{{ t_name }}-p{{ entry.part }}c{{ entry.chapter }}')">
              {{ t_name | replace: "tibbon", "Ibn Tibbon" | capitalize }}
            </button>
          {% endfor %}
        </div>

        {% for translation in trans_data %}
          {% assign t_name = translation[0] %}
          {% assign t_content = translation[1] %}
          <div id="{{ t_name }}-p{{ entry.part }}c{{ entry.chapter }}" class="tab-panel {% if forloop.first %}active{% endif %}" markdown="1">

{{ t_content }}

          </div>
        {% endfor %}
      </div>
    {% else %}
      <p style="font-style: italic; color: #888; font-size: 11px;">Translation pending for Part {{ entry.part }} Ch {{ entry.chapter }}</p>
    {% endif %}
</div> <p style="font-size: 10px;text-align:right">
      <a href="https://github.com/Emadmasroor/Guide-Perplexed/blob/main/{{ entry.path }}">Edit on GitHub</a>
  </p>
  <hr>
</div> {% endfor %}

<h2> Part 2 </h2>

{% assign sortedchapters = site.GPII_chapters | sort:"chapter" %}
{% for entry in sortedchapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      Part 2, {{ entry.title }}
    </a>
  </h3>
  <p style="font-size: 20px">
    {% if entry.highlights %}
      {{ entry.highlights }}
  {% endif %}
  </p>
  <p style="text-align:left;"> 
  <a href="{{site.baseurl}}{{page.url}}#top">
      :arrow_up:
  </a>
  </p>
  <p style="text-align:right; font-size:11px">
    <a target="_blank" rel="noopener noreferrer" href="https://archive.org/details/DelalatolHaerin_201804/page/n{{ entry.pnum }}">Arabic (Huseyin Attai, 1962)</a> | 
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=en">English (Michael Friedländer, 1885)</a> |
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=bi">Hebrew (Ibn Tibbon, 1204)</a> | 
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?vhe=Judeo_Arabic,_Paris,_1856_(ar)&lang=bi">Arabic (Munk, 1856)</a>
  </p>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}

<h2> Part 3 </h2>

{% assign sortedchapters = site.GPIII_chapters | sort:"chapter" %}
{% for entry in sortedchapters %}
  <h3>
    <a href="{{site.baseurl}}{{entry.url}}">
      Part 3, {{ entry.title }}
    </a>
  </h3>
  <p style="font-size: 20px">
    {% if entry.highlights %}
      {{ entry.highlights }}
  {% endif %}
  </p>
  <p style="text-align:left;"> 
  <a href="{{site.baseurl}}{{page.url}}#top">
      :arrow_up:
  </a>
  </p>
  <p style="text-align:right; font-size:11px">
    <a target="_blank" rel="noopener noreferrer" href="https://archive.org/details/DelalatolHaerin_201804/page/n{{ entry.pnum }}">Arabic (Huseyin Attai, 1962)</a> | 
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=en">English (Michael Friedländer, 1885)</a> |
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?lang=bi">Hebrew (Ibn Tibbon, 1204)</a> | 
    <a target="_blank" rel="noopener noreferrer" href="https://www.sefaria.org/Guide_for_the_Perplexed%2C_Part_{{ entry.part }}.{{ entry.chapter }}?vhe=Judeo_Arabic,_Paris,_1856_(ar)&lang=bi">Arabic (Munk, 1856)</a>
  </p>
  <p>{{ entry.content | markdownify }}</p>
{% endfor %}
