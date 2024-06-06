import streamlit as st
import os

def create_header():
    cwd = os.getcwd()
    
    # Get the absolute path to the image
    image_path = os.path.join(cwd, 'Genie-ome.png')

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
    col1, col2 = st.columns([1,8])

    with col1:
      st.image(image_path, width=180)
    with col2:
        st.markdown("<div class='title'>Genie-ome: A Genome Geolocator Model</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>By Arjun Maitra, Daren Zhong, Sarina Wang, Pooja Kallur</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>Upload a .fasta file, let's predict which region of the world it comes from</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
