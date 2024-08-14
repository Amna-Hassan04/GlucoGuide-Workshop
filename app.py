import streamlit as st
import anthropic

# Access your API key
api_key = st.secrets["claude_api_key"]
# Sidebar inputs
st.sidebar.header("Input Your Details")
fasting_sugar = st.sidebar.number_input("Fasting Sugar Level (mg/dL)", min_value=0, max_value=500, step=1)
pre_meal_sugar = st.sidebar.number_input("Pre-Meal Sugar Level (mg/dL)", min_value=0, max_value=500, step=1)
post_meal_sugar = st.sidebar.number_input("Post-Meal Sugar Level (mg/dL)", min_value=0, max_value=500, step=1)
dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., vegetarian, low-carb)")

# Main app
st.title("GlucoGuide")
st.write("""
### Your Personalized Meal Planning Assistant
GlucoGuide helps you manage your diabetes by providing meal plans tailored to your specific blood sugar levels and dietary preferences. 
Simply input your fasting, pre-meal, and post-meal sugar levels along with any dietary preferences, 
and let GlucoGuide suggest the best meals for you.
""")

# Function to generate meal plan using Claude API
def generate_meal_plan(fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences):
    client = anthropic.Anthropic(api_key=api_key)

    user_prompt = f"""
    Create a meal plan for a diabetic person with the following details:
    - Fasting Sugar Level: {fasting_sugar} mg/dL
    - Pre-Meal Sugar Level: {pre_meal_sugar} mg/dL
    - Post-Meal Sugar Level: {post_meal_sugar} mg/dL
    - Dietary Preferences: {dietary_preferences}
    Provide meals that help manage blood sugar levels effectively.
    """

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0.7,
        system="You are a nutritionist specializing in diabetes management.",
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    raw_context = message.content
    itinerary = raw_context[0].text
    return itinerary

# Button to generate meal plan
if st.sidebar.button("Generate Meal Plan"):
    meal_plan = generate_meal_plan(fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences)
    
    # Display the meal plan as formatted text
    st.subheader("Your Personalized Meal Plan")
    st.markdown(meal_plan)
