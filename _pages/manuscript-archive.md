---
title: "Manuscript Archive"
layout: archive
collection: manuscripts
permalink: /manuscript-archive/
entries_layout: grid
---
<h2>Debugging</h2>
<p>Total manuscripts: {{ site.manuscripts | size }}</p>
<ul>
  {% for doc in site.manuscripts %}
    <li>{{ doc.title }} — {{ doc.url }}</li>
  {% endfor %}
</ul>
My grandfather Walter Waczka had a collection of over 300 pieces of sheet music. I scanned and sorted his
collection to produce this comprehensive archive of sheet music.
