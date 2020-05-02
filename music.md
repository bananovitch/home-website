---
layout: default
title: music
permalink: /music/
---

<h1 class="page-title"> Muzyka</h1>

Muzyczka którą nagrałem.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PDgQ9s_nxuE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div>
  {% for post in site.categories.music %}
    <section class="post">
      <h2> <a href="{{ post.url }}">{{ post.title }}</a> </h2>
    </section>
  {% endfor %}
</div>
