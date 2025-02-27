import streamlit as st

st.set_page_config(page_title="Sample Agent Bot Voice", layout="centered")

st.markdown("# Tax Pro Agent")
st.markdown("### Powered by  NMS")

# User selection for AI Agent (Male or Female)
agent_choice = st.radio("Choose Your Agent:", ("Male Agent", "Female Agent"))

# Define agent IDs
male_agent_id = "wqwu6RS8mBYeCutSCqFW"  # Male Agent ID
female_agent_id = "npr5Ye8C8pwYJKDQRQDP"  # Female Agent ID

# Select the appropriate agent ID based on user choice
selected_agent_id = male_agent_id if agent_choice == "Male Agent" else female_agent_id

# Custom CSS to position the call button below the agent UI
custom_css = """
    <style>
        elevenlabs-convai {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
        }
    </style>
"""

# Embed the selected Eleven Labs ConvAI widget with styling
widget_code = f"""
{custom_css}
<elevenlabs-convai agent-id="{selected_agent_id}"></elevenlabs-convai>
<script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
"""

st.components.v1.html(widget_code, height=500)
