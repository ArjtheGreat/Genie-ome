import streamlit as st
from streamlit_extras.let_it_rain import rain
from joblib import load
from header import *
from userinput import *
from response import *
from predictor import *
from genomicbreakdown import *

# Load our DecisionTree model into our web app
lm = load("lm_model.joblib")
X_test = load('X_test.joblib')
original_sequence = load('original_sequence.joblib')
st.set_page_config(layout="wide")
# Custom CSS for the entire app
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Poppins:wght@400;600&display=swap');

    body {
        background: url('https://www.toptal.com/designers/subtlepatterns/memphis-mini-pattern/');
        font-family: 'Poppins', sans-serif;
        background-color: #e0f7fa;
        width: 100%;
    }

    .title {
        font-family: 'Montserrat', sans-serif;
        font-size: 3em;
        color: #004d40;
        text-align: center;
        margin-bottom: 0.5em;
        animation: slideInFromLeft 1s;
    }

    .subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2em;
        color: #00796b;
        text-align: center;
        margin-bottom: 1.5em;
        animation: slideInFromRight 1s;
    }

    .upload-box {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 1em;
        padding: 2em;
        border: 2px dashed #00796b;
        border-radius: 15px;
        background-color: #ffffff;
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }

    .upload-box:hover {
        transform: scale(1.05);
    }

    .response-box {
        background: linear-gradient(135deg, #a7ffeb, #64ffda);
        border-radius: 20px;
        padding: 30px;
        margin-top: 20px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        animation: fadeIn 2s;
    }

    .prediction-text {
        font-family: 'Montserrat', sans-serif;
        font-size: 2em;
        color: #004d40;
        text-align: center;
        font-weight: bold;
        animation: slideInFromRight 2s;
    }

    .prediction-result {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5em;
        color: #004d40;
        text-align: center;
        animation: slideInFromLeft 1s;
    }

    .back-button {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2em;
        color: #ffffff;
        background-color: #00796b;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        cursor: pointer;
        margin-top: 20px;
        display: block;
        text-align: center;
        transition: background-color 0.3s ease;
    }

    .back-button:hover {
        background-color: #004d40;
    }

    .continent-image {
        width: 100%;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    .double-helix-progress-container {
        height: 20px;
        width: 100%;
        background: repeating-linear-gradient(
            -45deg,
            lightgrey,
            lightgrey 10px,
            #ffffff 10px,
            #ffffff 20px
        );
        border-radius: 10px;
        margin-top: 10px;
        overflow: hidden;
        position: relative;
    }

    .double-helix-progress-fill {
        height: 100%;
        background: repeating-linear-gradient(
            -45deg,
            #00796b,
            #00796b 10px,
            #ffffff 10px,
            #ffffff 20px
        );
        position: absolute;
        top: 0;
        left: 0;
        border-radius: 10px;
    }

    .col-container {
        display: flex;
        justify-content: space-between;
        width: 90%;
        margin: 0 auto;
    }

    .col1, .col2 {
        flex: 1;
        padding: 0 2%;
        justify-content: center;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideInFromLeft {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    @keyframes slideInFromRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'show_upload' not in st.session_state:
    st.session_state.show_upload = True

def show_results():
    st.session_state.show_upload = False

def show_upload():
    st.session_state.show_upload = True

if st.session_state.show_upload:
    create_header()
    sequence = get_user_input()
    st.image("/content/drive/My Drive/Inspirit AI Demonstration/COVID World Map.png", use_column_width=True)
    st.write("Credit: Bloomberg")
    if sequence is not None:
        input_features = create_dataframe(sequence, X_test.columns)
        if input_features is not None and input_features.size > 0:
            st.session_state.sequence = sequence
            st.session_state.input_features = input_features
            show_results()
            st.experimental_rerun()
else:
    st.button('Back', on_click=show_upload)
    st.markdown("<div class='title'>Genie-ome Results</div>", unsafe_allow_html=True)
    st.markdown("<style>div.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)
    rain(emoji="🦠😷🧑‍🔬",font_size=35,falling_speed=1,animation_length=3,)
    st.markdown('<div class="col-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        prediction = make_prediction(lm, st.session_state.input_features)
        st.markdown('<div class="prediction-text">Prediction Result</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="prediction-result">{prediction[0]}</div>', unsafe_allow_html=True)

        if prediction[0] == "Oceania":
            col_center = st.columns([1, 2, 1])[1]
            with col_center:
                st.image("/content/drive/My Drive/Inspirit AI Demonstration/Oceania.png", use_column_width=True)
        elif prediction[0] == "Asia":
            col_center = st.columns([1, 2, 1])[1]
            with col_center:
                st.image("/content/drive/My Drive/Inspirit AI Demonstration/Asia.png", use_column_width=True)
        elif prediction[0] == "North America":
            col_center = st.columns([1, 2, 1])[1]
            with col_center:
                st.image("/content/drive/My Drive/Inspirit AI Demonstration/North America.png", use_column_width=True)


    with col2:
        col3, col4 = st.columns([1, 1])
        display_genomic_breakdown(st.session_state.sequence, original_sequence, col3, col4)
    st.markdown('</div>', unsafe_allow_html=True)


