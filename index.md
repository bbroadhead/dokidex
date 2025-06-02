---
layout: default
title: Dokimon: Quest - Wiki
---

<button id="filter-toggle">Toggle Filters</button>
<div class="filter-controls">
  <label for="stage-filter">Stage:</label>
  <select id="stage-filter">
    <option value="">All</option>
    <option value="1">Stage 1</option>
    <option value="2">Stage 2</option>
    <option value="3">Stage 3</option>
  </select>

  <label>Type:</label>
  <div id="type-filters">
    <button class="type-btn" data-type="Fire">Fire</button>
    <button class="type-btn" data-type="Water">Water</button>
    <button class="type-btn" data-type="Grass">Grass</button>
    <button class="type-btn" data-type="Electric">Electric</button>
    <button class="type-btn" data-type="Light">Light</button>
    <button class="type-btn" data-type="Dark">Dark</button>
    <button class="type-btn" data-type="Flying">Flying</button>
    <button class="type-btn" data-type="Fight">Fight</button>
  </div>

  <label for="location-filter">Location:</label>
  <input type="text" id="location-filter" placeholder="Search Location">

  <label for="search-filter">Name:</label>
  <input type="text" id="search-filter" placeholder="Search Name">

  <button id="clear-filters" class="clear-btn">Clear Filters</button>
</div>

<div class="dex-grid" id="dex-grid">
  {% assign sorted = site.pages | where: "layout", "dex_entry" | sort: "number" %}
  {% for mon in sorted %}
    <div class="dex-entry"
         data-name="{{ mon.name | downcase }}"
         data-location="{{ mon.location | downcase }}"
         data-stage="{{ mon.stage }}"
         data-type="{{ mon.type | join: ' ' }}">
      <a href="{{ mon.url }}">
        <div class="img-wrapper">
          <img src="{{ mon.image | relative_url }}" alt="{{ mon.name }}">
          <div class="img-blocker"></div>
        </div>
        <div>#{{ mon.number }} - {{ mon.name }}</div>
      </a>
    </div>
  {% endfor %}
</div>

<script>
const typeButtons = document.querySelectorAll('.type-btn');
const stageFilter = document.getElementById('stage-filter');
const locationFilter = document.getElementById('location-filter');
const searchFilter = document.getElementById('search-filter');
const clearBtn = document.getElementById('clear-filters');
const entries = document.querySelectorAll('.dex-entry');
const filterToggle = document.getElementById('filter-toggle');
const filterControls = document.querySelector('.filter-controls');

let activeTypes = new Set();

typeButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const type = btn.dataset.type;
    if (activeTypes.has(type)) {
      activeTypes.delete(type);
      btn.classList.remove('active');
    } else {
      activeTypes.add(type);
      btn.classList.add('active');
    }
    filterDex();
  });
});

[stageFilter, locationFilter, searchFilter].forEach(input =>
  input.addEventListener('input', filterDex)
);

clearBtn.addEventListener('click', () => {
  activeTypes.clear();
  typeButtons.forEach(btn => btn.classList.remove('active'));
  stageFilter.value = '';
  locationFilter.value = '';
  searchFilter.value = '';
  filterDex();
});

function filterDex() {
  const stage = stageFilter.value;
  const loc = locationFilter.value.toLowerCase();
  const search = searchFilter.value.toLowerCase();

  entries.forEach(entry => {
    const matchType = [...activeTypes].every(type =>
      entry.dataset.type.includes(type)
    );
    const matchStage = !stage || entry.dataset.stage === stage;
    const matchLoc = entry.dataset.location.includes(loc);
    const matchSearch = entry.dataset.name.includes(search);
    entry.style.display = (matchType && matchStage && matchLoc && matchSearch) ? '' : 'none';
  });
}

filterToggle.addEventListener('click', () => {
  filterControls.classList.toggle('collapsed');
});
</script>
