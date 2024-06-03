import streamlit as st
import os

def create_header():
    cwd = os.getcwd()
    
    # Get the absolute path to the image
    image_path = os.path.join(cwd, 'Genie-ome.png')
    st.write("Image path:", image_path)

    st.markdown("""
        <style>
        .header {
            display: flex;
            align-items: center;
            width: 100%;
        }
        .header img {
            animation: smokeDisappear 2s ease-in-out forwards;
        }

         @keyframes smokeDisappear {
            0% {
                opacity: 1;
                transform: scale(1);
            }
            100% {
                opacity: 0;
                transform: scale(2);
                filter: blur(10px);
            }
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='header'>", unsafe_allow_html=True)
    st.image("Genie-ome.png", width=180)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='title'>Genie-ome: A Genome Geolocator Model</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>By Arjun, Daren, Sarina, Pooja</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Upload a .fasta file, let's predict which region of the world it comes from</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
