---
permalink: /blog/
title: Blog
---

<div>
  {% for post in site.categories.blog %}
    <section class="post">
      <h2> <a href="{{ post.url }}">{{ post.title }}</a> </h2>
    </section>
  {% endfor %}
</div>
