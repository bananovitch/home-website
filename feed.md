---
permalink: /feed/
title: Newsfeed
---

<h1 class="page-title">Newsfeed</h1>
<div>
  {% for post in site.categories.feed %}
        {% include newsfeed-post.html %}

{% endfor %}

</div>
