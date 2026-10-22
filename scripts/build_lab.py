"""Build static lab pages and the A–H content document. Run from the project root."""
import json
from pathlib import Path
from html import escape as e

c=json.loads(Path('content/lab.json').read_text())

def paragraphs(text):
    return ''.join('<p>'+e(p)+'</p>' for p in text.split('\n\n'))

def list_html(items):
    return '<ul>'+''.join('<li>'+e(x)+'</li>' for x in items)+'</ul>'

nav_items=[('hero','Home'),('about','About'),('research','Research'),('projects','Projects'),('publications','Publications'),('people','People'),('news','News'),('join','Join Us'),('contact','Contact')]

def shell(title,main,home=False):
    prefix='' if home else 'index.html'
    nav=''.join(f'<a href="{prefix}#{id}">{label}</a>' for id,label in nav_items)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{"ΔMARS Lab | Δ Multi-Agent Robotic Systems Lab" if home else e(title)+" | ΔMARS Lab · Oakland University"}</title><meta name="description" content="ΔMARS Lab at Oakland University studies cooperative robotics, physical interaction, and autonomous manipulation, with a distinctive focus on cables and robotic knotting.">
<meta property="og:title" content="{"ΔMARS Lab | Δ Multi-Agent Robotic Systems Lab" if home else e(title)+" | ΔMARS Lab"}"><meta property="og:description" content="{e(c['supporting_line'])}"><meta property="og:type" content="website">
<link rel="icon" href="assets/img/lab-mark.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/vendor/bootstrap/css/bootstrap.min.css"><link rel="stylesheet" href="assets/css/lab.css?v=20261021b"><link rel="stylesheet" href="assets/vendor/bootstrap-icons/bootstrap-icons.css"></head>
<body><a class="skip-link" href="#main">Skip to content</a><header class="lab-header"><div class="container header-inner"><a class="brand" href="index.html"><span class="brand-wordmark"><img class="brand-logo" src="assets/img/delta-mars-logo.png" alt="ΔMARS"><span class="brand-lab">Lab</span></span><span class="brand-affiliation">Oakland University · ECE</span></a><button class="menu-toggle" type="button" aria-controls="navigation" aria-expanded="false">Menu</button><nav id="navigation" aria-label="Main navigation">{nav}</nav></div></header>
<main id="main">{main}</main><footer><div class="container footer-inner"><div><strong>ΔMARS Lab</strong><p>Electrical and Computer Engineering<br>Oakland University · Rochester, Michigan</p></div><div><a href="mailto:dantonio@oakland.edu">dantonio@oakland.edu</a><br><a href="{prefix}#hero">Back to top ↑</a></div></div></footer><script src="assets/js/lab.js?v=20261014"></script></body></html>'''

def heading(number,kicker,title,description=''):
    return f'<div class="section-intro"><span class="eyebrow">{number} / {kicker}</span><h2>{title}</h2>'+ (f'<p class="section-description">{description}</p>' if description else '')+'</div>'

def media(label,detail='Experimental media to be added'):
    return f'<div class="media-slot"><span class="media-cross" aria-hidden="true">＋</span><span>{e(label)}</span><small>{e(detail)}</small></div>'

hero=f'''<section id="hero" class="lab-hero"><div class="container hero-grid"><div><span class="eyebrow">Oakland University · Electrical and Computer Engineering</span><p class="hero-lab">ΔMARS LAB</p><h1>Robots That Cooperate,<br><span>Manipulate, and Interact.</span></h1><p class="hero-support">{e(c['supporting_line'])}</p><p class="hero-description">{e(c['intro'])}</p><div class="hero-links"><a class="lab-button" href="#research">Explore Our Research <span aria-hidden="true">→</span></a><a class="text-link" href="#projects">Discover Our Projects <span aria-hidden="true">↗</span></a></div></div><figure class="hero-media"><img class="hero-experiment" src="assets/img/hitches.gif" width="338" height="190" alt="Aerial robots manipulating cables around a cylindrical object during a laboratory experiment."><figcaption class="media-caption">Cable interlacing and cooperative aerial manipulation</figcaption></figure></div><div class="container research-path"><span>Cooperative robotics</span><span aria-hidden="true">·</span><span>Physical interaction</span><span aria-hidden="true">·</span><span>Autonomous manipulation</span></div></section>'''
about=f'''<section id="about" class="content-section"><div class="container">{heading('01','About the lab','Robots that act on the world.')}<div class="about-grid"><div>{paragraphs(c['overview'])}<p class="name-note">The symbol Δ (delta) represents incremental advances in robotic autonomy, physical interaction, and coordination that enable the development of increasingly capable multi-agent robotic systems.</p></div><div class="statement-panel"><h3>Mission</h3>{paragraphs(c['mission'])}<h3>Vision</h3>{paragraphs(c['vision'])}</div></div><div class="principle-grid">{''.join(f'<article><span class="eyebrow">0{i+1}</span><h3>{e(p[0])}</h3><p>{e(p[1])}</p></article>' for i,p in enumerate(c['principles']))}</div></div></section>'''
research_cards=''
for i,r in enumerate(c['research']):
    research_cards+=f'''<article class="research-card">{media(r['title'],'Research visualization reserved')}<div class="card-body"><span class="eyebrow">Theme 0{i+1}</span><h3>{e(r['title'])}</h3><p>{e(r['short'])}</p><details><summary>Research questions and approach</summary>{paragraphs(r['detail'])}<h4>Questions we study</h4>{list_html(r['questions'])}<h4>Potential applications</h4><p>{e(', '.join(r['applications']))}</p><p class="small-note">Connected to: {e(', '.join(r['connections']))}.</p></details></div></article>'''
research=f'<section id="research" class="content-section wash"><div class="container"><div class="research-grid">{research_cards}</div></div></section>'
projects_cards=''.join(f'''<article class="project-card">{media(p['subtitle'])}<div class="card-body"><span class="status">{e(p['status'])}</span><h3><a href="project-{p['id']}.html">{e(p['title'])}</a></h3><p>{e(p['brief'])}</p><a class="text-link" href="project-{p['id']}.html">Explore project <span aria-hidden="true">→</span></a></div></article>''' for p in c['projects'])
projects=f'<section id="projects" class="content-section"><div class="container">{heading("03","Projects","Specific questions. Physical systems.","Project concepts and verified research records, with the current evidence stated for each.")}<div class="projects-grid">{projects_cards}</div></div></section>'
pub=c['publications'][0]
pubhtml=''
for item in c['publications']:
    uid=item['id']
    thumbnail=(f'<img src="{e(item["image"])}" alt="{e(item.get("image_alt", "Publication experimental image"))}" loading="lazy">' if item.get('image') else '<div class="publication-image-placeholder"><span aria-hidden="true">＋</span><small>Paper image to be added</small></div>')
    license_link=(f' · <a href="{e(item["image_license"])}">{e(item.get("image_license_label", "CC BY-NC-SA 4.0"))}</a>' if item.get('image_license') else '')
    credit=(f'<p class="publication-image-credit"><a href="{e(item.get("image_source",item["source"]))}">{e(item["image_credit"])}</a>{license_link}</p>' if item.get('image_credit') else '')
    page_info=(f", pp. {e(item['pages'])}" if item.get('pages') else '')
    issue_info=(f", vol. {e(item['volume'])}" if item.get('volume') else '')+(f", no. {e(item['number'])}" if item.get('number') else '')
    badges={'Journal article':'Journal Article','Conference paper':'Proceedings Article','Preprint':'Preprint','Thesis':'Thesis','Presentation':'Presentation'}
    tags=''.join(f'<button class="publication-tag" type="button" data-topic="{e(topic)}">{e(topic.lower())}</button>' for topic in item['topics'])
    links=''
    for key,label,icon in [('paper','Paper','bi-file-earmark-text'),('video','Video','bi-youtube'),('code','Code','bi-github'),('doi','DOI','bi-link-45deg')]:
        if item.get(key):
            url=item[key] if key!='doi' or item[key].startswith('https://') else 'https://doi.org/'+item[key]
            links+=f'<a href="{e(url)}" class="publication-resource" aria-label="{label}: {e(item["title"])}" title="{label}"><i class="bi {icon}" aria-hidden="true"></i><span>{label}</span></a>'
    if item.get('project'):
        links+=f'<a href="project-{e(item["project"])}.html" class="publication-resource" aria-label="Project: {e(item["title"])}" title="Project"><i class="bi bi-box-arrow-up-right" aria-hidden="true"></i><span>Project</span></a>'
    pubhtml+=f"""<article class="publication publication-row" data-year="{item['year']}" data-type="{e(item['type'])}" data-topics="{e('|'.join(item['topics']))}"><div class="publication-thumbnail">{thumbnail}{credit}</div><div class="publication-content"><p class="publication-authors">{e(item['authors'])}</p><h3 class="publication-title">{e(item['title'])} <span class="publication-badge">{e(badges.get(item['type'],item['type']))}</span></h3><p class="publication-venue">In: {e(item['venue'])}{issue_info}, {item['year']}{page_info}.</p><div class="publication-meta"><button type="button" class="publication-disclosure" aria-expanded="false" aria-controls="abstract-{uid}">Abstract</button><span class="meta-separator" aria-hidden="true">|</span><button type="button" class="publication-disclosure" aria-expanded="false" aria-controls="bibtex-{uid}">BibTeX</button><span class="meta-separator" aria-hidden="true">|</span><span class="publication-tags"><span>Tags:</span> {tags}</span><span class="meta-separator" aria-hidden="true">|</span><span class="publication-resources"><span>Links:</span> {links}</span></div><div id="abstract-{uid}" class="publication-panel" hidden><h4>Abstract summary</h4><p>{e(item.get('abstract',item['summary']))}</p></div><div id="bibtex-{uid}" class="publication-panel" hidden><h4>BibTeX</h4><pre><code>{e(item['bibtex'])}</code></pre></div></div></article>"""
year_options=''.join(f'<option>{year}</option>' for year in sorted({item['year'] for item in c['publications']},reverse=True))
topic_options=''.join(f'<option>{e(topic)}</option>' for topic in sorted({topic for item in c['publications'] for topic in item['topics']}))
filters=f"""<div class="filters" aria-label="Publication filters"><label>Year<select id="filter-year"><option value="all">All years</option>{year_options}</select></label><label>Type<select id="filter-type"><option value="all">All types</option><option>Journal article</option><option>Conference paper</option><option>Preprint</option><option>Thesis</option><option>Presentation</option></select></label><label>Topic<select id="filter-topic"><option value="all">All topics</option>{topic_options}</select></label><button id="reset-filters" type="button">Reset filters</button></div><p id="publication-count" class="small-note" role="status" aria-live="polite">{len(c['publications'])} publications shown</p>"""
publications=f"""<section id="publications" class="content-section"><div class="container">{heading('04','Publications','Publications.', 'Explore our research publications by year, publication type, and topic.')}{filters}<div id="publication-list" class="is-expanded" tabindex="0" role="region" aria-label="Research papers">{pubhtml}</div><p id="publication-empty" class="empty-state" hidden>No publications match these filters.</p></div></section>"""
student_profiles=''
member_groups=['PhD Students','Master’s Students','Undergraduate Researchers']
for group in member_groups:
    members=[member for member in c.get('members',[]) if member['group']==group]
    if not members: continue

    for member in members:
        portrait=(f'<div><img class="member-portrait" src="{e(member["image"])}" alt="{e(member.get("image_alt",member["name"]))}" loading="lazy"></div>' if member.get('image') else '')
        education=''.join(f'<li><strong>{e(entry["degree"])} · {e(entry["year"])}</strong><span>Field: {e(entry["field"])}</span></li>' for entry in member.get('education',[]))
        research_focus=member.get('research_focus',[])
        if isinstance(research_focus,str): research_focus=[research_focus]
        details=('<p class="member-research-focus"><strong>Research focus:</strong> '+' · '.join(e(topic) for topic in research_focus)+'</p>' if research_focus else '')
        if education: details+=f'<h5 class="member-education-heading">Education</h5><ul class="member-education">{education}</ul>'
        if member.get('thesis'): details+=f'<p class="member-thesis"><strong>Thesis:</strong> {e(member["thesis"])}</p>'
        if member.get('award'): details+=f'<p class="member-award"><strong>Distinction:</strong> {e(member["award"])}</p>'
        layout='' if portrait else ' student-profile-text'
        student_profiles+=f'<article class="student-profile{layout}" id="{e(member["id"])}">{portrait}<div><span class="eyebrow member-group-label">{e(member["group"])}</span><h3 class="member-name">{e(member["name"])}</h3><p class="student-role">{e(member["position"])}</p>{details}</div></article>'

people=f'''<section id="people" class="content-section"><div class="container">{heading('05','People','Meet the lab.')}<article class="pi-grid"><div><img class="pi-portrait" src="assets/img/diego-dantonio.jpg" width="270" height="270" alt="Dr. Diego S. D’Antonio holding an aerial robot in a robotics laboratory." loading="lazy"><p class="eyebrow portrait-caption">Principal Investigator</p></div><div><h3 class="pi-name">Dr. Diego S. D’Antonio</h3><p class="pi-role">Assistant Professor · Electrical and Computer Engineering<br>Director, ΔMARS Lab · Oakland University</p>{paragraphs(c['bio'])}<a class="text-link" href="mailto:dantonio@oakland.edu">Contact Dr. D’Antonio ↗</a></div></article><div class="student-profiles">{student_profiles}</div><div class="member-groups">{''.join(f'<div><h4>{label}</h4><p>Profiles to be added.</p></div>' for label in ["Alumni","Collaborators"])}</div><div class="culture"><h3>How We Work</h3><p>{e(c['culture'])}</p></div></div></section>'''
news_items=''
for item in c.get('news',[]):
    caption=e(item.get('image_caption',''))
    if item.get('image_source'):
        caption=f'<a href="{e(item["image_source"])}">{caption}</a>'
    if item.get('image_license'):
        caption+=f' · <a href="{e(item["image_license"])}">CC BY-NC-ND 4.0</a>'
    news_link=(f'<a class="text-link" href="{e(item["url"])}">{e(item.get("link_label","Competition details"))} ↗</a>' if item.get("url") else "")
    news_items+=f"""<article class="news-card"><figure><img src="{e(item['image'])}" alt="{e(item['image_alt'])}" loading="lazy" width="{item.get('image_width',800)}" height="{item.get('image_height',402)}"><figcaption>{caption}</figcaption></figure><div class="news-copy"><p class="eyebrow">{e(item['label'])}</p><h3>{e(item['title'])}</h3><p>{e(item['summary'])}</p>{news_link}</div></article>"""
news=f'''<section id="news" class="content-section wash"><div class="container">{heading('06','News','Lab updates.')}{news_items or '<div class="empty-state"><p>Announcements will appear here.</p></div>'}</div></section>'''

join=f'''<section id="join" class="content-section join-section"><div class="container">{heading('07','Join us','Bring your questions. Build your research.')}<div class="join-grid"><div><p>We welcome inquiries from PhD and master’s students, undergraduate researchers, and potential collaborators interested in autonomous physical interaction.</p><p>Research may involve mathematical modeling, algorithm development, robot design, simulation, hardware development, experimental testing, and scientific writing. Publication goals depend on the project and its results.</p><p>Relevant backgrounds include control theory, applied mathematics, Python or C++, ROS 2, computer vision, embedded systems, mechanical design, electronics, optimization, and state estimation. You do not need all these skills. Technical curiosity, persistence, and a willingness to learn matter.</p></div><div class="inquiry-panel"><h3>Start a conversation</h3><p>Email Dr. D’Antonio with:</p><ol><li>A brief introduction and your academic background.</li><li>Your research interests and what draws you to the lab.</li><li>A CV or résumé.</li><li>Relevant projects, code, or publications, if available.</li></ol><a class="lab-button" href="mailto:dantonio@oakland.edu?subject=Research%20inquiry%20%E2%80%94%20%CE%94MARS%20Lab">Send a research inquiry ↗</a><p class="small-note">Contact the director to discuss current opportunities. Funded positions are not advertised unless confirmed.</p></div></div></div></section>'''
contact=f'''<section id="contact" class="content-section"><div class="container">{heading('08','Contact','Let’s connect.')}<div class="contact-grid"><div><h3>ΔMARS Lab</h3><p>Department of Electrical and Computer Engineering<br>Oakland University<br>Rochester, Michigan, USA</p><p><strong>Laboratory</strong><br>Engineering Center, Room 450</p></div><div><h3>Research inquiries</h3><p>Dr. Diego S. D’Antonio<br>Laboratory Director</p><a class="contact-email" href="mailto:dantonio@oakland.edu">dantonio@oakland.edu</a></div><div><h3>University links</h3><p><a class="text-link" href="https://www.oakland.edu/">Oakland University ↗</a></p><p><a class="text-link" href="https://www.oakland.edu/secs/departments/ece/">Electrical and Computer Engineering ↗</a></p><p class="small-note">Google Scholar, GitHub, LinkedIn, and lab collaboration profiles will be linked after confirmation.</p></div></div></div></section>'''
focus=c['featured_focus']
featured_focus=f"""<section id="research" class="content-section featured-focus"><div class="container"><span class="eyebrow">Distinctive research focus</span><h2>{e(focus['title'])}</h2><p class="focus-subtitle">{e(focus['subtitle'])}</p><div class="focus-grid"><div>{''.join('<p>'+e(t)+'</p>' for t in focus['paragraphs'])}<p><strong>Potential applications:</strong> {e(', '.join(focus['applications']))}.</p><a class="text-link" href="project-cable-interlacing.html">Explore cable interlacing →</a></div><div class="scientific-question"><h3>A connecting scientific question</h3><p>{e(c['question'])}</p><p class="small-note">Cables and knots can establish connections, distribute forces, secure payloads, and create mechanical constraints.</p></div></div></div></section>"""
Path('index.html').write_text(shell(c['headline'],hero+about+featured_focus+projects+publications+people+news+join+contact,True))
for p in c['projects']:
    theme_names=[r['title'] for r in c['research'] if r['id'] in p['themes']]
    main=f'''<section id="hero" class="project-hero"><div class="container"><a class="text-link" href="index.html#projects">← All projects</a><p class="eyebrow">{e(p['status'])}</p><h1>{e(p['title'])}</h1><p class="hero-description">{e(p['subtitle'])}</p></div></section><section class="content-section"><div class="container project-content">{media('Project experiment or illustration','Author-approved media to be added')}<div class="project-prose">{paragraphs(p['extended'])}<h2>Scientific challenge</h2><p>{e(p['challenge'])}</p><h2>Research approach</h2><p>{e(p['approach'])}</p><h2>Contributions and evidence</h2><p>{e(p['contributions'])}</p><h2>Related research themes</h2><p>{e(', '.join(theme_names))}</p><h2>Related publications</h2><p>{e(p['related'])}</p>{'<a class="text-link" href="https://arxiv.org/abs/2610.13665">Read the author-posted preprint ↗</a>' if p['id']=='sliding-transport' else ''}<h2>Affiliations and support</h2><p>{e(p['institutions'])}</p><p>{e(p['funding'])}</p></div></div></section>'''
    Path(f"project-{p['id']}.html").write_text(shell(p['title'],main))

# Requested A–H deliverable. Editorial notes are kept outside the public pages.
doc=['# ΔMARS Laboratory — Content, Positioning, and Website Blueprint\n\nPrepared October 12, 2026. This document separates proposed website copy from editorial verification notes. The supplied master prompt is the source for lab identity, mission, interests, facilities, contact, and project concepts. Research themes describe an agenda; they do not assert completed results.\n',
'''## Part A — Laboratory positioning

