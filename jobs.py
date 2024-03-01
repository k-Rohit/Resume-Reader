from serpapi import GoogleSearch
import streamlit as st
import json
def search_jobs():
    search = GoogleSearch({
        "q": "Data Scientist Jobs",
        "location": "Pune,India",
        "api_key": "2aa16b465f280635fa94bc38073abd9abacc4abee29e2d727bdd93962a755d6c"
    })
    result = search.get_dict()
    st.write(result)

    
