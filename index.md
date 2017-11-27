---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
---

[site-map]({{ site.baseurl }}{% link site-map.md %})

{% for my_collection in site.collections %}
{% if my_collection.label != 'posts' %}
collection: <a href="{{ site.baseurl }}/{{ my_collection.label }}">{{ my_collection.title }}</a>
{% for my_page in my_collection.docs %}
{% if my_page.title != 'Index' %}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a class="page-link" href="{{ my_page.url | prepend: site.baseurl }}">{{ my_page.title }}</a>
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}