**Identity:** ΔMARS Lab, Department of Electrical and Computer Engineering, Oakland University, Rochester, Michigan. Director: Dr. Diego S. D’Antonio. Scientific focus: cooperative robotics, physical interaction, and autonomous manipulation. Cables, knots, and flexible structures are a distinctive central investigation within this broader mission.

**Recommended headline:** Robots That Cooperate, Manipulate, and Interact.

**Positioning:** Cooperative Robotics, Physical Interaction, and Autonomous Manipulation.

This headline states three connected research objectives without confining the laboratory to a particular platform or mechanism. Cable manipulation and robotic knotting provide a distinctive focus within an agenda spanning aerial vehicles, blimps, ground robots, and heterogeneous teams. The headline describes the research direction, rather than asserting that every capability is already demonstrated.

**Short supporting line:** Advancing autonomous robotics through cooperative coordination, physical interaction, and intelligent manipulation.

**Interconnected identity:** Cooperative Robotics · Physical Interaction · Autonomous Manipulation.

**Overarching question:** How can autonomous multi-robot systems coordinate their actions and leverage contact dynamics and mechanical interactions with deformable linear objects—including cable tension, friction, and topological constraints—to enable complex manipulation capabilities beyond those achievable by individual robots?

**Distinguishing scientific questions:** How can a robot create a useful attachment? How do changing contacts alter the dynamics? What must a team coordinate besides motion? What measurements reveal an interaction state? Frame these as research questions, then connect individual contributions to verified papers and experiments.

