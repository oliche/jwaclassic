---
layout: page
show_meta: false
title: "Technique"
subheadline: ""
header:
    image_fullwidth: "banner_technique.jpg"
permalink: "/technique/"
---

Cette rubrique recense d’une part des conseils recueillis dans de la documentation exclusivement d’époque (toujours intéressante à re-découvrir) et d’autre part le partage d’expériences menées de nos jours.

<ul>
    {% for post in site.categories.technique %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
