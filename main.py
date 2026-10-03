import streamlit as st 
from google import genai
from dotenv import load_dotenv
import time
# load_dotenv() 

client = genai.Client()

# st.title(" 🌍 Travel Assistant") 
st.markdown("""
<style>
@keyframes gradient-animation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.live-heading {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(-45deg, #FF4B4B, #FF8A00, #2E86C1, #1ABC9C);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient-animation 6s ease infinite;
    margin-bottom: 0px;
}
</style>

<div style="text-align: center; padding: 15px 0;">
    <h1 class="live-heading">✈️️ Travel Assistant 🌍 </h1>
    <p style="color: #7F8C8D; font-size: 1.1rem; letter-spacing: 2px; margin-top: 5px;">
        DISCOVER • PLAN • EXPLORE
    </p>
</div>
""", unsafe_allow_html=True)

st.caption("Tumhara Personall Planner")

location  = st.text_input("Where do you want to go chipmunk")
Days_Nr = st.number_input("How many days of Trip",min_value=1 , max_value=30)

budget = st.selectbox("Select Budget",["Luxury","Moderate","Budgeted"])
travel_type=st.radio("Who are Travelling with",["Family","Solo","Friends"])

prompt = f"""You are a Travel Planner User is saying He/She wants to go to 
 {location} for {Days_Nr} days, he is on a budget of type {budget}
 Travel Type is : {travel_type} 
 Plan a trip a share answer in bullet format"""
if st.button("Plan Trip") : 
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input= prompt
        )
    with st.spinner("Wait for it....." , show_time=True): 
           time.sleep(5)

    st.success("Vola !! here are some fab suggestions") 
    st.write(interaction.output_text) 
    
