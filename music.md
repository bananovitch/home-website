---
layout: default
title: music
permalink: /music/
---

<h1 class="page-title"> Muzyka</h1>

Muzyczka którą nagrałem. Na razie skromnie.

<div class="video-wrapper">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/PDgQ9s_nxuE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div>
  {% for post in site.categories.music %}
        {% include post.html %}

{% endfor %}

</div>
