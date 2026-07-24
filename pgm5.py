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

        st.success("Movie Ticket Booked Successfully!")

        st.markdown("## 🎫 Booking Confirmation")

        st.markdown(f"""
            **👤 Customer Name:** {name}

            **🎬 Movie:** {movie}

            **🕒 Show Timing:** {timing}

            **🎟 Number of Tickets:** {tickets}

            **💺 Seat Type:** {seat}

            **🍿 Snacks:** {", ".join(snacks)}
        """)

    else:
        st.error("Please accept the Terms and Conditions.")