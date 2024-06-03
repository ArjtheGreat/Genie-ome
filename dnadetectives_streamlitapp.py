import pandas as pd
import os
from joblib import dump, load

import warnings
warnings.filterwarnings("ignore")
!pip -q install streamlit
!pip -q install pyngrok
from pyngrok import ngrok

def launch_website():
  print ("Click this link to try your web app:")
  public_url = ngrok.connect()
  print (public_url)
  !streamlit run --server.port 80 app.py >/dev/null

launch_website()
