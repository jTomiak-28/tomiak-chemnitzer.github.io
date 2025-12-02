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

<style>
/* This custom class ensures items are hidden without breaking the grid */
.manuscript-item.is-hidden {
  display: none;
}
</style>

<div class="grid__wrapper" id="manuscript-grid">
  {% for post in site.manuscripts %}
    <div class="manuscript-item grid__item"
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
document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("manuscript-search");
    const items = document.querySelectorAll(".manuscript-item");

    searchInput.addEventListener("input", function () {
        const query = this.value.toLowerCase().trim();

        items.forEach(item => {
            // Include all your data attributes in the search
            const haystack =
                (item.dataset.title + " " +
                 item.dataset.number + " " +
                 item.dataset.key + " " +
                 item.dataset.meter + " " +
                 item.dataset.type + " " +
                 item.dataset.notes + " " +
                 item.dataset.content
                ).toLowerCase();

            // Toggle the visibility class
            if (haystack.includes(query)) {
                item.classList.remove("is-hidden");
            } else {
                item.classList.add("is-hidden");
            }
        });
    });
});
</script>