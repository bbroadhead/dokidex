---
layout: default
title: Dokimon Dex
---

# Dokimon Dex

<ul class="dex-grid">
  {% assign sorted_dex = site.dokimon | sort: "number" %}
  {% for mon in sorted_dex %}
    <li>
      <a href="{{ mon.url }}">
        <img src="{{ mon.image }}" alt="{{ mon.name }}"><br>
        #{{ mon.number }} - {{ mon.name }}
      </a>
    </li>
  {% endfor %}
</ul>
