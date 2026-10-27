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
- Hero meta: 16px / 500 items, `•` separators at 40% white, gap 8px, row 32px tall; rating (TV-MA) 400. Hero description: 20px / 28px white, ≈500px wide (re-measured 2026-10-26; an earlier title measured 18px meta, 24/30 description).
- Hero buttons: 18px / 500.
- Modal: section heading 24px / 500, top-10 line 20px / 500, description 14px / 24px, cast labels 14px / 20px.
- Episode: title 16px / 500, duration 16px, synopsis 14px / 20px `#d2d2d2`, number 24px `#d2d2d2`.
- Badges (HD): 11.2px, 1px `rgba(255,255,255,.4)` border, radius 3px, padding 0 5.6px.

## Layout
- Side gutter (Netflix's row stylesheet): 24px (< 600), 36px (600–1279), 48px (1280–1599), 60px (1600–2559), 72px (≥ 2560).
- Header: sticky, height 80, padding 0 / gutter. Background `linear-gradient(rgba(0,0,0,.8), transparent)` at the top; solid `#000` once scrolled (transition: background-color .4s).
- Nav pills: group padding 4px, gap 6px; each pill padding 10px 16px, radius 24px; active bg `rgba(255,255,255,.2)`; transition background-color .2s.
- Logo: 76×20 at 1384, red `#e50914`.
- Hero: inset card at x = gutter, top 88, 1288×591 at 1384×797 (≈ 74vh, ≈ width × .4588), radius 24px, shadow `rgba(0,0,0,.45) 10px 20px 32px 0`, overflow hidden, content padding 36px, anchored bottom-left. Overlay `linear-gradient(90deg, rgba(0,0,0,.6) 0%, transparent 60%), linear-gradient(0deg, rgba(0,0,0,.5) 0%, rgba(0,0,0,.1) 35%, transparent 70%)`. Title logo ≤ 415×166, 20px above meta; meta → description 8px; description → buttons 32px; buttons 12px apart. First row title 36px below the card. Ambient radial glow from the hero colour behind the page top. Badges ("Recently Added") bottom-right: 13px / 500, `rgba(0,0,0,.5)`, padding 8px, radius 8px.
- Rows: title→cards 13px; card bottom→next title 36px (≈ 221px row pitch at 1384).
- Cards: 16:9 backdrops, radius 12px, gap 8px. Width = (page width without scrollbar − 2·gutter − (n−1)·8) / n, with n = 2 (< 600), 3 (600–959), 4 (960–1279), 5 (1280–1599), 6 (1600–1919), 7 (1920–2559), 8 (≥ 2560) by viewport width. Read from Netflix's `--slot-width` rules 2026-10-27; 248.2×139.7 at 1384 (1369 client).
- Search grid: 5 columns, column gap 8, row gap 19, gutter 60, radius 12.

## Components
- Primary button (Play): white bg, black text, radius 9999px, padding 8px 20px, height 48 (hero). Modal variant: radius 4px, padding 8px 22px.
- Secondary (More Info): `rgba(128,128,128,.4)`, white text, same pill shape.
- Round icon buttons: 38px, 2px `rgba(255,255,255,.5)` border, `rgba(42,42,42,.6)` fill, radius 50%.
- Hover card: about 1.5× scale (251→377 wide; 368→552 measured again) after a short delay, centred on the card; radius 6px; shadow `0 3px 10px rgba(0,0,0,.75)`; `#181818` info panel, 16px padding, round buttons, red 2px progress line. Panel buttons: 34px white play disc, then 38px round buttons with a 2px `rgba(255,255,255,.5)` border on `rgba(42,42,42,.6)`, 8px apart; text about 17px below them.
- Details modal: width 850, top 32, radius 6, `#181818`; backdrop with `linear-gradient(0deg,#181818,transparent 50%)` fade; content padding 0 48px; close button 36px circle `#181818`.
- Episode row: padding 16px, radius 4px, 1px `#404040` bottom border; thumbnail ≈130×73 radius 4.
- Profile dropdown: `#232323`, radius 12px, 1px `rgba(255,255,255,.04)` border, shadow `0 2px 8px rgba(0,0,0,.4)`; items 48 tall, radius 8, padding 8px 12px; avatars 32px radius 4.
- Search input: 400×56 pill, padding 16px 53px 16px 48px, 1px light border.

## Motion
- Nav background: .4s linear. Pill background: .2s.
- Buttons: background-color .25s cubic-bezier(.4,0,.68,.06).
- Hover-card expand: Netflix delays about 400ms, then scales over about 300ms.

## Profile selector
Measured from the live Netflix profile selector on 2026-10-26 at 2374×1723 and 393×852 CSS px.

- Background: black with `radial-gradient(max(1600px, 125vw) at 50% -54dvh, rgba(111,24,29,.8) 19%, rgba(56,12,15,.4) 60%, transparent 100%)`.
- Heading: 32px / 38.4px, weight 700. Group gap 16px, centred in the space below the 80px header, with 24px bottom padding.
- Desktop profile buttons: 160px wide, padding 16px, radius 16px, 8px between buttons. Artwork 128×128, radius 12px. Name 24px below artwork, 18px / 21.6px, weight 500.
- Phone profile buttons: 96px wide, padding 12px, artwork 72×72. Three columns at 393px; names 14px / 16.8px, 12px below artwork.
- Manage Profiles: 40px tall, 16px / 16px, weight 500, padding 6px 16px, pill radius, `rgba(0,0,0,.7)` fill; 36px below desktop profiles, 32px on phone.
- Jellyfin mapping: `#loginPage .visualLoginForm`, `#divUsers`, `.manualLoginForm`, and `.readOnlyContent`. Nine profiles wrap into two centred rows on desktop and three on phone. Jellyfin's authentication actions replace the Manage Profiles action; actual user pictures remain. Long names may wrap on phone to preserve identification. The visible selector heading is supplied by CSS; Jellyfin retains its original sign-in heading in the DOM.

## Jellyfin mapping and limits
- Header → `.skinHeader` / MUI `header.MuiAppBar-root` (Jellyfin 12 uses the MUI app bar).
- Rows → `.verticalSection > .sectionTitle` + `.emby-scroller .itemsContainer > .card`.
- Cards → `.cardScalable`, `.cardImageContainer`, `.cardText`; progress → `.itemProgressBar(Foreground)`.
- Hover pop-out → landscape cards in rows (`.overflowBackdropCard`): the whole `.cardBox` scales 1.5×, Jellyfin's hover buttons move under the image onto a `::before` panel, and the text slides down. Posters keep a flat hover. A card scrolled to the right edge can't be detected, so its pop-out isn't anchored right as Netflix's is.
- Details page (`#itemDetailPage`) is a full page, not a modal, so it is a wide `#181818` card (viewport minus the gutters, max 1600px) with Netflix's More Info styling inside. The image is capped at 70vh.
- Home billboard → Media Bar plugin (`#slides-container`, needs File Transformation 3.x). Its Details button is relabelled "More Info" through CSS; the favourite button stays as a matching round button; slide dots sit bottom-right. The plugin's row offset ignores the 80px header, so the theme sets `.homeSectionsContainer` margin-top itself.
- **Can't do with CSS alone:** the hero's ambient colour glow (it's derived from each image); Netflix Sans; the "Top 10" and "Recently added" ribbons.
