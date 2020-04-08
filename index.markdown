---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Piotr Romanowski | strona domowa
---
# Piotr Romanowski

Programowanie / Muzyka / DIY / Inne

Cześć! Nazywam się Piotr Romanowski, a to jest moja strona domowa. 

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>