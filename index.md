---
layout: default
title: "Dokimon: Quest - Wiki"
---
{% include type_chart_ui.html %}

<button id="filter-toggle">Toggle Filters</button>

<div class="filter-controls">
  <!-- Group: Stage -->
  <div class="filter-block">
<label for="formFilter">Palettes:</label>
<select id="formFilter" style="margin-right: 1rem;">
  <option value="common">Common</option>
  <option value="2">Rare Form 1</option>
  <option value="3">Rare Form 2</option>
  <option value="4">Rare Form 3</option>
  <option value="5">Rare Form 4</option>
  <option value="6">Rare Form 5</option>
  <option value="7">Rare Form 6</option>
  <option value="8">Rare Form 7</option>
  <option value="9">Bound</option>
  <option value="10">Unique</option>
</select>
</div>

  <!-- Vertical Separator -->
  <div class="separator"></div>

  <div class="filter-block">
  
    <label for="stage-filter">Stage:</label>
    <select id="stage-filter">
      <option value="">All</option>
      <option value="1">Stage 1</option>
      <option value="2">Stage 2</option>
      <option value="3">Stage 3</option>
	  <option value="4">Stage 4</option>
	  <option value="5">Stage 5</option>
	  <option value="6">Stage 6</option>
    </select>
  </div>

  <!-- Group: Type -->
  <div class="filter-block type-block">
    <label>Type:</label>
    <div id="type-filters">
      <button class="type-btn type-fire" data-type="Fire">Fire</button>
      <button class="type-btn type-water" data-type="Water">Water</button>
      <button class="type-btn type-grass" data-type="Grass">Grass</button>
      <button class="type-btn type-electric" data-type="Electric">Electric</button>
      <button class="type-btn type-light" data-type="Light">Light</button>
      <button class="type-btn type-dark" data-type="Dark">Dark</button>
      <button class="type-btn type-flying" data-type="Flying">Flying</button>
      <button class="type-btn type-fight" data-type="Fight">Fight</button>
      <button class="type-btn type-fairy" data-type="Fairy">Fairy</button>
      <button class="type-btn type-ghost" data-type="Ghost">Ghost</button>
      <button class="type-btn type-poison" data-type="Poison">Poison</button>
      <button class="type-btn type-dragon" data-type="Dragon">Dragon</button>
      <button class="type-btn type-ice" data-type="Ice">Ice</button>
    </div>
  </div>

  <!-- Group: Location -->
  <div class="filter-block">
    <label for="location-filter">Location:</label>
    <input type="text" id="location-filter" placeholder="Search Location">
  </div>

  <!-- Group: Name -->
  <div class="filter-block">
    <label for="search-filter">Name:</label>
    <input type="text" id="search-filter" placeholder="Search Name">
  </div>

  <!-- Group: Clear Button -->
  <div class="filter-block">
    <button id="clear-filters" class="clear-btn">Clear Filters</button>
  </div>
</div>

<div class="dex-grid" id="dex-grid">
  {% if site.dokimon %}
    {% assign sorted = site.dokimon | sort: "number" %}
    {% for mon in sorted %}
{% assign raw_type = mon.type | default: '' %}
{% assign type_array = raw_type | downcase | split: ',' | map: 'strip' %}
{% assign type1 = type_array[0] %}
{% assign type2 = type_array[1] %}
{% assign type_class = '' %}

{% if type1 != blank and type2 != blank and type2 != 'nan' %}
  {% assign types_sorted = type_array | sort %}
  {% assign type_class = 'border-' | append: types_sorted[0] | append: '-' | append: types_sorted[1] %}
{% elsif type1 != blank and type1 != 'nan' %}
  {% assign type_class = 'border-' | append: type1 %}
{% endif %}

      <article class="dex-entry"
           data-name="{{ mon.name | downcase | default: '' }}"
		   data-number="{{ mon.number | default: '' }}"
           data-location="{{ mon.location | downcase | default: '' }}"
           data-stage="{{ mon.stage | default: '' }}"
           data-type="{% if mon.type %}{{ mon.type | default: '' | join: ' ' }}{% else %}none{% endif %}">
        <a href="{{ mon.url }}">
          <div class="img-wrapper {{ type_class }}">
            <img src="{{ mon.image }}" alt="{{ mon.name }}" class="monster-image small" data-default="{{ mon.image }}">
            <div class="img-blocker"></div>
          </div>
          <div class="dex-card-details"><span class="dex-card-number">#{{ mon.number }}</span><strong class="dex-card-name">{{ mon.name }}</strong></div>
        </a>
      </article>
    {% endfor %}
  {% else %}
    <p style="color: red;">⚠ No Dokimon collection found. Check `_config.yml` and `_dokimon/` folder.</p>
  {% endif %}
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

document.getElementById("formFilter").addEventListener("change", function () {
  const selectedForm = this.value;

  document.querySelectorAll(".dex-entry").forEach(entry => {
    const name = entry.dataset.name;
	const number = entry.dataset.number;
    const img = entry.querySelector("img.monster-image");

    if (!img || !name) return;
	
	const folderName = `${number}_${name}`;

    if (selectedForm === "common") {
      img.src = img.dataset.default;
    } else {
      img.src = `/assets/images/forms/${folderName}/${name}_${selectedForm}.png`;
    }
  });
});

</script>
