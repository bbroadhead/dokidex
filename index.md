---
layout: default
title: "Dokimon: Quest - Wiki"
---
{% include type_chart_ui.html %}

<style id="yanoverse-filter-collapse-fix">
#dex-filter-controls.collapsed,
body.dark-mode #dex-filter-controls.collapsed { display: none !important; }
#filter-toggle {display:flex!important;align-items:center!important;justify-content:center!important;width:fit-content!important;max-width:calc(100% - 24px)!important;min-height:42px!important;margin:4px auto 18px!important;padding:10px 22px!important;border:1px solid rgba(152,191,237,.36)!important;border-radius:12px!important;background:linear-gradient(145deg,#243c5b,#14273e)!important;color:#edf5ff!important;font:700 13px/1.3 system-ui,sans-serif!important;letter-spacing:.025em!important;box-shadow:0 6px 20px rgba(0,0,0,.2)!important;cursor:pointer!important;transition:background .2s,transform .2s!important;}
#filter-toggle:hover,#filter-toggle:focus-visible {background:linear-gradient(145deg,#355779,#1d3653)!important;}
#filter-toggle:active {transform:scale(.98)!important;}

/* Centered glass-style type chips, with compact search and clear controls. */
#dex-filter-controls .type-block {flex:1 1 100%!important;text-align:center!important}
#dex-filter-controls .type-block>label {text-align:center!important;margin-bottom:10px!important}
#dex-filter-controls #type-filters {
  display:flex!important;flex-wrap:wrap!important;justify-content:center!important;
  align-items:center!important;gap:9px!important;width:100%!important;
}
#dex-filter-controls #type-filters .type-btn {
  position:relative!important;overflow:hidden!important;
  min-height:37px!important;padding:9px 14px!important;
  border:1px solid rgba(220,237,255,.34)!important;border-radius:11px!important;
  background-image:linear-gradient(160deg,rgba(255,255,255,.29),rgba(255,255,255,.08) 46%,rgba(5,17,32,.2))!important;
  background-blend-mode:screen!important;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.32),0 4px 12px rgba(0,0,0,.19)!important;
  color:#fff!important;font:700 12px/1.2 system-ui,sans-serif!important;
  text-shadow:0 1px 3px rgba(0,0,0,.65)!important;
  backdrop-filter:blur(10px) saturate(145%)!important;
  -webkit-backdrop-filter:blur(10px) saturate(145%)!important;
  transition:transform .16s,box-shadow .16s,filter .16s!important;
}
#dex-filter-controls #type-filters .type-btn {
  box-sizing:border-box!important;
  flex:0 0 92px!important;
  width:92px!important;
  min-width:92px!important;
  max-width:92px!important;
  height:38px!important;
  min-height:38px!important;
  max-height:38px!important;
  display:inline-flex!important;
  align-items:center!important;
  justify-content:center!important;
  padding:6px 8px!important;
  white-space:nowrap!important;
}
#dex-filter-controls #type-filters .type-btn:hover {
  transform:translateY(-2px)!important;filter:brightness(1.13)!important;
}
#dex-filter-controls #type-filters .type-btn.active {
  border-color:rgba(255,255,255,.9)!important;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 0 0 2px rgba(145,206,255,.55),0 5px 18px rgba(40,117,199,.34)!important;
  filter:brightness(1.2)!important;
}
#dex-filter-controls {
  row-gap:8px!important;column-gap:12px!important;align-items:end!important;
}
#dex-filter-controls .filter-block:has(#location-filter),
#dex-filter-controls .filter-block:has(#search-filter) {margin-bottom:0!important;padding-bottom:0!important}
#dex-filter-controls .filter-block:has(#clear-filters) {
  flex:1 1 100%!important;display:flex!important;justify-content:center!important;
  margin:0!important;padding:0!important;
}
#dex-filter-controls #clear-filters {
  width:auto!important;min-height:41px!important;margin:0 auto!important;
  padding:10px 23px!important;border:1px solid rgba(181,215,250,.38)!important;
  border-radius:12px!important;color:#edf6ff!important;
  background:linear-gradient(150deg,rgba(80,119,164,.42),rgba(23,45,72,.75))!important;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.2),0 5px 17px rgba(0,0,0,.2)!important;
  backdrop-filter:blur(12px) saturate(140%)!important;
  -webkit-backdrop-filter:blur(12px) saturate(140%)!important;
  font:700 13px/1.2 system-ui,sans-serif!important;
  transition:transform .16s,background .16s!important;
}
#dex-filter-controls #clear-filters:hover {background:linear-gradient(150deg,rgba(105,149,199,.55),rgba(31,61,95,.82))!important}
#dex-filter-controls #clear-filters:active {transform:scale(.98)!important}
@media(max-width:767px){
  #dex-filter-controls {row-gap:7px!important}
  #dex-filter-controls #type-filters {gap:7px!important}
  #dex-filter-controls #type-filters .type-btn {padding:6px 8px!important;height:38px!important;min-height:38px!important;max-height:38px!important}
}
</style>
<button id="filter-toggle" type="button" aria-controls="dex-filter-controls" aria-expanded="true">Hide Filters</button>

