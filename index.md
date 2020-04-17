---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Piotr Romanowski | strona domowa
---
<h1 class="page-title">Piotr Romanowski</h1>

## Programowanie / Muzyka / DIY / Inne
 

<div>
  {% for post in site.posts %}
    <section class="post">
      <h2> <a href="{{ post.url }}">{{ post.title }}</a> </h2>
    </section>
  {% endfor %}
</div>