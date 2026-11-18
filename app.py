import streamlit as st
import pandas as pd
from promoter_scanner import clean_sequence, is_valid, scan_sequence, get_gc_content

st.title("Gene Regulatory Element Scanner")
st.write("Enter a DNA sequence to search for selected motifs.")

sequence = st.text_area("Enter DNA sequence")

if st.button("Scan Sequence"):
    sequence = clean_sequence(sequence)

    if not is_valid(sequence):
        st.error("Please enter a valid DNA sequence using only A, T, G and C.")
    else:
        results = scan_sequence(sequence)

        st.subheader("Sequence Information")
        st.write("Sequence length:", len(sequence))
        st.write("GC content:", str(get_gc_content(sequence)) + "%")

        st.subheader("Motif Results")
        rows = []

        for name, positions in results.items():
            if positions:
                position_text = ", ".join(str(position) for position in positions)
            else:
                position_text = "Not found"

            rows.append({
                "Motif": name,
                "Pattern": {"TATA Box": "TATA", "CAAT Box": "CAAT",
                            "GC Box (simplified)": "GC"}[name],
                "Number of matches": len(positions),
                "Positions": position_text
            })

        st.dataframe(pd.DataFrame(rows), hide_index=True)

        st.download_button(
            "Download Results as CSV",
            data=pd.DataFrame(rows).to_csv(index=False),
            file_name="motif_results.csv",
            mime="text/csv"
        )
