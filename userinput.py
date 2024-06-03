import streamlit as st
from Bio import SeqIO
import numpy as np
from io import StringIO
import pandas as pd

def get_user_input():
    uploaded_file = st.file_uploader("Choose a .fasta file", type="fasta")
    sequence = ""
    if uploaded_file is not None:
        # Convert the uploaded file to a StringIO object
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        for record in SeqIO.parse(stringio, 'fasta'):
            sequence = str(record.seq)
            st.write(sequence[:20] + "..." + sequence[-20:])
        st.success("File uploaded successfully!")
        st.markdown("</div>", unsafe_allow_html=True)
        return sequence
    else:
        st.warning("Please upload a .fasta file.")
        st.markdown("</div>", unsafe_allow_html=True)
        return None

def create_dataframe(sequence, X_test_columns):
    columns = {}
    if sequence:
        for column in X_test_columns:
            location = int(column.split('_')[0])
            base = column.split('_')[1]

            if location < len(sequence):
                if sequence[location] == base:
                    columns[column] = 1
                else:
                    columns[column] = 0
            else:
                columns[column] = 0
        df = pd.DataFrame([columns])
        return df
    else:
        return None


def pad_or_truncate_sequence(sequence, expected_length):
    if len(sequence) > expected_length:
        return sequence[:expected_length]
    elif len(sequence) < expected_length:
        return sequence + 'N' * (expected_length - len(sequence))
    else:
        return sequence
