# Fantasy Printing Art - Website Blueprint

## Core Identity
- **Business Name**: Fantasy Printing Art
- **Niche Focus**: 3D Printing Service. Primary categories: Articulated Dragons, Fidget Toys, Pop Culture Merch (Star Wars, Harry Potter, LotR), and Practical Solutions.
- **Repository**: Hosted manually as a "User Pages" GitHub Pages setup.

## Architecture & Styling
We deliberately bypassed Jekyll's default `jekyll-theme-minimal` settings to achieve a "Wow"-factor premium design.
- **Layout Config**: Uses a custom wrapper located at `_layouts/default.html`.
- **Primary Styling Elements**: (`assets/css/styles.css`) Features a modern Dark Mode palette (background: `#0b0f19`), Glassmorphism transparent nav-bars/cards, and vibrant neon cyan/purple gradients for hover animations and headers. Avoids TailwindCSS.
- **Content Strategy**:
  - `index.md` (Homepage): Combines HTML structures for Heros, Info Grids, Pricing Transparency, and a customized Contact Form.
  - Subpages (`dragons.md`, `merch.md`, `practical.md`): Simplified markdown pages designed primarily as photo gallery containers.

## Technical Details & Deployment
- **Local Development Exception**: Do not assume the developer uses a local terminal Ruby/Jekyll environment. To prevent blockers, the standard deployment workflow consists of directly committing and executing a `git push` command, allowing GitHub Pages background processors to build it live.
- **Contact Forms**: Designed relying on frontend-only solutions. The `index.md` contains an HTML form built for Formspree.io integration. The `action` tag requires insertion of the specific Formspree endpoint ID.
