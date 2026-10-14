## Part C — Homepage structure

| Sequence | Headline and purpose | Actions | Media |
|---|---|---|---|
| Hero | Robots That Cooperate, Manipulate, and Interact. Establish the scientific question with the 40–60 word introduction. | Explore Our Research; Discover Our Projects | Wide experimental video of cable attachment and transport, once approved; an honest media placeholder until then |
| About | Robots that act on the world. Explain mission, vision, approach, and affiliation. | Continue to research | Real laboratory photograph when supplied; three concise methodology statements |
| Research | One agenda. Five connected themes. Show the long-term problems the lab studies. | Expand each theme’s questions and approach | Five experimental or scientific media panels |
| Featured research | Cable Manipulation and Robotic Knotting. Explain how flexible structures become functional connections and attachment mechanisms within the broader mission. | Cable-interlacing project | Credited hitch or knot experiment paired with contact geometry |
| Projects | Specific questions. Physical systems. Connect research to concrete investigations. | Open one of five project detail pages | Project-specific photograph or 5–12 second loop |
| Selected publications | Research, with its evidence. Connect claims to accessible records. | Paper; project; BibTeX; confirmed video/code | Three selected contribution panels; only one populated until further verification |
| Publication list | Make the bibliography usable for researchers. | Combine year, type, and topic filters; reset | Concise text records; no decorative charts |
| People | Meet the lab. Introduce the PI and reserve member groups. | Email; confirmed academic profiles | Real portraits and candid lab images |
| News | Lab updates. Show dated scientific activity. | Read related paper or project | Three newest verified entries when available; an empty state now |
| Join Us | Bring your questions. Build your research. Explain fit and inquiry materials. | Email the director | Optional real student experiment image; no stock people |
| Contact | Let’s connect. Provide room, affiliation, email, and official links. | Email; institution; department | Optional campus map only after exact entrance/location confirmation |

Navigation: Home | About | Research | Projects | Publications | People | News | Join Us | Contact. Keep all nine links on wide desktops and a keyboard-operable disclosure menu on smaller screens. Project pages return to the homepage projects section. Avoid nested dropdowns until the content volume warrants them.

The homepage prioritizes concise orientation; long technical narratives live on project pages and inside research disclosures. The A–H document supplies the full editorial copy for future standalone About, Research, and People pages if the lab grows.

## Part D — Research and project storytelling

Use the sequence **question → physical mechanism → method → evidence → limitation**. Begin with what a visitor can see, introduce one technical variable, then connect it to the scientific question. Mark actual data, explanatory schematics, and proposed systems explicitly.

| Research theme | Experimental video | Scientific animation | Interactive concept | Still images |
|---|---|---|---|---|
| Cable manipulation and robotic knotting | Cable routing, hitch formation, attachment, and lift in one documented trial | Knot or hitch geometry and cable–object contact region | Select a stage to inspect constraints; avoid implying a validated simulator | Full-system photograph plus attachment close-up |
| Physical interaction | Actual contact establishment and regulation on aerial or ground robots | Contact regions and constraints | Inspect an illustrative contact mode with assumptions labeled | Robot–object interface and measured interaction state |
| Cooperative robotics | Shared-load motion with all robots visible | Robot trajectories and interaction-force vectors | Inspect individual roles and shared constraints | Team configuration with geometry annotations |
| Dynamics and control | A real contact or slack–tension transition synchronized to measurements | Mode changes, suspended-load response, and force directions | Inspect an idealized taut/slack diagram with assumptions shown | Interface close-up plus a readable sensor trace |
| Perception and planning | Observe–act–observe sequence, followed by retrieval when demonstrated | Visibility changes and candidate actions | Step through a labeled illustrative decision sequence | Actual camera view and estimated-state overlay |

**Project A — Cable interlacing:** Show the initial attachment problem, then the cable route and resulting contact. A continuous camera view supports understanding of the maneuver. Use a close-up to explain friction and an overhead diagram to explain routing. Preserve the original institution and authors. Do not cut together unrelated trials to imply one continuous success.

**Project B — Sliding transport:** Introduce the hook and changing cable distribution before showing robot motion. A synchronized schematic clarifies why attachment geometry matters. Pair any selected tracking trace with units, test conditions, and the authors’ explanation. Keep the preprint label visible.

**Project C — Blimp capture emulation:** Show robot roles, target motion, approach, and contact. State the terrestrial emulation scope in the caption. Add a compact assumptions panel naming buoyancy, aerodynamic drag, gravity, and actuation differences; do not label a blimp trial as orbital validation.

