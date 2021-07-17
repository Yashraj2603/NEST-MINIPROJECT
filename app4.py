import streamlit as st
import base64
#file="home1.jfif"
#st.image(file)

main_bg='back.jpg'
main_bg_ext='jpg'
st.markdown(
    f"""
    <style>
    
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

col1, col2, col3 = st.beta_columns([3,5,2])

with col1:
    st.write("")

with col2:
    st.image("logo1.jpg")
    st.write("")
    st.write(" [Get started now](https://share.streamlit.io/ameenafarooq/mini_project_signin/main/app1.py)")

with col3:
    st.write("")
#st.write("Get your prediction now [link](https://share.streamlit.io/ameenafarooq/mini_project_signin/main/app1.py)")    




