---
layout: page
show_meta: false
title: "Véhicules"
subheadline: ""
header:
    image_fullwidth: "Banner-Mosaic.jpg"
permalink: "/voitures/"
lang: fr
---

Un petite visite dans une galerie virtuelle de véhicules à vendre ou pas, avant tout pour le plaisir des yeux.

<ul>
    {% for post in site.categories.voitures %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
