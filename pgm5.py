import streamlit as st

st.set_page_config(page_title="Movie Booking", page_icon="🎬")

st.title("🎬 Movie Ticket Booking")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Customer Name")

    movie = st.selectbox(
        "Movie",
        ["Interstellar", "Avengers", "Jawan", "Leo"]
    )

    timing = st.radio(
        "Show Timing",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

with col2:

    tickets = st.number_input(
        "Tickets",
        1,
        10,
        1
    )

    seat = st.select_slider(
        "Seat Type",
        options=["Silver", "Gold", "Platinum"]
    )

snacks = st.multiselect(
    "Snacks",
    ["Popcorn", "Cold Drink", "Nachos", "French Fries"]
)

agree = st.checkbox("I agree to the Terms and Conditions")

st.divider()

if st.button("🎟 Book Ticket"):

    if agree:

        st.balloons()

        st.success("Booking Confirmed!")

        st.markdown("### 🎫 Booking Summary")

        st.write("Customer:", name)
        st.write("Movie:", movie)
        st.write("Show:", timing)
        st.write("Tickets:", tickets)
        st.write("Seat:", seat)
        st.write("Snacks:", snacks)

    else:
        st.error("Please agree to the Terms and Conditions.")