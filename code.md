---
title: Programowanie
permalink: /code/
---
<h1 class="page-title"> Programowanie</h1>

<div>
  {% for post in site.categories.code %}
    <section class="post">
      <h2> <a href="{{ post.url }}">{{ post.title }}</a> </h2>
    </section>
  {% endfor %}
</div>