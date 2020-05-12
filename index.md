---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Piotr Romanowski | strona domowa
description: Strona domowa na którą wrzucam swoją muzykę, zrób-to-samy i okołoprogramistyczne teksty
---

<h1 class="page-title">Piotr Romanowski</h1>

## Programowanie / Muzyka / DIY / Inne

<div>
  {% for post in site.posts %}
    {% include post.html %}
  {% endfor %}
</div>
