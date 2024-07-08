import streamlit as st
from streamlit_extras.bottom_container import bottom

st.set_page_config(
    page_title="About project",
    page_icon="🧑‍💻",
    layout="wide",
)

st.logo(image="./images/NCSC.png")
st.page_link("main.py", label="Back", icon="🔙")
st.header("National Commission of Senior Citizens", divider="rainbow", anchor=False)

st.markdown("### Members")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.image("./images/placeholder.png")
    st.markdown("[Meinard Adrian Francisco](https://github.com/znarfm)")
with c2:
    st.image("./images/placeholder.png")
    st.write("[Prince Bryll Soliven](https://www.linkedin.com/in/prince-bryll-soliven/)")
with c3:
    st.image("./images/placeholder.png")
    st.write("[Jedric Knight Vicente](https://github.com/HalluciKnight)")
with c4:
    st.image("./images/placeholder.png")
    st.write("[Novelle Estrella](https://github.com/Novelle-Estrella)")

st.divider()
st.markdown("### Links")
st.page_link(page="https://github.com/znarfm/infoman_project", label="GitHub Repository", icon="👨‍💻")
st.page_link(page="https://www.ncsc.gov.ph/", label="Official NCSC Website", icon="🌐")

with bottom():
    st.warning("This website is an independent project and is not affiliated with [NCSC](https://www.ncsc.gov.ph/). It is intended solely for academic purposes.", icon="⚠️")