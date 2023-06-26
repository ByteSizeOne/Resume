from pathlib import Path

import streamlit as st
from PIL import Image

# -- PATH SETTINGS

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assests" / "CV.pdf"
profile_pic = current_dir / "assests" / "profile-pic.png"

# -- GENERAL SETTINGS

PAGE_TITLE = "Digital CV | John Doe"
PAGE_ICON = ":wave:"
NAME = "John Doe"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data driven decision-making.
"""
EMAIL = "johndoe@mailinator.com"
SOCIAL_MEDIA = {
    "Youtube": "https://www.youtube/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https:twitter.com",
}

PROJECTS = {
    "🔐 Sales Dashboard - Comparing sales across three stores:": "https://youtu.be/Sb0A9i6d320",
    "🔐 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🔐 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🔐 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there!")

# -- LOAD CSS, PDF, & PROFILE PIC --

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# -- HERO SECTION --

col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=240)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📃 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
st.write("📫", EMAIL)

# --- SOCIAL LINKS ---

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---

st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 7 Years experience extrating actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sence of initiative on tasks
""")

# --- SKILLS ---

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 🟡 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 🔴 Data visualisation: PowerBI, MS Excel, Ploty
- 🟢 Modeling: Logistic, regression, linear regression, decition trees
- 🟣 Databases: Postgres, MongoDB, MySQL   
"""
)
