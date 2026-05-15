import streamlit as st
import os, json

# ══════════════════════════════════════════════════════════════════════════
# SETUP — birinchi ishga tushganda korgazmalar/ papkasini yaratadi
# ══════════════════════════════════════════════════════════════════════════
ROOT = "korgazmalar"

def setup():
    """Asosiy papka strukturasini yaratadi (faqat bir marta)"""
    sinflar  = ['05-sinf','06-sinf','07-sinf','08-sinf','09-sinf','10-sinf','11-sinf']
    choraklar = ['1-chorak','2-chorak','3-chorak','4-chorak']
    for sinf in sinflar:
        for chorak in choraklar:
            path = os.path.join(ROOT, sinf, chorak)
            os.makedirs(path, exist_ok=True)
            # .gitkeep — GitHub bo'sh papkani saqlashi uchun
            gk = os.path.join(path, '.gitkeep')
            if not os.path.exists(gk):
                open(gk, 'w').close()

if not os.path.exists(ROOT):
    setup()

# ══════════════════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Informatika Lab | InfoSchoolUz",
    page_icon="🖥️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html, body, [data-testid="stAppViewContainer"] {
    background: #f8fafc !important;
    font-family: 'Inter', sans-serif;
}
[data-testid="stHeader"],[data-testid="stDecoration"]{display:none}

