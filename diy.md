---
layout: default
title: DIY
permalink: /diy/
---

# DIY projects

<ul>
  {% for post in site.categories.diy %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>