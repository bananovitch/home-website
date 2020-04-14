---
layout: default
title: music
permalink: /music/
---

# Music

<ul>
  {% for post in site.categories.music %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>