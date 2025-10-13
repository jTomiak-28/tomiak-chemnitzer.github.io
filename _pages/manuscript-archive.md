---
title: "Manuscript Archive"
layout: archive
collection: manuscripts
permalink: /manuscript-archive/
entries_layout: grid
author_profile: true
header:
  image: /assets/images/lily/jtom-33.jpg
  overlay_filter: 0.3
  image_description: "The Chemnitzer instrument on a mantle next to a vintage radio"

---
My grandfather Walter Waczka had a collection of over 300 pieces of sheet music. I scanned and sorted his
collection to produce this comprehensive archive of sheet music.

<div class="grid__wrapper">
  {% for post in site.manuscripts %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>