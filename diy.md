---
layout: default
title: DIY
permalink: /diy/
---

# DIY projects

<div>
  {% for post in site.categories.diy %}
    <section class="post">
      <h2> <a href="{{ post.url }}">{{ post.title }}</a> </h2>
    </section>
  {% endfor %}
</div>