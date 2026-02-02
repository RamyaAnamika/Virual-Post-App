import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Viral Post Detector",
    page_icon="🔥",
    layout="centered"
)

st.markdown("""
<style>

/* 🌸 Attractive mixed gradient background */
.stApp {
    background: linear-gradient(135deg, #FDFCFB, #E2EBF0, #F3E7E9);
}

/* 📝 ALL normal text */
p, span, label, div {
    color: #2C2C2C !important;
    font-weight: 500;
}

/* 🔠 Headings */
h1 {
    color: #1F3C88 !important;
    font-weight: 800;
}
h2, h3 {
    color: #3A4F7A !important;
    font-weight: 700;
}

/* ✍️ Text area & select box */
textarea, select, input {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    border-radius: 12px;
    border: 1px solid #CBD5E1;
}

/* 🔘 Button */
div.stButton > button {
    background: linear-gradient(to right, #4F8EF7, #6A5ACD);
    color: #FFFFFF;
    font-weight: bold;
    border-radius: 14px;
    height: 48px;
    font-size: 16px;
}

/* 📦 Card (for AI answer / content) */
.card {
    background-color: #FFFFFF;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.1);
}

/* 🤖 AI Answer text */
.ai-answer {
    color: #333333;
    font-size: 17px;
    font-weight: 600;
    line-height: 1.7;
}

/* 🔹 Bullet points */
.ai-answer li {
    color: #374151;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

#API Setup
api_key = "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"

#Exception handling
try:
    client = Groq(api_key=api_key) # AI connection
except Exception as e:
    st.error(f"Error initializing Groq client: {e}")

st.title("🔥 Viral Post Detector")
st.markdown("------------------")

st.write("Enter your topic and get a viral post")
topic = st.text_area("what is your post about?", placeholder="My first day learning AI with Python")
language = st.selectbox("Select Language", ["English","Tamil","Tanglish", "Spanish", "French", "German", "Chinese"])

col1, col2, col3 = st.columns([1,2,1])
with col2:
    generate_btn = st.button("Generate Post", type="primary", use_container_width=True)

if generate_btn:
    if not topic.strip():
        st.warning("Please enter a topic to generate a post.")
    else:
        with st.spinner("AI is thinking..."):

            prompt = f"""
            Act as a professional social media influencer
            write an engaging, viral linkedin/instagram post about : '{topic}'.

            STRICT REQUIREMENTS: Write the post in **{language}**.

            Rules:
            1. Start with a catchy Hook/Headline
            2. Use bullet points
            3. Include relevant Emojis
            4. End with a qusetion to audience
            5. Add 5 trending just hashtags related to the topic
            """

            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role":"user", "content": prompt}
                    ],
                    model = "llama-3.3-70b-versatile"
                )

                ai_response = chat_completion.choices[0].message.content
                st.balloons()
                st.success("🔥 Viral Post Generated!")
                st.markdown(ai_response)

                st.info("Tip: copy this and post it on your linkedin/instagram")

            except Exception as e:
                st.error(f"Error generating post: {e}")
# Run the app with: streamlit run viral_post.py