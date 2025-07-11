import streamlit as st
import random

st.set_page_config(page_title="🍕 Random Pizza Toppings", layout="centered")

st.title("🍕 Random Pizza Topping Generator")

# Sidebar options
st.sidebar.header("Topping Preferences")

num_toppings = st.sidebar.slider("Number of toppings", min_value=1, max_value=10, value=3)

vegetarian = st.sidebar.checkbox("Vegetarian", value=False)
vegan = st.sidebar.checkbox("Vegan", value=False)

# Topping lists
meat_toppings = ["Pepperoni", "Sausage", "Bacon", "Ham", "Chicken", "Anchovies"]
vegetarian_toppings = ["Mushrooms", "Bell Peppers", "Olives", "Onions", "Pineapple", "Tomatoes", "Jalapeños"]
vegan_toppings = ["Mushrooms", "Bell Peppers", "Olives", "Onions", "Pineapple", "Spinach", "Zucchini", "Artichokes"]

# Decide what topping pool to use
if vegan:
    available_toppings = vegan_toppings
elif vegetarian:
    available_toppings = vegetarian_toppings + vegan_toppings
else:
    available_toppings = meat_toppings + vegetarian_toppings + vegan_toppings

# Remove duplicates
available_toppings = list(set(available_toppings))

# Button to generate toppings
if st.button("🎲 Generate Toppings"):
    if num_toppings > len(available_toppings):
        st.error(f"Only {len(available_toppings)} toppings available for the current setting.")
    else:
        selected = random.sample(available_toppings, k=num_toppings)
        st.success("Your random pizza toppings are:")
        st.write("🍕 " + ", ".join(selected))
