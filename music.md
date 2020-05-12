---
layout: default
title: music
permalink: /music/
---

<h1 class="page-title"> Muzyka</h1>

Muzyczka którą nagrałem. Na razie skromnie.

{% include video.html url="https://www.youtube.com/embed/PDgQ9s_nxuE" %}

<div>
  {% for post in site.categories.music %}
        {% include post.html %}

{% endfor %}

</div>
