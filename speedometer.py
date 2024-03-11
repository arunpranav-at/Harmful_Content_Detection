import streamlit as st
import plotly.graph_objects as go

def indicator_gauge(val,istoxix):
    # st.header("Text Input")
    # text_input = st.text_area("Enter Text", key="my_input_text_area")
    # b = st.button("Proceed")
    if istoxix:
        clr = "red"
        textval = "Toxic"
    else:
        clr = "green"
        textval = "Non toxic"
    vals = val*100
    
        
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=vals,
        domain={'x': [0.5, 0.5], 'y': [0, 0.5]},
        title={'text': textval},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': clr}
                }))
    
    st.write(fig)
        
         
# indicator_gauge(0.74,True)