<div class="filter-controls" id="dex-filter-controls">
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

<div class="yv-dex-summary" id="yv-dex-summary" role="status" aria-live="polite">
  <span><strong id="yv-visible-count">0</strong> <span data-yv-count-label>Dokimon shown</span></span>
</div>
<style id="yv-dex-summary-style">
.yv-dex-summary{box-sizing:border-box;max-width:100%;width:fit-content;margin:4px auto 18px;padding:9px 19px;border:1px solid rgba(145,184,230,.27);border-radius:999px;background:linear-gradient(145deg,rgba(36,60,91,.68),rgba(20,39,62,.75));color:#dceaff;font:600 13px/1.4 system-ui,sans-serif;text-align:center}
.yv-dex-summary strong{color:#fff;font-size:15px}
</style>
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
// Apply type-based border colors, blending both colors on dual-type Dokimon.
const dexTypeColors = {
  fire:'#f27655', water:'#58b8f5', grass:'#74c987',
  electric:'#f6d65b', light:'#f8e9a4', dark:'#9c88d6',
  flying:'#8ed5e5', fight:'#e58d6a', fairy:'#ef9fdf',
  ghost:'#a38ce8', poison:'#bc80d8', dragon:'#8b9cff', ice:'#91e0ed'
};
document.querySelectorAll('#dex-grid .dex-entry').forEach(card => {
  const types = (card.dataset.type || '').toLowerCase().match(/[a-z]+/g) || [];
  const valid = [...new Set(types.filter(type => dexTypeColors[type]))];
  if (!valid.length) return;
  card.style.setProperty('--yv-type-one', dexTypeColors[valid[0]]);
  card.style.setProperty('--yv-type-two', dexTypeColors[valid[1] || valid[0]]);
});

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

  let visibleCount = 0;
  entries.forEach(entry => {
    const matchType = [...activeTypes].every(type =>
      entry.dataset.type.includes(type)
    );
    const matchStage = !stage || entry.dataset.stage === stage;
    const matchLoc = entry.dataset.location.includes(loc);
    const matchSearch = entry.dataset.name.includes(search);
    const visible = matchType && matchStage && matchLoc && matchSearch;
    entry.style.display = visible ? '' : 'none';
    if (visible) visibleCount++;
  });
  const count = document.getElementById('yv-visible-count');
  if (count) count.textContent = String(visibleCount);
}
filterDex();

filterToggle.addEventListener('click', () => {
  const isCollapsed = filterControls.classList.toggle('collapsed');
  filterToggle.setAttribute('aria-expanded', String(!isCollapsed));
  filterToggle.textContent = isCollapsed ? 'Show Filters' : 'Hide Filters';
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
