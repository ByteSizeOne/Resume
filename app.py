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

# --- WORK HISTORY ---

st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---

st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- 👉 Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives,
and supplied recommendations to boost landing page conversion by 38%
- 👉 Led a team of 4 analyst to brainstorm potential marketing and sales improvements,
and implementated A/B tests to generate 15% more client leads
- 👉 Redesigned data model through integrations that improved pridictions by 12%
"""
)

# --- JOB 2 ---

st.write("#")
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- 👉 Build data models and maps to generate meaningful insights from customer data,
boosting successful sales efforts by 12%
- 👉 Modeled targets likely to renew, and presented analysis to leadership, which led to
a YoY revenue increase of $300K
- 👉 Complied, studied, and inferred large amounts of data, modelling information to drive
auto policy pricing
"""
)


# --- JOB 3 ---

st.write("#")
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- 👉 Devised KPIs using SQL across company website in collaboration with cross-functional
teams to achieve a 120% jump in organic traffic
- 👉 Analyzed, documented, and reported user survey results to improve customer
communication processes by 18%
- 👉 Collaborated with analyst team to oversee end-to-end process surrounding customers'
return data
"""
)

# --- PROJECTS AND ACCOMPLISHMENTS

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}][{link}]")
    
