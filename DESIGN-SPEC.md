# Netflix → Jellyfin design spec

Measured from netflix.com/browse on 2026-10-26 (logged-in web UI) with computed styles.
Main reference viewport: 1384×797 CSS px. Values are CSS px unless noted.

## Colour
| Token | Value | Where |
|---|---|---|
| page | `#141414` (rgb 20,20,20) | body/html |
| surface | `#181818` | details modal, hover-card info panel |
| surface-2 | `#232323` | profile dropdown |
| surface-3 | `#242424` / border `#4d4d4d` 1.5px | season select |
| row-active | `#333333` | current episode row |
| divider | `#404040` 1px | episode rows |
| text | `#fff` | |
| text-muted | `rgba(255,255,255,.7)` | inactive nav links |
| text-meta | `#bcbcbc` | modal year/seasons |
| text-desc | `#d2d2d2` | episode synopsis, episode number |
| text-label | `#777` | "Cast:", "Genres:" labels |
| accent | `#e50914` | progress bar, badges |
| progress-track | `rgba(255,255,255,.3)` 2px | |
| pill-active | `rgba(255,255,255,.2)` | active nav pill |
| btn-secondary | `rgba(128,128,128,.4)` | "More Info" |
| icon-btn | `rgba(42,42,42,.6)` + 2px `rgba(255,255,255,.5)` border | round add/like buttons |
| overlay | `#000` at opacity .7 | behind modal |

## Type
- Family: `Netflix Sans` → fallback `"Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif`. Netflix Sans isn't licensed for us, so we use the fallback stack.
- Nav links: 16px / 400, inactive at 70% white; active is 500 white in a pill.
- Row title (h2): 24px / 500 (18px under ~1100px viewport).
- Hero meta: 18px / 500; hero description: 24px / 30px line-height.
- Hero buttons: 18px / 500.
- Modal: section heading 24px / 500, top-10 line 20px / 500, description 14px / 24px, cast labels 14px / 20px.
- Episode: title 16px / 500, duration 16px, synopsis 14px / 20px `#d2d2d2`, number 24px `#d2d2d2`.
- Badges (HD): 11.2px, 1px `rgba(255,255,255,.4)` border, radius 3px, padding 0 5.6px.

## Layout
- Side gutter: 60px (≥ ~1900 vw), 48px (~1400), 36px (≤ ~1100).
- Header: sticky, height 80, padding 0 / gutter. Background `linear-gradient(rgba(0,0,0,.8), transparent)` at the top; solid `#000` once scrolled (transition: background-color .4s).
- Nav pills: group padding 4px, gap 6px; each pill padding 10px 16px, radius 24px; active bg `rgba(255,255,255,.2)`; transition background-color .2s.
- Logo: 76×20 at 1384, red `#e50914`.
- Hero: inset card at x = gutter, top 88, height ≈ 591 (≈ 74vh), radius 24px, shadow `0 10px 20px 32px rgba(0,0,0,.45)`, content padding 36px. Ambient radial glow from the hero colour behind the page top.
- Rows: title→cards 13px; card bottom→next title 36px (≈ 221px row pitch at 1384).
- Cards: 16:9 backdrops, radius 12px, gap 8px; 5 visible + peek at 1384, 7 at 2077 (card width = (vw − 2·gutter − (n−1)·8) / n).
- Search grid: 5 columns, column gap 8, row gap 19, gutter 60, radius 12.

## Components
- Primary button (Play): white bg, black text, radius 9999px, padding 8px 20px, height 48 (hero). Modal variant: radius 4px, padding 8px 22px.
- Secondary (More Info): `rgba(128,128,128,.4)`, white text, same pill shape.
- Round icon buttons: 38px, 2px `rgba(255,255,255,.5)` border, `rgba(42,42,42,.6)` fill, radius 50%.
- Hover card: about 1.5× scale (251→377 wide) after a short delay; radius 6px; shadow `0 3px 10px rgba(0,0,0,.75)`; `#181818` info panel, 16px padding, round buttons, red 2px progress line.
- Details modal: width 850, top 32, radius 6, `#181818`; backdrop with `linear-gradient(0deg,#181818,transparent 50%)` fade; content padding 0 48px; close button 36px circle `#181818`.
- Episode row: padding 16px, radius 4px, 1px `#404040` bottom border; thumbnail ≈130×73 radius 4.
- Profile dropdown: `#232323`, radius 12px, 1px `rgba(255,255,255,.04)` border, shadow `0 2px 8px rgba(0,0,0,.4)`; items 48 tall, radius 8, padding 8px 12px; avatars 32px radius 4.
- Search input: 400×56 pill, padding 16px 53px 16px 48px, 1px light border.

## Motion
- Nav background: .4s linear. Pill background: .2s.
- Buttons: background-color .25s cubic-bezier(.4,0,.68,.06).
- Hover-card expand: Netflix delays about 400ms, then scales over about 300ms.

## Jellyfin mapping and limits
- Header → `.skinHeader` / MUI `header.MuiAppBar-root` (Jellyfin 12 uses the MUI app bar).
- Rows → `.verticalSection > .sectionTitle` + `.emby-scroller .itemsContainer > .card`.
- Cards → `.cardScalable`, `.cardImageContainer`, `.cardText`; progress → `.itemProgressBar(Foreground)`.
- Details page (`#itemDetailPage`) is a full page, not a modal, so it is a wide `#181818` card (viewport minus the gutters, max 1600px) with Netflix's More Info styling inside. The image is capped at 70vh.
- **Can't do with CSS alone:** a home hero/billboard (no featured-item markup on the home page); Netflix's hover pop-out panel with buttons and episode info (Jellyfin has its own hover overlay, which we restyle); Netflix Sans; the "Top 10" and "Recently added" ribbons.
