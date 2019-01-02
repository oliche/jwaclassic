---
layout: page
show_meta: false
title: "Technique"
subheadline: ""
header:
    image_fullwidth: "banner_talbot.png"
permalink: "/technique/"
---

Cette rubrique recense d’une part des conseils recueillis dans de la documentation exclusivement d’époque (toujours intéressante à re-découvrir) et d’autre part le partage d’expérience menée à notre époque.

<ul>
    {% for post in site.categories.technique %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
