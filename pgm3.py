import streamlit as st

st.set_page_config(page_title="Food Ordering", page_icon="🍔")

st.title("🍔 Online Food Ordering")

left, right = st.columns(2)

with left:
    name = st.text_input("Customer Name")
    restaurant = st.selectbox(
        "Restaurant",
        ["Dominos", "KFC", "Pizza Hut", "McDonald's"]
    )

with right:
    quantity = st.slider("Quantity", 1, 10, 1)
    payment = st.radio(
        "Payment",
        ["Cash", "UPI", "Card"]
    )

food = st.multiselect(
    "Food Items",
    ["Pizza", "Burger", "Fries", "Chicken", "Coke"]
)

instructions = st.text_area("Delivery Instructions")

confirm = st.checkbox("I confirm my order")

st.divider()

if st.button("🍽 Place Order"):

    if confirm:

        st.success("Order Placed Successfully!")

        st.json({
            "Customer": name,
            "Restaurant": restaurant,
            "Items": food,
            "Quantity": quantity,
            "Instructions": instructions,
            "Payment": payment
        })

    else:
        st.warning("Please confirm your order.")