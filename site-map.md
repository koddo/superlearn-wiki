---
layout: page
title:  Site map

---

{% for my_collection in site.collections %}
{% if my_collection.label != 'posts' %}
collection: <a href="{{ site.baseurl }}/{{ my_collection.label }}">{{ my_collection.title }}</a>
{% for my_page in my_collection.docs %}
{% if my_page.title != 'Index' %}
<a class="page-link" href="{{ my_page.url | prepend: site.baseurl }}">{{ my_page.title }}</a>
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
  
