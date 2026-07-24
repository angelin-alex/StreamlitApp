import streamlit as st

st.set_page_config(page_title="Employee Feedback", page_icon="💼")

st.title("💼 Employee Feedback System")

col1, col2 = st.columns(2)

with col1:
    empid = st.text_input("Employee ID")
    name = st.text_input("Employee Name")

with col2:
    department = st.selectbox(
        "Department",
        ["HR", "IT", "Finance", "Marketing"]
    )

    rating = st.slider(
        "Satisfaction",
        1,
        10,
        5
    )

facilities = st.multiselect(
    "Facilities Used",
    ["WiFi", "Transport", "Gym", "Cafeteria"]
)

suggestion = st.text_area("Suggestions")

document = st.file_uploader("Upload Document")

st.divider()
if st.button("📩 Submit Feedback"):

    st.success("Feedback Submitted Successfully!")

    st.metric("⭐ Satisfaction Rating", rating)

    st.markdown("## 📝 Feedback Summary")

    st.markdown(f"""
**🆔 Employee ID:** {empid}

**👤 Employee Name:** {name}

**🏢 Department:** {department}

**🏋 Facilities Used:** {", ".join(facilities)}

**💬 Suggestions:** {suggestion}
""")

    if document is not None:
        st.info("📄 Supporting Document Uploaded Successfully.")