**Name:** The symbol Δ (delta) represents incremental advances in robotic autonomy, physical interaction, and coordination that enable the development of increasingly capable multi-agent robotic systems. An [author-posted manuscript](https://arxiv.org/html/2610.13665v1) identifies the full lab name as “Distributed Multi-Agent Robotic Systems.” This is strong primary evidence; confirm the intended official wordmark and expansion before adding the full name to the public site. Preserve ΔMARS as one word.

Because the brief did not explicitly provide the official expansion, the following are suggestions requiring approval, not definitions: (1) Multi-Agent Robotic Systems; (2) Manipulation and Autonomous Robotic Systems; (3) Modeling and Autonomy for Robotic Systems. Prefer the existing manuscript wording if confirmed, rather than introducing a new expansion.

**Mission**
'''+c['mission']+'\n\n**Vision**\n'+c['vision']+'\n',
'## Part B — Complete website copy\n\n### 01 / About the Lab\n\n**Homepage introduction**\n\n'+c['intro']+'\n\n**Laboratory overview**\n\n'+c['overview']+'\n\n**Mission and vision:** Use the statements in Part A.\n\n**Research philosophy**\n\n'+ '\n\n'.join('**'+p[0]+'** — '+p[1] for p in c['principles'])+'\n\n**Academic affiliation**\n\nΔMARS Lab is part of the Department of Electrical and Computer Engineering at Oakland University. The laboratory is directed by Dr. Diego S. D’Antonio, Assistant Professor. Earlier research and coauthored publications retain their original institutional attribution; authorship does not establish that every result was produced at Oakland.\n\n### 02 / Research\n\n**Section introduction:** One agenda. Five connected themes. We connect cooperative robotics, physical interaction, and autonomous manipulation, with cables and robotic knotting as a distinctive focus.\n']
for r in c['research']:
    doc.append(f"#### {r['full_title']}\n\n**Card title:** {r['title']}\n\n**Card description:** {r['short']}\n\n{r['detail']}\n\n**Representative questions**\n\n"+'\n'.join('- '+q for q in r['questions'])+f"\n\n**Potential applications:** {', '.join(r['applications'])}. These are motivating use cases, not deployed capabilities.\n\n**Suggested visual:** {r['visual']}\n\n**Connections:** {', '.join(r['connections'])}.\n")
doc.append('#### Featured Research: '+c['featured_focus']['title']+'\n\n**'+c['featured_focus']['subtitle']+'**\n\n'+'\n\n'.join(c['featured_focus']['paragraphs'])+'\n\n**Potential applications:** '+', '.join(c['featured_focus']['applications'])+'.\n')
doc.append('### 03 / Projects\n\n**Section introduction:** Specific questions. Physical systems. Explore project concepts and verified research records, with the current evidence stated for each.\n')
for p in c['projects']:
    doc.append(f"#### {p['title']}\n\n**Subtitle:** {p['subtitle']}\n\n**Status:** {p['status']}\n\n**Brief description**\n\n{p['brief']}\n\n**Extended description**\n\n{p['extended']}\n\n"+'\n\n'.join('**'+label+'** — '+p[key] for label,key in [('Scientific challenge','challenge'),('Research approach','approach'),('Expected or demonstrated contributions','contributions'),('Photograph','photo'),('Experimental video','video'),('Animation','animation'),('Related publications','related'),('Institutions','institutions'),('Funding acknowledgment','funding')])+"\n\n**Themes:** "+', '.join(r['title'] for r in c['research'] if r['id'] in p['themes'])+'.\n')
doc.append('''### 04 / Publications

**Section introduction:** Research, with its evidence. Explore scientific contributions organized by year, topic, and publication type. Original authorship, venue, and project context accompany each verified entry.

**Categories:** Journal articles; conference papers; preprints; theses; selected presentations. Empty categories remain valid filters and display an honest empty state.

**Metadata contract:** Title, ordered authors, venue, year, type, research topics, DOI, paper URL, video URL, code URL, project URL, BibTeX, provenance source, publication status, and outstanding verification fields. Missing URLs are null; do not create empty anchors. An arXiv DOI is not a publisher DOI, and a presentation of a journal paper does not create a conference-paper record.

**Verified initial record**

- Title: Cooperative Aerial Transportation of a Payload with a Sliding Cable Attachment.
- Authors: Sebastian Tilaguy Lezama; Diego S. D’Antonio.
- Venue/type: arXiv preprint, arXiv:2610.13665. Peer-reviewed venue not established by the checked record.
- Year: 2026. Submission: October 9, 2026, as stated on the primary record.
- Paper: [Author-posted preprint](https://arxiv.org/abs/2610.13665).
- DOI: the arXiv record marks registration as pending; omit a DOI link until it resolves.
- Video/code: not verified; omit buttons.
- Project: project-sliding-transport.html.
- Main contribution summary: studies cooperative payload transport with a sliding cable attachment; the preprint reports experiments.

**BibTeX**

```bibtex
'''+pub['bibtex']+'''
```

**Cable-interlacing record:** “From Hitch to Lift: Autonomous Cable Interlacing by Multi-UAV Teams for Aerial Grasping and Transportation.” The author supplied the 2026 IEEE Transactions on Robotics citation, ordered authors, pages 1–16, and DOI 10.1109/TRO.2026.3677011. These are now included with the supplied experimental GIF. Publisher access was unavailable, so metadata provenance remains the author-supplied record.

**Publication layout:** Horizontal rows for all supplied papers, with the sliding-cable preprint retained first. Each row provides a paper-specific thumbnail, ordered authors, title and publication-type badge, venue/year/pages, abstract summary, BibTeX, topic tags, and populated paper/video/DOI/project links. Images and citations retain their own source context.

**Venue taxonomy:** Support IEEE Transactions on Robotics, IEEE Robotics and Automation Letters, ICRA, IROS, RSS, and Latin American Robotics Symposium as metadata values when verified records exist. Do not display logos or counts that imply publications in each venue.

**Filters:** Year, topic, and type combine using AND. Reset restores all records. Announce result counts and show a no-results message. Use a readable list, not a dense bibliography table on mobile.

### 05 / People

**Principal investigator**

Dr. Diego S. D’Antonio · Assistant Professor · Department of Electrical and Computer Engineering · Oakland University · Director, ΔMARS Lab.

'''+c['bio']+'''

**Research interests:** Aerial robotics; autonomous manipulation; cooperative robotic systems; dynamics and control; cable-mediated physical interaction; multi-robot transportation.

**Member profile structure:** Name, actual photograph and alt text, academic position, research interests, current project links, 40–80 word biography, and optional email, personal website, Google Scholar, GitHub, LinkedIn. Use only consented contact/profile information. Never use stock faces as actual members.

**PhD Student — Sebastian Tilaguy-Lezama**

Ph.D. in Electrical Engineering — 1st year. Research field: Aerial Cable Interaction.

M.Sc. in Control Engineering — 2021. Field: Precision agriculture with UGVs.

Electronic Engineering — 2017. Field: Power electronics and control.

Education and research focus supplied by the user. Portrait: assets/img/sebastian.png, supplied by the user.

**Groups:** Principal Investigator; PhD Students; Master’s Students; Undergraduate Researchers; Alumni; Collaborators. Keep unconfirmed groups as “Profiles to be added.” Do not infer student membership from paper coauthorship.

**Laboratory culture**

'''+c['culture']+'''

### 06 / News

**Section introduction:** Lab updates. Follow publications, research demonstrations, conferences, and laboratory milestones.

The live draft has no dated entries because announcement dates and event completion are not confirmed. The following 40–80 word summaries are editorial drafts held outside the public site.

**Transactions on Robotics — hold pending primary publication verification and announcement date**

Research on autonomous cable interlacing examines how aerial robot teams can use flexible cables to establish an attachment for object handling. The work connects coordinated motion with contact and friction mechanics. Once the publisher record is confirmed, this update will link the paper, identify all authors, and explain the demonstrated contribution with author-approved experimental media.

**IROS 2026 — use only if a presentation is confirmed; date and tense pending**

Dr. Diego S. D’Antonio is scheduled to present research on multi-UAV cable manipulation and aerial transportation at IROS 2026. The presentation examines how coordinated cable interactions can support object securement and handling. Add the confirmed session, presentation date, and paper link before posting. Change to past tense only after the presentation has occurred and is confirmed.

**Michigan Space Grant Consortium — project-specific support pending verification**

The laboratory is developing research on cooperative blimp systems for studying selected aspects of object capture and transportation. The project explores coordinated motion and cable-mediated interaction using terrestrial experimental platforms. Confirm the award and approved acknowledgment before announcing support. Each demonstration will state its emulation scope, including the differences between buoyant flight and orbital microgravity dynamics.

**LARS-LARC 2026 — participation, contribution, and date pending**

A proposed laboratory update will describe verified participation in LARS-LARC activities related to aerial robotics and autonomous systems. Once confirmed, the announcement will identify the presenters, contribution titles, and activity dates, then connect the work to the laboratory’s research themes. Include a paper or program link where available; do not describe planned participation as a completed achievement.

**News schema:** Title, summary, category, publication date, event date if relevant, event state (planned/completed), source URL, project/publication link, optional actual photograph, publish flag. Sort published entries by announcement date, newest first; never derive an event date from a publication year.

### 07 / Join Us

**Headline:** Bring your questions. Build your research.

We welcome inquiries from PhD and master’s students, undergraduate researchers, and potential collaborators interested in autonomous physical interaction. Research may involve mathematical modeling, algorithm development, robot design, simulation, hardware development, experimental testing, and scientific writing. Publication goals depend on the project and its results.

Relevant backgrounds include robotics, control theory, applied mathematics, Python or C++, ROS 2, computer vision, embedded systems, mechanical design, electronics, optimization, state estimation, and experimental robotics. You do not need all these skills. Technical curiosity, persistence, and a willingness to learn matter.

**Call to action:** Start a conversation. Email Dr. D’Antonio at dantonio@oakland.edu with a brief introduction, your academic background, your research interests, a CV or résumé, and relevant projects, code, or publications if available. Contact the director to discuss current opportunities. Funded positions are not advertised unless confirmed.

**Audience paths:** Graduate students discuss research fit and degree plans; undergraduate researchers describe coursework and interests; collaborators describe the scientific question and potential connection. Add verified admissions links separately from lab inquiries.

### 08 / Contact

ΔMARS Lab  
Department of Electrical and Computer Engineering  
Oakland University  
Rochester, Michigan, USA  
Laboratory: Engineering Center, Room 450  
Director: Dr. Diego S. D’Antonio  
Email: [dantonio@oakland.edu](mailto:dantonio@oakland.edu)

**Institutional links:** [Oakland University](https://www.oakland.edu/) · [Electrical and Computer Engineering](https://www.oakland.edu/secs/departments/ece/).

**Reserved external profiles:** Google Scholar, GitHub, LinkedIn, and laboratory collaboration pages. Display only after official account URLs are confirmed. Lab room is user-supplied; do not substitute the department office room from the institutional page.
''')
Path('WEBSITE_BLUEPRINT.md').write_text('\n'.join(doc))
Path('WEBSITE_BLUEPRINT.md').write_text(Path('WEBSITE_BLUEPRINT.md').read_text()+'\n'+Path('content/blueprint-appendix.md').read_text())

with Path('WEBSITE_BLUEPRINT.md').open('a') as document:
    document.write('\n## Current publication records\n\nThe original sliding-cable paper remains first. Additional citations were supplied by the author. Images come from author-posted manuscripts, matching original-lab publication thumbnails, author-provided footage, and paper-linked demonstration videos. Customizable-ModQuad links to an author-uploaded manuscript because its arXiv identifier remains unconfirmed.\n')
    for record in c['publications']:
        document.write('\n### '+record['title']+'\n\n'+record['authors']+'\n\n'+record['venue']+', '+str(record['year'])+'.\n\n[Paper]('+record['paper']+')\n\n```bibtex\n'+record['bibtex']+'\n```\n')

with Path('WEBSITE_BLUEPRINT.md').open('a') as document:
    document.write('\n## Current lab members\n\n')
    for member in c.get('members',[]):
        document.write('### '+member['name']+'\n\n'+member['group']+' · '+member['position']+'\n\n')
        if member.get('research_focus'): document.write('Research focus: '+member['research_focus']+'\n\n')
        if member.get('thesis'): document.write('Thesis: '+member['thesis']+'\n\n')
        if member.get('award'): document.write('Distinction: '+member['award']+'\n\n')
