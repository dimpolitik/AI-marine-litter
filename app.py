# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:00:03 2022

@author: ΔΗΜΗΤΡΗΣ
""" 
# https://towardsdatascience.com/7-reasons-why-you-should-use-the-streamlit-aggrid-component-2d9a2b6e32f0
import pandas as pd 
import streamlit as st 
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(page_title="Marine Litter Modelling", layout="wide") 

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 26px;">Last Update: November 2022</p>'
st.markdown(new_title, unsafe_allow_html=True)

st.title("Using Artificial Intelligence to Support Marine Litter Research: An Online Database")
st.markdown("**Authors:** Dimitris Politikos, Argyro Adamopoulou, George Petasis, Francois Galgani. **Correspondence:** dimpolit@hcmr.gr")

#url = "https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py"
#st.write("For more details, see the [link](%s)." % url)

#st.markdown("check out this [link](%s)" % url)

xls = pd.ExcelFile('screening_deep_new.xlsx')
shows = pd.read_excel(xls)
shows['Year'] = shows['Year'].astype(str)

st.image('maps_site.png', width = 1000)

gb = GridOptionsBuilder.from_dataframe(shows)
gb.configure_pagination()

gb.configure_side_bar()
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
gridOptions = gb.build()

new_title = '<p style="font-family:calibri; font-size: 20px;">List of papers that use AI in marine macrolitter research. The user can filter papers based on several criteria such as Year, Title, doi, Region, Litter deposit, Dataset type, Dataset source, Sampling system, Usability, Task, Predictability, and Architecture<sup>1</sup>.</p>'
st.markdown(new_title, unsafe_allow_html=True)

#st.markdown("List of papers that use AI in marine litter research. The user can filter papers based on several criteria such as Year, Litter deposit, Dataset, Data type, Goal-of-study, Region, Approach, Implications.")

n = '<p style="font-family:calibri; font-size: 16px;">Abbreviations<sup>1</sup>: Convolutional neural networks (CNN), Object detection architectures (OD), Feed forward neural networks (FFNN), Machine learning algorithms (MLA), Endoder-decoder architectures (ED), Instance segmentation architectures (Inst-Seg), Semantic segmentation architectures (Seg-Sem) and Clustering.</p>'

AgGrid(shows, gridOptions=gridOptions, allow_unsafe_jscode=True, enable_enterprise_modules=True)
st.markdown(n, unsafe_allow_html=True)




