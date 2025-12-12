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


<!-- Search bar for manuscripts -->
<div style="margin-bottom: 1.5em;">
  <input
    id="manuscript-search"
    type="text"
    placeholder="Search manuscripts…"
    style="width: 100%; padding: 0.6em; font-size: 1.0em; border: 1px solid #ccc; border-radius: 4px;"
  />
</div>


<div class="grid__wrapper" id="manuscript-grid">
  {% for post in site.manuscripts %}
    <div class="grid__item manu-item"
      data-id="{{ post.id | default: '' | escape }}"
      data-title="{{ post.title | default: '' | escape }}"
      data-translation="{{ post.translation | default: '' | escape }}"
      data-number="{{ post.number | default: '' | escape }}"
      data-key="{{ post.key | default: '' | escape }}"
      data-meter="{{ post.meter | default: '' | escape }}"
      data-piece_type="{{ post.piece_type | default: '' | escape }}"
      data-appears_in="{{ post.appears_in | default: '' | escape }}"
      data-composer="{{ post.composer | default: '' | escape }}"
      data-arranger="{{ post.arranger | default: '' | escape }}"
      data-publisher="{{ post.publisher | default: '' | escape }}"
      data-publication_place="{{ post.publication_place | default: '' | escape }}"
      data-copyright_holder="{{ post.copyright_holder | default: '' | escape }}"
      data-copyright_year="{{ post.copyright_year | default: '' | escape }}"
      data-medium="{{ post.medium | default: '' | escape }}"
      data-file_name="{{ post.file_name | default: '' | escape }}"
      data-notes="{{ post.notes | default: '' | escape }}"
      data-audio_recording="{{ post.audio_recording | default: '' | escape }}"
      data-excerpt="{{ post.excerpt | default: '' | strip_html | escape }}"
    >
      {% include archive-single.html type="grid" %}
    </div>
  {% endfor %}
</div>


<script>
document.getElementById("manuscript-search").addEventListener("input", function () {
    const query = this.value.toLowerCase();
    const items = document.querySelectorAll(".manu-item");

    items.forEach(item => {
        const haystack = (
            (item.dataset.id || "") + " " +
            (item.dataset.title || "") + " " +
            (item.dataset.translation || "") + " " +
            (item.dataset.number || "") + " " +
            (item.dataset.key || "") + " " +
            (item.dataset.meter || "") + " " +
            (item.dataset.piece_type || "") + " " +
            (item.dataset.appears_in || "") + " " +
            (item.dataset.composer || "") + " " +
            (item.dataset.arranger || "") + " " +
            (item.dataset.publisher || "") + " " +
            (item.dataset.publication_place || "") + " " +
            (item.dataset.copyright_holder || "") + " " +
            (item.dataset.copyright_year || "") + " " +
            (item.dataset.medium || "") + " " +
            (item.dataset.file_name || "") + " " +
            (item.dataset.notes || "") + " " +
            (item.dataset.audio_recording || "") + " " +
            (item.dataset.excerpt || "")
        ).toLowerCase();

        item.style.display = haystack.includes(query) ? "" : "none";
    });
});
</script>

<style>
#manuscript-grid .grid__item {
  width: 100%;
  max-width: none;
  margin-bottom: 1rem;
}

#manuscript-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  column-gap: 1.5rem;
}

#manuscript-grid .archive__item {
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 0.8rem;
  background: #f2f2f2;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

#manuscript-grid .archive__item-teaser img {
  width: 100%;
  height: auto;
  display: block;
}

#manuscript-grid .archive__item-title {
  font-size: 1.1rem;
  line-height: 1.3;
  white-space: normal;
}
</style>
