---
layout: page
show_meta: false
title: "Mecanique"
subheadline: ""
header:
    image_fullwidth: "banner_talbot.jpg"
permalink: "/mecanique/"
---

<ul>
    {% for post in site.categories.mecanique %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
