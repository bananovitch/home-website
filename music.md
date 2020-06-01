---
layout: default
title: music
permalink: /music/
---

<h1 class="page-title"> Muzyka</h1>

Muzyka i wszelkie okołomuzyczne rzeczy które tworzę. Najbardziej interesuje mnie muzyka elektroniczna we wszelkich odmianach: ambient, techno, eksperymenty. Tutaj też znajdują zastosowanie wszelkiej maści elektroniczne ustrojstwa które zbudowałem. W rezultacie powstaje coś, co mozna określić mianem _lo-fi_.

<div>
  {% for post in site.categories.music %}
        {% include post.html %}

{% endfor %}

</div>