.main-header {
    background: #fff;
    border-bottom: 2px solid #e2e8f0;
    padding: 28px 0 20px;
    text-align: center;
    margin-bottom: 28px;
}
.main-header h1 { font-size:1.9rem;font-weight:800;color:#1e293b;margin:0 0 4px }
.main-header p  { color:#64748b;font-size:.88rem;margin:0 }
.author-badge {
    display:inline-flex;align-items:center;gap:8px;
    background:#f1f5f9;border:1px solid #e2e8f0;border-radius:20px;
    padding:5px 16px;font-size:.8rem;color:#475569;margin-top:10px;font-weight:600
}
.author-badge span { color:#3b82f6 }

.breadcrumb {
    display:flex;align-items:center;gap:8px;
    padding:4px 0 18px;font-size:.85rem;flex-wrap:wrap
}
.bc-item { color:#3b82f6;font-weight:600 }
.bc-sep  { color:#cbd5e1 }
.bc-cur  { color:#1e293b;font-weight:700 }

.section-title {
    font-size:1.1rem;font-weight:700;color:#1e293b;
    margin-bottom:18px;display:flex;align-items:center;gap:8px
}
.count-badge {
    background:#f1f5f9;color:#64748b;border-radius:20px;
    padding:3px 12px;font-size:.78rem;font-weight:600
}

.sinf-card {
    background:#fff;border:2px solid #e2e8f0;border-radius:18px;
    padding:24px 16px;text-align:center;
    box-shadow:0 1px 4px rgba(0,0,0,.04);transition:all .2s
}
.sinf-card:hover {
    border-color:var(--c);
    box-shadow:0 6px 24px rgba(0,0,0,.1);transform:translateY(-3px)
}
.sinf-num   { font-size:2.4rem;font-weight:800;color:var(--c);margin-bottom:4px }
.sinf-label { font-size:.85rem;color:#64748b;font-weight:600 }
.sinf-count { font-size:.72rem;color:#94a3b8;margin-top:5px }

.chorak-card {
    background:#fff;border:2px solid #e2e8f0;border-radius:16px;
    padding:22px 16px;text-align:center;
    box-shadow:0 1px 4px rgba(0,0,0,.04);transition:all .2s
}
.chorak-card:hover {
    border-color:var(--c);
    box-shadow:0 6px 20px rgba(0,0,0,.09);transform:translateY(-2px)
}
.chorak-num    { font-size:2.2rem;margin-bottom:8px }
.chorak-name   { font-size:1rem;font-weight:700;color:#1e293b;margin-bottom:4px }
.chorak-months { font-size:.75rem;color:#94a3b8 }
.chorak-count  {
    display:inline-block;margin-top:10px;border-radius:20px;
    padding:3px 14px;font-size:.75rem;font-weight:700;
    background:var(--cl);color:var(--c)
}

.korgazma-card {
    background:#fff;border:1.5px solid #e2e8f0;border-radius:14px;
    padding:20px 16px;text-align:center;
    box-shadow:0 1px 4px rgba(0,0,0,.04);transition:all .2s
}
.korgazma-card:hover {
    border-color:var(--c);
    box-shadow:0 6px 22px rgba(0,0,0,.1);transform:translateY(-2px)
}
.k-icon  { font-size:2.4rem;margin-bottom:10px }
.k-title { font-size:.92rem;font-weight:700;color:#1e293b;margin-bottom:5px }
.k-desc  { font-size:.76rem;color:#64748b;line-height:1.5;margin-bottom:10px }
.k-badge {
    display:inline-block;border-radius:20px;
    padding:3px 12px;font-size:.72rem;font-weight:700;
    background:var(--cl);color:var(--c)
}

.empty-state { text-align:center;padding:60px 20px;color:#94a3b8 }
.empty-state .e-icon { font-size:3rem;margin-bottom:12px }
.empty-state h3 { font-size:1.1rem;color:#64748b;margin-bottom:6px }
.empty-state p  { font-size:.82rem }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# META
# ══════════════════════════════════════════════════════════════════════════
SINF_META = {
    '05-sinf': {'color':'#3b82f6','light':'#eff6ff','label':'5-sinf'},
    '06-sinf': {'color':'#10b981','light':'#f0fdf4','label':'6-sinf'},
    '07-sinf': {'color':'#f59e0b','light':'#fffbeb','label':'7-sinf'},
    '08-sinf': {'color':'#ef4444','light':'#fef2f2','label':'8-sinf'},
    '09-sinf': {'color':'#a855f7','light':'#faf5ff','label':'9-sinf'},
    '10-sinf': {'color':'#06b6d4','light':'#ecfeff','label':'10-sinf'},
    '11-sinf': {'color':'#f97316','light':'#fff7ed','label':'11-sinf'},
}

CHORAK_META = {
    '1-chorak': {'icon':'🍂','name':'1-chorak','months':'Sentyabr — Oktyabr','color':'#f59e0b','light':'#fffbeb'},
    '2-chorak': {'icon':'❄️','name':'2-chorak','months':'Noyabr — Dekabr',   'color':'#3b82f6','light':'#eff6ff'},
    '3-chorak': {'icon':'🌸','name':'3-chorak','months':'Yanvar — Mart',      'color':'#10b981','light':'#f0fdf4'},
    '4-chorak': {'icon':'☀️','name':'4-chorak','months':'Aprel — May',        'color':'#f97316','light':'#fff7ed'},
}

ALL_SINFLAR = ['05-sinf','06-sinf','07-sinf','08-sinf','09-sinf','10-sinf','11-sinf']

# ══════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════
def count_korgazmalar(path):
    if not os.path.isdir(path): return 0
    return sum(
        1 for x in os.listdir(path)
        if os.path.isdir(os.path.join(path, x))
        and os.path.exists(os.path.join(path, x, 'index.html'))
    )

def count_sinf_total(sinf):
    total = 0
    for ch in CHORAK_META:
        total += count_korgazmalar(os.path.join(ROOT, sinf, ch))
    return total

def get_korgazmalar(sinf, chorak):
    path = os.path.join(ROOT, sinf, chorak)
    items = []
    if not os.path.isdir(path): return items
    for name in sorted(os.listdir(path)):
        fp = os.path.join(path, name)
        mp = os.path.join(fp, 'meta.json')
        hp = os.path.join(fp, 'index.html')
        if os.path.isdir(fp) and os.path.exists(mp) and os.path.exists(hp):
            with open(mp, encoding='utf-8') as f:
                meta = json.load(f)
            meta['folder']    = name
            meta['html_path'] = hp
            items.append(meta)
    return items

def go(sinf=None, chorak=None, korgazma=None):
    st.session_state.sinf     = sinf
    st.session_state.chorak   = chorak
    st.session_state.korgazma = korgazma
    st.rerun()

# ══════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════════════════
for k in ['sinf','chorak','korgazma']:
    if k not in st.session_state:
        st.session_state[k] = None

S = st.session_state

# ══════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="main-header">
    <div style="font-size:2rem;margin-bottom:6px">🖥️</div>
    <h1>Informatika fanidan vizual ko'rgazmalar</h1>
    <p>InfoSchoolUz &middot; Urgench &middot; Khorezm</p>
    <div class="author-badge">
        👨‍🏫 Tayyorladi: <span>Azamat Madrimov</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# BREADCRUMB
# ══════════════════════════════════════════════════════════════════════════
bc = '<div class="breadcrumb">'
bc += '<span class="bc-item">🏠 Bosh sahifa</span>'
if S.sinf:
    sm = SINF_META.get(S.sinf, {})
    bc += '<span class="bc-sep">›</span>'
    if S.chorak:
        bc += f'<span class="bc-item">{sm.get("label", S.sinf)}</span>'
        cm = CHORAK_META.get(S.chorak, {})
        bc += '<span class="bc-sep">›</span>'
        if S.korgazma:
            bc += f'<span class="bc-item">{cm.get("name", S.chorak)}</span>'
            bc += '<span class="bc-sep">›</span>'
            bc += f'<span class="bc-cur">{S.korgazma.get("title","")}</span>'
        else:
            bc += f'<span class="bc-cur">{cm.get("name", S.chorak)}</span>'
    else:
        bc += f'<span class="bc-cur">{sm.get("label", S.sinf)}</span>'
bc += '</div>'
st.markdown(bc, unsafe_allow_html=True)

# ── Back button ────────────────────────────────────────────────────────────
if S.korgazma:
    if st.button("← Orqaga"): go(S.sinf, S.chorak)
elif S.chorak:
    if st.button("← Orqaga"): go(S.sinf)
elif S.sinf:
    if st.button("← Orqaga"): go()

# ══════════════════════════════════════════════════════════════════════════
# LEVEL 3 — Ko'rgazma
# ══════════════════════════════════════════════════════════════════════════
if S.korgazma:
    sel = S.korgazma
    st.markdown(
        f'<div class="section-title">{sel["icon"]} {sel["title"]}</div>',
        unsafe_allow_html=True
    )
    with open(sel['html_path'], encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=900, scrolling=True)

# ══════════════════════════════════════════════════════════════════════════
# LEVEL 2 — Chorak ko'rgazmalari
# ══════════════════════════════════════════════════════════════════════════
elif S.chorak:
    sm    = SINF_META.get(S.sinf, {})
    cm    = CHORAK_META.get(S.chorak, {})
    color = sm.get('color', '#3b82f6')
    items = get_korgazmalar(S.sinf, S.chorak)

    st.markdown(f"""
    <div class="section-title">
        {cm.get('icon','')} {cm.get('name', S.chorak)}
        &nbsp;—&nbsp; {sm.get('label', S.sinf)}
        <span class="count-badge">📚 {len(items)} ta ko'rgazma</span>
    </div>""", unsafe_allow_html=True)

    if not items:
        st.markdown(f"""
        <div class="empty-state">
            <div class="e-icon">📂</div>
            <h3>Hozircha ko'rgazmalar yo'q</h3>
            <p><code>{ROOT}/{S.sinf}/{S.chorak}/</code> papkasiga qo'shing</p>
        </div>""", unsafe_allow_html=True)
    else:
        cols = st.columns(3, gap="large")
        for i, item in enumerate(items):
            c  = item.get('color', color)
            cl = c + '18'
            with cols[i % 3]:
                st.markdown(f"""
                <div class="korgazma-card" style="--c:{c};--cl:{cl}">
                    <div class="k-icon">{item['icon']}</div>
                    <div class="k-title">{item['title']}</div>
                    <div class="k-desc">{item.get('description','')}</div>
                    <span class="k-badge">{item.get('sinf','')}</span>
                </div>""", unsafe_allow_html=True)
                if st.button("▶ Ochish",
                             key=f"{S.sinf}_{S.chorak}_{item['folder']}",
                             use_container_width=True):
                    go(S.sinf, S.chorak, item)

# ══════════════════════════════════════════════════════════════════════════
# LEVEL 1 — 4 ta chorak
# ══════════════════════════════════════════════════════════════════════════
elif S.sinf:
    sm    = SINF_META.get(S.sinf, {})
    total = count_sinf_total(S.sinf)

    st.markdown(f"""
    <div class="section-title">
        {sm.get('label', S.sinf)} — Choraklar
        <span class="count-badge">📚 Jami {total} ta ko'rgazma</span>
    </div>""", unsafe_allow_html=True)

    cols = st.columns(4, gap="medium")
    for i, ch in enumerate(['1-chorak','2-chorak','3-chorak','4-chorak']):
        cm  = CHORAK_META[ch]
        cnt = count_korgazmalar(os.path.join(ROOT, S.sinf, ch))
        c   = cm['color']
        cl  = cm['light']
        with cols[i]:
            st.markdown(f"""
            <div class="chorak-card" style="--c:{c};--cl:{cl}">
                <div class="chorak-num">{cm['icon']}</div>
                <div class="chorak-name">{cm['name']}</div>
                <div class="chorak-months">{cm['months']}</div>
                <div class="chorak-count">{cnt} ta ko'rgazma</div>
            </div>""", unsafe_allow_html=True)
            if st.button(
                "▶ Ochish" if cnt > 0 else "+ Qo'shish",
                key=f"{S.sinf}_{ch}",
                use_container_width=True
            ):
                go(S.sinf, ch)

# ══════════════════════════════════════════════════════════════════════════
# LEVEL 0 — 5-11 sinflar
# ══════════════════════════════════════════════════════════════════════════
else:
    total_all = sum(count_sinf_total(s) for s in ALL_SINFLAR)

    st.markdown(f"""
    <div class="section-title">
        🏫 Sinflar
        <span class="count-badge">Jami {total_all} ta ko'rgazma</span>
    </div>""", unsafe_allow_html=True)

    cols = st.columns(4, gap="medium")
    for i, sinf in enumerate(ALL_SINFLAR):
        sm  = SINF_META[sinf]
        c   = sm['color']
        cl  = sm['light']
        cnt = count_sinf_total(sinf)
        with cols[i % 4]:
            st.markdown(f"""
            <div class="sinf-card" style="--c:{c};--cl:{cl}">
                <div class="sinf-num">{sm['label'].replace('-sinf','')}</div>
                <div class="sinf-label">-sinf</div>
                <div class="sinf-count">{cnt} ta ko'rgazma</div>
            </div>""", unsafe_allow_html=True)
            if st.button(
                "▶ Ochish",
                key=f"sinf_{sinf}",
                use_container_width=True
            ):
                go(sinf)
