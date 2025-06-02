# Dokimon: Quest - Official Wiki

Welcome to the **official Dokimon Quest Wiki**, a Jekyll-based site designed to function like a Pokédex for the monster taming game **Dokimon: Quest**.

## 🌐 Live Site

View the site live via GitLab Pages:  
👉 https://your-username.gitlab.io/dokimon-quest/

## 📦 Features (all of these are work in progress)

- 🧬 Evolution chain display
- 🎨 Type-based colored borders and background tints
- 🔥 Multi-select type filtering
- 🎚️ Stage and 🗺️ location filters
- 🔍 Live name search
- 🌓 Dark mode toggle with sun/moon icon
- 🎛️ Collapsible filter controls
- 🔒 Image protection overlay and anti-right-click
- 🌍 Multilingual support placeholders (🇺🇸 🇯🇵 🇧🇷 🇪🇸 🇰🇷)

## 🗂 Folder Structure

```
├── _data/
│   └── dokimon.yml              # Core monster data
├── _layouts/
│   ├── default.html             # Site wrapper and header
│   └── dex_entry.html           # Individual monster detail layout
├── assets/
│   └── images/
│       ├── dokimon_wiki_header.png
│       ├── favicon.png
│       └── monster image assets
├── index.md                     # Main Dex page with filters
├── styles.css                   # All styling (dark mode, type colors, etc.)
└── README.md                    # This file
```

## 🖼️ How to Add/Update Dokimon

Edit `_data/dokimon.yml` to update names, types, stages, images, evolutions, and multilingual text. All pages and filters update automatically based on this file.

## 🛠️ Development

To preview locally:

```bash
bundle install
bundle exec jekyll serve
```

Then open: [http://localhost:4000](http://localhost:4000)

## 📤 Deploying to GitLab Pages

Make sure your `.gitlab-ci.yml` includes:

```yaml
pages:
  stage: deploy
  script:
    - mkdir public
    - cp -r * public/
  artifacts:
    paths:
      - public
  only:
    - main
```

> 🔁 Push to `main` branch to deploy automatically.

---

## 💡 Credits

- Game: **Dokimon: Quest**
- Design by: Yanako RPGs
- https://www.yanakorpgs.com/
