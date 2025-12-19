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
  /* Reduced 400px to 280px to ensure it fits on mobile */
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem; /* Slightly tighter gaps for better fit */
}

#articles-grid .grid__item {
  width: 100%;
  max-width: none;
  margin-bottom: 0;
}

#articles-grid .archive__item {
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 1rem;
  background: #f2f2f2;
  box-shadow: 0 2px 5px rgba(0,0,0,0.08); 
  height: 100%; /* Ensures all boxes in a row are the same height */
}

/* Mobile-Specific Adjustments (Screens smaller than 600px) */
@media (max-width: 600px) {
  #articles-grid {
    grid-template-columns: 1fr; /* Force single column */
    gap: 1rem;
    padding: 0 10px; /* Prevents boxes from touching screen edges */
  }

  #articles-grid .archive__item {
    padding: 0.8rem; /* Tighter padding inside the box */
  }

  #articles-grid .archive__item-title {
    font-size: 1.1rem; /* Slightly smaller text for small screens */
  }
}

#articles-grid .archive__item-teaser {
  max-height: none; 
  height: auto;
  overflow: hidden;
  margin: -1rem -1rem 1rem -1rem; /* Negative margin pulls image to the very edges of the gray box */
}

#articles-grid .archive__item-teaser img {
  width: 100%;
  height: auto; 
  display: block;
  border-radius: 10px 10px 0 0; /* Rounds only the top corners to match the box */
  /* Change 'cover' to 'contain' if you want the full image without any cropping, 
     but 'unset' is usually best for a "zoomed-out" natural look */
  object-fit: fill; 
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