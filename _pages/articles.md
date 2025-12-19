---
title: "Articles"
layout: archive
permalink: /articles/
collection: articles
author_profile: true
header:
  overlay_image: /assets/images/headers/pateks-club.jpg
  overlay_filter: "0.3"
  image_description: "Group of well-dressed musicians with concertinas and other polka instruments"
---

<div id="articles-grid" class="grid__wrapper">
  {% for post in site.articles %}
    <div class="grid__item"> 
      {% include archive-single.html type="grid" %}
    </div>
  {% endfor %}
</div>

<style>
/* Base Grid (Desktop/Tablet) */
#articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(450px, 1fr)); 
  gap: 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

#articles-grid .grid__item {
  width: 100%;
  display: flex; /* Ensures the inner .archive__item stretches to full height */
}

#articles-grid .archive__item {
  display: flex;
  flex-direction: column;
  width: 100%;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 1rem;
  background: #f2f2f2;
  box-shadow: 0 2px 5px rgba(0,0,0,0.08); 
}

#articles-grid .archive__item-teaser {
  margin: -1rem -1rem 1rem -1rem; /* Edge-to-edge image */
  max-height: none !important;
  height: auto !important;
  overflow: hidden;
}

#articles-grid .archive__item-teaser img {
  width: 100%;
  height: 400px;
  object-fit: cover; 
  object-position: center 20%; 
  display: block;
  border-radius: 10px 10px 0 0;
}

#articles-grid .archive__item-title {
  font-size: 1.2rem;
  margin-top: 0.5em;
  line-height: 1.3;
}

#articles-grid .archive__item-excerpt {
  font-size: 0.8rem;
  margin-top: 0.5rem;
  flex-grow: 1; /* Pushes the bottom of the card down if text is short */
}

/* Mobile-Specific Adjustments */
@media (max-width: 600px) {
  #articles-grid {
    grid-template-columns: 1fr;
    gap: 0.5rem;
    padding: 0 10px;
  }

  #articles-grid .archive__item-teaser img {
    height: 200px !important;
  }
}
</style>