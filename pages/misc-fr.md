---
layout: page
show_meta: false
title: "Blog & Portfolio"
subheadline: ""
header:
    image_fullwidth: "banner_talbot.png"
permalink: "/misc/"
lang: fr
---

Ici, c’est un peu le fourre-tout ou l’on parle essentiellement des sujets d’actualité.

<ul>
    {% for post in site.categories.misc %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
