import streamlit as st
import google.generativeai as genai
import os

# Streamlit setup
st.set_page_config(page_title="StartAI – Gemini Mentor Panel", layout="centered")
st.title("🌟 StartAI – Create Your Dream Mentor Panel (Gemini-Powered)")

# Set Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# UI Inputs
mentor_name = st.text_input("👤 Mentor Name", placeholder="e.g., Elon Musk, Indra Nooyi")
domain = st.text_input("🏷️ Domain / Industry", placeholder="e.g., HealthTech, FinTech, AgriTech")
query = st.text_area("💬 What would you ask this mentor?", placeholder="Ask about fundraising, team building, scaling...")
context = st.text_area("📄 Optional: Describe your startup or current challenge", placeholder="We are a B2B SaaS startup building an AI tool for HR...")

# Prompt Builder
def generate_persona_prompt(name, domain, query, context):
    return f"""
You are {name}, a legendary leader in the {domain} industry.

A young startup founder is asking for your guidance. Please:
- Use your typical personality and leadership tone
- Share industry-specific advice and bold thinking
- Inspire them with practical steps and mental models
- Mention relevant failure patterns or startup cases if any

Startup Context:
{context}

Founder’s Question:
{query}

Now respond as {name}, speaking directly to the founder.
"""

# Generate Advice
if st.button("🎯 Get Mentor Advice"):
    if not mentor_name or not domain or not query:
        st.warning("Please fill in the mentor, domain, and question.")
    else:
        prompt = generate_persona_prompt(mentor_name, domain, query, context)
        with st.spinner("Consulting your AI-powered mentor..."):
            try:
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(prompt)
                st.success(f"✅ Advice from {mentor_name}:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"❌ Error generating advice: {e}")
