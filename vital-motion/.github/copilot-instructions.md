# Copilot Instructions for AI Agents

## Project Overview
This codebase is a static website for "Vital Motion," structured with HTML, CSS, and image assets. It is organized for a PERSONAL TRAINING SERVICE, featuring both Spanish and English content. There is no backend or build system; all files are served as-is.

## Key Directories & Files
- `index.html`, `index-2.html`: Main entry points for the site.
- `e-menu.html`, `e-menuenglish.html`: Digital menu pages (Spanish/English).
- `_images/`: Contains HTML menu sections (e.g., `bebidas.html`, `combos.html`) and their English versions, used as includes or standalone pages.
- `css/`: Custom and third-party stylesheets (e.g., Bootstrap, Swiper, Ionicons).
- `images/`: All image assets and some HTML fragments for UI elements.
- `js/`, `vid/`: (If present) JavaScript and video assets.

## Patterns & Conventions
- **Language Support**: Most content is duplicated for Spanish and English, with files named `*english.html` for English versions.
- **Menu Structure**: Menu sections are modularized as separate HTML files in `_images/` and referenced or included in main menu pages.
- **No Build Step**: All files are edited directly; there is no build, test, or deployment automation in this repo.
- **Styling**: Uses Bootstrap and custom CSS. Do not modify third-party CSS files directly; add overrides in `style.css`.
- **Navigation**: Navigation between sections/pages is handled via standard HTML links.

## Productivity Tips for AI Agents
- When adding new menu items or sections, follow the naming and duplication pattern for both languages.
- Place new images in `images/` and reference them with relative paths.
- For new styles, update `css/style.css` only.
- Keep HTML fragments in `_images/` modular and language-specific.
- Do not introduce JavaScript frameworks or backend code unless explicitly requested.

## Example: Adding a New Menu Section
1. Create `newsection.html` and `newsectionenglish.html` in `_images/`.
2. Add links to these in `e-menu.html` and `e-menuenglish.html`.
3. Add any images to `images/` and styles to `css/style.css`.

## Integration Points
- No external APIs or dynamic integrations are present.
- All content is static and must be manually updated.

---

For questions about structure or conventions, review the main HTML files and `_images/` directory for examples.
