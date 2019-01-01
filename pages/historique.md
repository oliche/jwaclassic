---
layout: page
show_meta: false
title: "Historique"
subheadline: ""
header:
    image_fullwidth: "banner_talbot.png"
permalink: "/historique/"
---

<ul>
    {% for post in site.categories.historique %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
