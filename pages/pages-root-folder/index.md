---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: banner_delahaye.png
widget1:
  title: "Voitures"
  url: '/voitures/'
  image: home_delage.jpg
  text: 'Voitures'
widget2:
  title: "Historique"
  image: home_delahaye.jpg
  url: '/historique/'
  text: 'Historique'
widget3:
  title: "Mecanique"
  url: '/mecanique/'
  image: home_talbot.jpg
  text: 'Talbot.'
permalink: /index.html
homepage: true
---

<div id="videoModal" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/U0hT9vO_oHA" frameborder="0" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>
