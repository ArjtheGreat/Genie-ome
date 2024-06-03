import streamlit as st
import numpy as np
from Bio.Seq import Seq

def display_genomic_breakdown(sequence, original_sequence, left_col, right_col):
    base_counts = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'C': sequence.count('C'),
        'G': sequence.count('G'),
        'N': sequence.count('N')
    }

    with left_col:
        st.subheader("Genomic Breakdown")
        st.write(f"**Total Length:** {len(sequence)}")

        st.write(f"**A (Adenine):** {base_counts['A']} - Essential for cellular respiration and energy storage.")
        st.write(f"**T (Thymine):** {base_counts['T']} - Vital for DNA stability and structure.")
        st.write(f"**C (Cytosine):** {base_counts['C']} - Important for cell signaling and genetic regulation.")
        st.write(f"**G (Guanine):** {base_counts['G']} - Crucial for protein synthesis and enzyme function.")
        st.write(f"**N (Unknown):** {base_counts['N']} - Represents unrecognized or missing bases.")

    with right_col:
        st.subheader("Comparison Original Strand:")
        sequence_arr = np.array(Seq(sequence))
        n_bases_different = sum(1 for a, b in zip(sequence, original_sequence) if a != b)
        n_bases_same = len(sequence) - n_bases_different
        st.write(f"Comparing your sequence to the original strand of Severe acute respiratory syndrome coronavirus 2 (isolate Wuhan-Hu-1) from Wuhan, China. Helps to identify mutations and understand the evolutionary changes of the virus based on location.")
        st.write(f"1. Number of bases that differ: **{n_bases_different}**")
        st.write(f"2. Number of bases that are same: **{n_bases_same}**")
        percent_similarity = 100 * n_bases_same / len(sequence)
        st.write(f"3. Percent similarity: **{percent_similarity:.2f}%**")

        st.markdown(
            f"""
            <div class="double-helix-progress-container">
                <div class="double-helix-progress-fill" style="width: {percent_similarity}%"></div>
            </div>
            """,
            unsafe_allow_html=True
        )
