---
permalink: /blog/
title: Blog
---

<h1 class="page-title">Blog</h1>
<div>
  {% for post in site.categories.blog %}
        {% include post.html %}

{% endfor %}

</div>
