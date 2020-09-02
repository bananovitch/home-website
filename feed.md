---
permalink: /feed/
title: Newsfeed
---

<h1 class="page-title">Newsfeed</h1>
<div>
  {% for post in site.categories.feed %}
        {% include post.html %}

{% endfor %}

</div>
