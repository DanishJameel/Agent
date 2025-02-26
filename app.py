import streamlit as st

st.set_page_config(page_title="Sample Agent Bot voice", layout="centered")

st.markdown("# Tax pro agent")
st.markdown("### Powered")

# User selection for AI Agent (Male or Female)
agent_choice = st.radio("Choose Your  Agent:", ("Male Agent", "Female Agent"))

# Define agent IDs
male_agent_id = "4HHypNdTplYHuGM3A1Ky"  # Male Agent ID
female_agent_id = "SLjqAdjbda6LpRyBbDd3"  # Female Agent ID

# Select the appropriate agent ID based on user choice
selected_agent_id = male_agent_id if agent_choice == "Male Agent" else female_agent_id

# Embed the selected Eleven Labs ConvAI widget
widget_code = f"""
<elevenlabs-convai agent-id="{selected_agent_id}"></elevenlabs-convai>
<script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
"""

st.components.v1.html(widget_code, height=500)
