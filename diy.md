---
layout: default
title: DIY
permalink: /diy/
---

<h1 class="page-title"> DIY</h1>

Wszelkiej maści sprzęty i urządzenia które zbudowałem.

<div>
  {% for post in site.categories.diy %}
        {% include post.html %}

{% endfor %}

</div>
