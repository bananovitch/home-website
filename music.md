---
layout: default
title: music
permalink: /music/
---

# Music

<div>
  {% for post in site.categories.music %}
    <section class="post">
      <h2> <a href="{{ post.url }}">{{ post.title }}</a> </h2>
    </section>
  {% endfor %}
</div>