import streamlit as st


def render_interview(result):
    st.subheader("🎤 Interview Preparation")

    questions = result.get("interview_questions", "")

    if not questions.strip():
        st.info("No interview questions generated.")
        return

    st.markdown(
        f"""
<div style="
background:#F6F8FA;
border:1px solid #D0D7DE;
border-radius:12px;
padding:20px;
">
{questions}
</div>
""",
        unsafe_allow_html=True,
    )