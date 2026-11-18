import streamlit as st
import pandas as pd
from promoter_scanner import clean_sequence, is_valid, scan_sequence, get_gc_content

st.set_page_config(page_title="Gene Regulatory Element Scanner", page_icon="🧬", layout="centered")

st.markdown("""
<style>
.stApp { background: #f7f8f4; }
[data-testid="stHeader"] { background: rgba(247,248,244,0.85); }
.block-container { padding-top: 2.2rem; padding-bottom: 3rem; max-width: 950px; }
.hero { background: linear-gradient(120deg,#e5efe6,#edf4f5); border: 1px solid #d4e2d6; padding: 1.5rem 1.7rem; border-radius: 20px; margin-bottom: 1.2rem; }
.hero-kicker { color:#557a62; font-size:0.85rem; letter-spacing:0.09em; text-transform:uppercase; font-weight:700; margin-bottom:0.35rem; }
.hero h1 { color:#254c37; font-size:2.15rem; margin:0; line-height:1.2; }
.hero p { color:#52645a; margin:0.6rem 0 0 0; font-size:1rem; }
.section-title { color:#2e5a40; font-size:1.3rem; font-weight:700; margin:1.35rem 0 0.5rem 0; }
div[data-testid="stTextArea"] textarea { background:#ffffff; border:1px solid #cbdccc; border-radius:12px; }
div[data-testid="stButton"] button { background:#477858; color:white; border:0; border-radius:10px; padding:0.55rem 1.25rem; font-weight:600; }
div[data-testid="stButton"] button:hover { background:#355f45; color:white; border:0; }
div[data-testid="stMetric"] { background:#ffffff; border:1px solid #d9e5d9; border-radius:14px; padding:1rem 1.1rem; box-shadow:0 2px 8px rgba(38,74,48,0.04); }
div[data-testid="stMetricLabel"] p { color:#66806d; }
div[data-testid="stMetricValue"] { color:#315b40; }
[data-testid="stDataFrame"] { border:1px solid #d8e3d8; border-radius:12px; overflow:hidden; }
div[data-testid="stDownloadButton"] button { background:#e1eee2; color:#315b40; border:1px solid #bfd5c2; border-radius:10px; font-weight:600; }
div[data-testid="stDownloadButton"] button:hover { background:#cfe3d1; color:#264b35; border:1px solid #bfd5c2; }
hr { border-color:#dbe5db; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="hero-kicker">DNA sequence analysis · Bioinformatics</div>
  <h1>🧬 Gene Regulatory Element Scanner</h1>
  <p>Explore selected promoter-related motifs in a DNA sequence and view their locations and basic sequence statistics.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Enter your DNA sequence")
st.caption("Paste or type a DNA sequence below. Spaces and line breaks are handled automatically.")
sequence = st.text_area("DNA sequence", placeholder="Example: ATGCGCTATAAAAGGCCAATGCGCGC", label_visibility="collapsed", height=140)

if st.button("🔎 Scan sequence", use_container_width=False):
    sequence = clean_sequence(sequence)

    if not is_valid(sequence):
        st.error("Please enter a valid DNA sequence using only A, T, G and C.")
    else:
        results = scan_sequence(sequence)

        st.markdown('<div class="section-title">Sequence overview</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.metric("Sequence length", f"{len(sequence)} bp")
        col2.metric("GC content", f"{get_gc_content(sequence)}%")

        st.markdown('<div class="section-title">Motif results</div>', unsafe_allow_html=True)
        rows = []
        patterns = {"TATA Box": "TATA", "CAAT Box": "CAAT", "GC Box (simplified)": "GC"}
        for name, positions in results.items():
            position_text = ", ".join(str(position) for position in positions) if positions else "Not found"
            rows.append({
                "Motif": name,
                "Pattern": patterns[name],
                "Number of matches": len(positions),
                "Positions": position_text
            })

        result_df = pd.DataFrame(rows)
        st.dataframe(result_df, hide_index=True, use_container_width=True)
        st.download_button(
            "⬇️ Download results as CSV",
            data=result_df.to_csv(index=False),
