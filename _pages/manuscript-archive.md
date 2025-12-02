---
title: "Manuscript Archive"
layout: archive
collection: manuscripts
permalink: /manuscript-archive/
entries_layout: grid
author_profile: true
header:
  image: /assets/images/headers/radio-and-conc.jpg
  overlay_filter: 0.3
  image_description: "The Chemnitzer instrument on a mantle next to a vintage radio"
---
My grandfather Walter Waczka had a collection of over 300 pieces of sheet music. I scanned and sorted his
collection to produce this comprehensive archive of sheet music.

<input
  id="manuscript-search"
  type="text"
  placeholder="Search manuscripts…"
  style="width:100%; padding:0.6em; font-size:1.1em; margin-bottom:1.2em;"
>

<div class="grid__wrapper" id="manuscript-grid">
  {% for post in site.manuscripts %}
    <div class="manuscript-item"
      data-title="{{ post.title | escape }}"
      data-number="{{ post.number | escape }}"
      data-key="{{ post.key | escape }}"
      data-meter="{{ post.meter | escape }}"
      data-type="{{ post.piece_type | escape }}"
      data-notes="{{ post.notes | escape }}"
      data-content="{{ post.content | strip_html | escape }}"
    >
      {% include archive-single.html type="grid" %}
    </div>
  {% endfor %}
</div>

<script>
document.getElementById("manuscript-search").addEventListener("input", function () {
    const query = this.value.toLowerCase();
    const items = document.querySelectorAll(".manuscript-item");

    items.forEach(item => {
        const haystack =
            (item.dataset.title + " " +
             item.dataset.number + " " +
             item.dataset.key + " " +
             item.dataset.meter + " " +
             item.dataset.type + " " +
             item.dataset.notes + " " +
             item.dataset.content
            ).toLowerCase();

        if (haystack.includes(query)) {
            item.style.display = "";
        } else {
            item.style.display = "none";
        }
    });
});
</script>