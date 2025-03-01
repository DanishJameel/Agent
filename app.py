import streamlit as st

st.set_page_config(page_title="Sample Agent Bot Voice", layout="centered")

st.markdown("# Tax Pro Agent")
st.markdown("### Powered by NMS")

# User selection for AI Agent (Male or Female)
agent_choice = st.radio("Choose Your Agent:", ("Male Agent", "Female Agent"))

# Define agent IDs
male_agent_id = "wqwu6RS8mBYeCutSCqFW"  # Male Agent ID
female_agent_id = "npr5Ye8C8pwYJKDQRQDP"  # Female Agent ID

# Select the appropriate agent ID based on user choice
selected_agent_id = male_agent_id if agent_choice == "Male Agent" else female_agent_id

# Embed the ElevenLabs ConvAI widget using an iframe
iframe_code = f"""
    <iframe src="https://elevenlabs.io/convai-widget/index.html?agent-id={selected_agent_id}" 
    width="100%" height="500" style="border:none;"></iframe>
"""

st.components.v1.html(iframe_code, height=500)
