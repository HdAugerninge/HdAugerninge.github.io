# Fantasy Printing Art - Technical Setup & Best Practices

## Project Fundamentals
- **Business Focus**: 3D printing service specializing in articulated dragons, fidget toys, nerd stuff, and customized, web-sourced practical solutions.
- **Routing & Tech Stack**: Hosted statically generated via GitHub Pages user site.
- **Formspree Setup**: The contact form logic in `index.md` uses the `@formspree/ajax` Vanilla JS library via CDN. We intentionally **avoid** standard HTTP Basic action posts to prevent users from being thrown out to Formspree's success/captcha page. It captures validation dynamically inside `data-fs-error`. 

## Bilingual Architecture (DE & EN)
Because GitHub Pages restricts some custom Jekyll i18n plugins in safe-mode:
- **Root Pages = German**: `index.md`, `dragons.md`, etc., serve German content natively since the core audience is German.
- **English Path = `/en/`**: Deep mirrored copies exist in the `en/` subfolder.
- **Liquid Rendering**: Shared headers/footers in `_layouts/default.html` rely on pulling dictionary variables structured inside `_data/de.yml` and `_data/en.yml`. E.g., `{{ ui.nav.home }}`.
- **Best Practice for New Content**: If you add a new page (e.g., `new_gallery.md`), you **must** build a German version at the root folder, and sequentially copy it to `/en/new_gallery.md`. Make sure to attach the `lang: de` and `lang: en` tags in the YAML frontmatter.

## Styling & Theme Rules
We intentionally removed Jekyll's base minimals.
- **Design Core**: Pure CSS defined inside `assets/css/styles.css`. Look and feel relies heavily on `#0b0f19` dark modes, neon cyan/purple combinations (`#00f2fe`), and heavy Glassmorphism overlay panels.
- **Global Background Watermark**: A faint logo (`opacity: 0.04`) sits embedded inside the `body::before` CSS rule so it hovers universally across the interface. 
- **Dropdown Navigation**: Floating dropdowns (like the one for "Models & Inspiration") use a `padding-bottom` bridge on the `.nav-dropdown` container. This extends the hoverable area to cover the visual gap between the trigger and the menu content, ensuring the menu stays open during mouse movement.
- **Media Galleries**: Use `display: grid;` and structure cards with `.media-item`. This class applies to both `<img>` and `<video>` elements.
- **Media Ratios:** Always format videos using `object-fit: contain;` coupled with a solid background (instead of `cover`). Vertically aligned MP4 files (from phones) will stretch and tear aesthetically if framed with `cover`. 

## Universal Lightbox
The media expansion logic is implemented in Vanilla JS at the bottom of `_layouts/default.html`.
- **Media Support**: The lightbox supports both images and videos. It automatically switches between `<img>` and `<video>` tags based on the source element.
- **Navigation**:
    - **UI**: Clickable arrows (`.lightbox-prev`, `.lightbox-next`) are available on the sides.
    - **Keyboard**: Supports `ArrowLeft`, `ArrowRight` for navigation and `Escape` for closing.
    - **Behavior**: The gallery wraps around (end-to-beginning) and uses all `.media-item` elements found on the current page.
- **Video Handling**: Videos in the lightbox should be set to `autoplay`, `loop`, `muted`, and `playsinline` to match the site's aesthetic.

## Process: Adding New Models
The workflow for adding new content starts when a new file (image, video, or GIF) is added to the `resources/` folder.

1. **Hierarchy Detection**:
    - **Layer 1 (Page)**: The first subdirectory under `resources/models/` determines which page the item belongs to (e.g., `dragons/` -> `dragons.md`).
    - **Layer 2 (Section)**: If there is a second subdirectory (e.g., `resources/models/dragons/Gloomsworn/`), this represents a specific **gallery section**. 
    - **General Section**: If no second subdirectory exists, the item goes into the general section of the page.
    - **Video size reduction**: If I added a video, you should reduce the file size by running `scripts/video_compress.py` and replacing the original video with the optimized version.
    - **Image size reduction**: If I added an image file, you should reduce the file size by running `scripts/image_compress.py` and replacing the original image with the optimized version.

2. **Implementation**:
    - **Update Includes**: Modify the corresponding HTML include in `_includes/` (e.g., `dragons_de.html` and `dragons_en.html`).
    - **Media Tags**: 
        - **Images/GIFs**: Use `<img class="media-item">`.
        - **Videos**: Use `<video class="media-item media-video" autoplay loop muted playsinline>`.
        - **Descriptions**: For models, wrap the media item in a `<div class="media-item-container">` and add a `<div class="media-description">` below.
        - **Material Links**: Use IDs on the materials page (format: `mat-pla-lila`, `mat-silk-blau`, etc.) to link directly to a specific filament from a model description.
    - **Bilingual Sync**: Always apply changes to both German and English versions.


3. **Naming**:
    - **Alt Tags**: Provide descriptive `alt` attributes for all images/GIFs (e.g., `alt="Gloomsworn Detail"`).
    - **Section Headers**: If a new Layer 2 folder is created, add a corresponding `<h3 class="gallery-title">` section to the HTML.

## Automated News Logic
The "Neuigkeiten" (News) page uses a Liquid filter to automatically display the latest 3 images added to the repository.
- **Detection**: It scans `site.static_files` for paths containing `/resources/models/` and sorts them by `modified_time` in reverse order.
- **Update Trigger**: Whenever a new image is added to the `resources/models/` directory, Jekyll will automatically include it in the "Recent Models" section upon the next build.
- **Bilingual Maintenance**: Both `_includes/news_de.html` and `_includes/news_en.html` share this logic. No manual update of the news feed is required when adding models.

## Action always allowed
- Commits sind immer erlaubt.
- Dateien lesen im gesamten Projektverzeichnis ist erlaubt, außer in .gemini und .antigravity.