**Project D — Cable sensing:** Pair a physical event with its measurement. A tension trace should show actual measurements and units, with an indication of how the estimate is used. Until sensors and experiments are confirmed, use only a labeled conceptual state diagram.

**Project E — Search and manipulation:** Present an exploratory storyboard: partial observation, action choice, new observation, and retrieval attempt. Explain how an action can reveal information. Use conceptual graphics until hardware and results exist.

**Caption template:** “What is happening. Which scientific variable matters. What this experiment demonstrates under the stated conditions. Original experiment location and credited authors.” Include failure cases and limitations where they help assess the claim.

**Media formats and delivery**

- MP4 (broad support) plus WebM where useful: preferred for actual experiments and preview loops. Video gives better compression and playback control than GIF for photographic motion. Use poster images, `playsinline`, and `preload="none"` or `metadata`; mute autoplay previews and provide a pause control. Never autoplay audible content.
- GIF: reserve for very short, low-resolution explanatory snippets where video is unsuitable; avoid it for large experiment sequences.
- Animated WebP: useful for short visual snippets with a static fallback, but lacks the playback and caption controls of video.
- Lightweight SVG: preferred for technical diagrams, vector labels, and restrained schematic motion. Provide textual explanations and respect reduced-motion settings.
- JavaScript interactions: use for inspecting roles, geometry, and assumptions. Label illustrative quantities; do not invent measurements or present a toy model as experimental validation.
- YouTube: click-to-load embeds for full talks or demonstrations, with a clear iframe title and captions/transcript. Avoid loading several players at initial page load.
- Galleries: responsive image grids with meaningful captions. Bootstrap modal or the existing GLightbox can handle a lightbox after real assets arrive; keyboard access and focus restoration must be checked.

Target mobile-first assets. Give images explicit dimensions, responsive sizes, and descriptive alt text. Load below-fold media lazily. A muted loop needs an adjacent description; videos with speech need captions and a transcript. The hero must remain legible and useful before its media loads. Do not create synthetic imagery that appears to document a real experiment.

## Part E — Visual design

**Direction:** A scientific editorial layout with clean typography, clear section numbers, real experimental media, and room for technical explanation. Keep the ΔMARS wordmark distinct from the university affiliation. A simple Δ favicon is a lab graphic, not a reproduction of the official Oakland mark.

