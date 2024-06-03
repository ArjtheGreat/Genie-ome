import streamlit as st

def get_app_response(prediction):
    st.markdown("<div class='prediction-result'>Prediction Result</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='prediction-text'>{prediction[0]}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
