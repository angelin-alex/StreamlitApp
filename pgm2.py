import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Registration", page_icon="🎓")

st.title("🎓 Student Registration Portal")
st.markdown("Fill in your details below.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Student Name")
    age = st.number_input("Age", 18, 40, 18)

with col2:
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    department = st.selectbox(
        "Department",
        ["BCA", "B.Sc CS", "B.Tech AI", "MCA"]
    )

subjects = st.multiselect(
    "Subjects",
    ["Python", "Java", "AI", "Cloud Computing", "Data Science"]
)

date = st.date_input("Admission Date")

photo = st.file_uploader(
    "Upload Profile Photo",
    type=["jpg", "jpeg", "png"]
)

st.divider()

if st.button("✅ Register"):

    st.balloons()
    st.success("Registration Completed Successfully!")

    st.markdown("## 📄 Registration Summary")

    st.markdown(f"""
**👤 Student Name:** {name}

**🎂 Age:** {age}

**🚻 Gender:** {gender}

**🏫 Department:** {department}

**📚 Subjects Chosen:** {", ".join(subjects)}

**📅 Admission Date:** {date}
""")

    if photo is not None:
        st.markdown("### 🖼 Profile Photo")
        st.image(photo, width=180)
