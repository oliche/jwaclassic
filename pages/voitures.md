---
layout: page
show_meta: false
title: "Voitures"
subheadline: ""
header:
    image_fullwidth: "banner_delahaye.png"
permalink: "/voitures/"
---

<ul>
    {% for post in site.categories.voitures %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
