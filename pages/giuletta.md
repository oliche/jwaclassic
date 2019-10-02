---
layout: page
show_meta: false
title: "Alfa Romeo Giuletta 1962"
subheadline: ""
header:
    image_fullwidth: "banner_aston.png"
permalink: "/alfa_romeo_giuletta/"
lang: eng
---

Combien d’entre-nous buttent sur des difficultés à reconstituer un historique complet de leur véhicule ou possède un voiture dont l’histoire mérite d’être contée ? Cette rubrique constitue une sorte de bouteille à la mer pour le recueil d’informations qui viendront – peut-être – compléter un joli récit.


<ul>
    {% for post in site.categories.historique %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
