---
layout: page
show_meta: false
title: "Documentation"
subheadline: ""
header:
    image_fullwidth: "Banner_Presse.jpg"
permalink: "/documentation/"
---

Vous trouverez ici une reproduction des informations recueillies dans la lecture de la presse contemporaine à nos belles anciennes. Vous y trouverez aussi des brochures d’époque.
<ul>
    {% for post in site.categories.presse %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