**Palette:** Oakland core gold `#BC945B`, black `#000000`, and white `#FFFFFF`, verified from [Oakland’s official design guidance](https://oakland.edu/brand/design-with-purpose/index). Use near-black `#20201E` and warm white `#F7F5F0` for large UI surfaces. Small text uses dark ink or a darker gold treatment checked against its actual background; core gold on white is primarily decorative. Do not rely on hue alone for status distinctions. Use authentic, unaltered official university assets when supplied.

**Typography:** Helvetica/Arial/system sans-serif for interface and body, with an ordinary monospace stack for BibTeX and technical labels. This avoids font downloads and licensing assumptions. Use a large but responsive headline, 16px or larger main text, generous line height, and short paragraphs. University logo typography should come from the supplied official asset rather than an imitation.

**Layout:** Maximum content width around 1180px. A two-column hero, five theme panels in a responsive two-column grid, a responsive project grid, a three-panel selected-publication row, and a readable list for the bibliography. One-column stacking on phones. Project narratives use a narrower reading width. Make long titles and email addresses wrap without horizontal overflow.

**Interaction:** Research details use native HTML disclosures; project titles are ordinary links; publication filters use labeled native selects. Hover states are restrained. A visible focus indicator, skip link, semantic landmarks, logical headings, and Escape-to-close mobile navigation support accessibility. Avoid hover-only content and auto-rotating carousels.

**Animation:** Use restrained transitions only where they explain a scientific event. Reduced-motion visitors receive static views and no forced smooth scrolling. A future hero video should have a poster and pause control. Current placeholders have no decorative motion.

**Image direction:** Actual robots, cables, attachments, researchers, and facilities. Prioritize clear physical relationships over dramatic crops. Do not use humanoid stock photos, glowing AI brains, synthetic lab photographs, or stock portraits.

## Part F — Website implementation

The current workspace is a local BootstrapMade/FlexStart HTML export. Keep it static for this version. There is no reason to introduce WordPress, React, a database, or a server application for the current content and interactions.

**Implemented source structure**

- `content/lab.json`: homepage copy, research themes, project descriptions, project status, and verified bibliography.
- `content/blueprint-appendix.md`: the strategy and verification material in Parts C–H.
- `scripts/build_lab.py`: small standard-library Python generator; run `python3 scripts/build_lab.py` from this directory after content edits.
- `index.html`: generated homepage, all eight content sections, navigation, recruitment, and contact.
- `project-*.html`: five generated static project pages with readable URLs and evidence/status notes.
- `assets/css/lab.css`: lab-specific responsive presentation.
- `assets/js/lab.js`: mobile navigation and publication filtering.
- `assets/img/lab-mark.svg`: Δ favicon.
- `WEBSITE_BLUEPRINT.md`: generated A–H editorial deliverable.

Static generation makes the core text available without JavaScript and keeps each project independently linkable. The small generator uses only Python’s standard library; no dependency installation or build service is needed. Bootstrap CSS remains available, while the old template scripts and stock assets are not loaded by the new pages.

**Publication data:** Keep unverified records outside the displayed list. Render verified metadata at build time; filter those visible HTML records with plain JavaScript. Add paper, DOI, video, and code links only when populated and verified. Preserve each source URL and missing fields in the data. A future download link should point to an authorized author manuscript or open paper, not imply local hosting when the file is absent.

**Project details:** Use normal static pages generated from the data. Add approved videos and image galleries to these pages when assets arrive. Keep collaborators and funding associated with the correct project, not a global banner that suggests support for every investigation.

**News:** Store verified entries with separate event and announcement dates plus an explicit planned/completed state. Build a chronological archive and show the newest three on the homepage once available. The present `news` array is intentionally empty; dated example drafts are kept in this document only.

**Member profiles:** Use structured profiles and optional URLs when confirmed. Current student/collaborator groups reserve space without inventing membership.

**Libraries:** Standard HTML/CSS/JS suffice for disclosures, navigation, filtering, status labels, video playback, and static diagrams. Bootstrap can support layout and modal dialogs. GLightbox is useful only after a gallery exists. A chart library is warranted only for real scientific data that benefits from inspection. Avoid loading unused template libraries such as counters, sliders, and portfolio filters.

**SEO:** Descriptive page titles and summaries are implemented, with basic Open Graph text. Add a canonical URL, social image, sitemap, robots policy, and scholarly structured metadata after the domain and bibliographic records are confirmed. Use per-project descriptions when final copy is approved. Do not invent a public domain or deployment URL. Research keywords should appear naturally in explanatory prose rather than in keyword stuffing.

**Contact:** Use the supplied email with an ordinary mailto link. The old PHP form handlers are not connected to the new site; static hosting cannot execute them. Add a submission service only if form submission becomes an explicit requirement.

**Before public packaging:** The export still contains unused original demo pages and stock assets. Exclude them from the deployment or archive them outside the served directory, and check template license/attribution requirements. Do not publish a directory containing reachable generic business/blog pages. This iteration updates the local workspace; it does not create a hosted Site or deploy the draft.

**Verification:** Check generated anchors and local assets, page structure, bibliography metadata, filter intersections and empty states, mobile navigation, focus behavior, text contrast, and phone/desktop layouts. JavaScript syntax and runtime checks depend on the available environment. Check the actual downloaded media and external links again when final assets are provided.

## Part G — Improvement recommendations

1. Obtain one clear, credited experimental sequence for the hero. It should explain cable interaction without requiring a visitor to read a paper first. Include a static poster and short text explanation.
2. Confirm the formal lab expansion and naming style. Use ΔMARS consistently in all visible branding and metadata; add a plain-text search alias where appropriate once the official name is confirmed.
3. Curate three selected contributions around distinct questions: attachment, cooperative transport, and interaction sensing or autonomy. Do not imply a contribution exists simply to fill the third panel.
4. Establish a verified bibliography from publisher records and author-approved manuscripts. Link papers to the appropriate project, code, and experiment; distinguish preprints from accepted and published work.
5. Record project stage, experiment institution, collaborator role, and funding separately. This makes the lab’s emerging Oakland program visible without recasting earlier work as new Oakland results.
6. Strengthen recruitment with concrete project scopes, expected student activities, degree pathways, and verified application links. When funded opportunities are confirmed, add a dated posting with eligibility and contact instructions.
7. Add authentic member profiles and researcher–student experiment photographs. Describe how students contribute without promising publication outcomes or specific funding.
8. Use lab news to document verified progress, not to fill a feed. Quarterly content review can catch stale opportunity posts, broken links, and outdated project states.
9. Add small explanatory diagrams alongside real experiments. Explain a cable state, contact region, or coordination constraint before offering more detailed methods.
10. Publish limitations alongside demonstrations. This improves scientific clarity, helps potential collaborators identify open questions, and keeps emulation and experimental evidence properly scoped.

## Part H — Information requiring verification

- [ ] Official MARS expansion and whether the full name should match “Distributed Multi-Agent Robotic Systems” in the author-posted manuscript.
- [ ] Final lab wordmark and approved Oakland University logo asset.
- [ ] Recheck publisher records for later metadata changes. Four citations, including cable interlacing, have now been supplied by the author and added to the site; empty volume/issue fields remain omitted.
- [ ] Three selected publication choices; complete bibliography across all actual publication categories and venues.
- [ ] Sliding-cable preprint DOI registration, any later accepted venue, video URL, and code repository. Do not describe the preprint as peer-reviewed without confirmation.
- [ ] Project stages for cable interlacing, blimp capture, and cable sensing; distinguish historical work, ongoing Oakland activity, and proposed directions.
- [ ] Project-specific collaborations and each experiment’s original institutional location. The sliding preprint identifies Oakland University; do not generalize that affiliation to every project.
- [ ] Blimp-project Michigan Space Grant Consortium award, award period, exact acknowledgment, and authorized logos. Funding in the sliding-cable manuscript does not by itself verify the blimp award.
- [ ] Author approval of the sliding-project acknowledgment: the manuscript names NASA award 80NSSC25M7087 through MSGC. Preserve the exact scope and required acknowledgment.
- [ ] News announcement dates and event dates; IROS and LARS-LARC participation, presentation titles, and whether events occurred. No scheduled item is presented as completed.
- [ ] Real experimental videos, images, captions, reuse permission, credit, accessible transcripts, and hero poster.
- [ ] PI portrait and any additional approved educational/appointment details. No dates or awards have been added.
- [ ] Actual members, positions, bios, contact permissions, and personal profile URLs.
- [ ] Official lab Google Scholar, GitHub, LinkedIn, and collaboration links.
- [ ] Confirm Engineering Center Room 450 as the visitor-facing lab location; email and room are supplied in the brief.
- [ ] Recruitment availability, funded positions if any, degree/application links, and inquiry expectations.
- [ ] Final domain and hosting method; canonical URLs, social-preview image, sitemap, and packaging policy.
- [ ] Template license terms and whether attribution is required for this export before deployment.

### Verification sources and limits

- [Author-posted sliding-cable preprint metadata](https://arxiv.org/abs/2610.13665): title, authors, year, submission date, preprint classification, and pending DOI registration.
- [Author-posted full manuscript](https://arxiv.org/html/2610.13665v1): lab expansion, Oakland affiliations, project mechanism, experimental reporting, and project-specific funding acknowledgment.
- [Oakland ECE department](https://www.oakland.edu/secs/departments/ece/): official department link and affiliation context.
- [Oakland design guidance](https://oakland.edu/brand/design-with-purpose/index): official core palette and university identity guidance.

Publisher pages for cable interlacing and aerial knot formation were inaccessible in this review. Their citations and DOI links are included from the records supplied by the author; no additional publication details are inferred. The user-supplied brief and updated positioning remain the source for the lab director’s biography, laboratory room, research interests, and unverified project concepts. No Swarms Lab content or members were migrated.

### Validation completed for this draft

Six generated pages passed checks for unique section IDs, one H1 per page, existing local assets, local page links, and anchor destinations. Requested introduction, overview, mission, vision, theme descriptions, and project descriptions are within the specified word ranges; the PI biography is approximately 150 words. All A–H parts are present. The local server returned HTTP 200 for the homepage.

JavaScript ran successfully against a lightweight DOM mock covering publication filter intersections, empty results, reset, result counts, mobile menu toggling, same-page link closure, and Escape with focus return. This validates logic, not actual browser rendering or assistive technology behavior. Browser preview failed twice because the browser request-header policy could not load, so desktop/mobile appearance and live browser interactions remain unverified.

### Publication presentation update

The homepage bibliography now follows the supplied reference: a horizontal thumbnail on the left, authors above a bold title and blue publication-type badge, a venue/year line, and an inline Abstract/BibTeX/Tags/Links row. The separate three-panel preview has been removed. Abstract and BibTeX buttons expand content inline; tags apply the topic filter. Only confirmed resource links are shown. Thumbnail spaces remain placeholders until a paper-specific image is supplied. Rows stack vertically on small screens.
