# Netflix theme for Jellyfin 12

- `netflix.css`: commented source of truth.
- `netflix.min.css`: the exact copy saved in Dashboard → Branding → Custom CSS (SHA-256 `fa8ca0d0…`).
- `DESIGN-SPEC.md`: measurements taken from netflix.com.
- `backup/branding-2026-10-26.json`: branding settings before the theme (Custom CSS was empty).

## Rebuild after editing
    { printf '/* Netflix theme for Jellyfin 12 — generated from ~/jellyfin-netflix-theme/netflix.css (edit that file, not this). */\n'; python3 -I tools/minify.py netflix.css; } > netflix.min.css
Paste `netflix.min.css` into Dashboard → Branding → Custom CSS (or the readable `netflix.css`; both work).

## Undo
Clear Dashboard → Branding → Custom CSS and save.

## Caching note
Jellyfin 12 keeps branding in a persistent query cache (IndexedDB `keyval-store` → `jellyfin-query-cache`).
After a CSS change, other browsers may show the old CSS until that cache goes stale. Clear site data to force it.

## Backdrops on narrow screens
- **Desktop layout at 1000px or wider:** uses Jellyfin's backdrop layer.
- **Mobile layout (phones and tablets):** Jellyfin puts the backdrop on `#itemBackdrop` when the per-device Settings → Display → "Details banner" option is on (it is on by default).
- **Desktop layout under 1000px:** Jellyfin loads no backdrop at all, so CSS can't show one.
