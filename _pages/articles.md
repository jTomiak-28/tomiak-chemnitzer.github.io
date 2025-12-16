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
#articles-grid .grid__item {
  width: 100%;
  max-width: none;
  margin-bottom: 0;
}

#articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 2.5rem;
}

#articles-grid .archive__item {
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 1rem;
  background: #f2f2f2;
  box-shadow: 0 2px 5px rgba(0,0,0,0.08); 
}

#articles-grid .archive__item-teaser {
  max-height: none; 
  height: auto;
  overflow: visible;
}

#articles-grid .archive__item-teaser img {
  width: 100%;
  height: auto; 
  display: block;
  border-radius: 4px;
  object-fit: cover; /* Ensures the image covers the area nicely without squishing */
}

#articles-grid .archive__item-title {
  font-size: 1.2rem;
  margin-top: 0.5em;
  line-height: 1.3;
}

#articles-grid .archive__item-excerpt {
  font-size: 0.8rem;
  margin-top: 0.5rem;
}
</style>