---
permalink: /blog/
title: Blog
---
<h1 class="page-title">Blog</h1>
<div>
  {% for post in site.categories.blog %}
    <section class="post">
      <h2> <a href="{{ post.url }}">{{ post.title }}</a> </h2>
    </section>
  {% endfor %}
</div>
