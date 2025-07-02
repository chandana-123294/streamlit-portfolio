import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="centered")

st.title("👋 Hi, I'm Your Name Here")
st.subheader("💻 Aspiring Developer | AI Enthusiast")

# About
st.markdown("## 🧠 About Me")
st.write("I'm a student passionate about AI, automation, and solving problems with code.")

# Projects
st.markdown("## 💼 Projects")
st.markdown("🔍 **Manufacturing Quality Control AI** - Real-time defect detection system using computer vision and sensors.")
st.markdown("📧 **Email Generator App** - Creates professional emails using AI and lets users download them.")
st.markdown("🧘 **Healthy Day Planner** - Plans a full day using Gemini AI and Streamlit.")

# Skills
st.markdown("## 🛠 Skills")
st.write("Python | Streamlit | Gemini API | n8n | AI Agents | GitHub | Computer Vision")

# Resume
with open("Resume.pdf", "rb") as f:
    st.download_button("📄 Download Resume", f, file_name="YourName_Resume.pdf")

# Contact
st.markdown("## 📫 Contact Me")
st.markdown("""
- 📧 your.email@example.com  
- [GitHub](https://github.com/yourusername)  
- [LinkedIn](https://linkedin.com/in/yourusername)  
""")
