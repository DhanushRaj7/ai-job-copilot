import streamlit as st


def render_analysis(result):
    """
    Render the Skill Gap Analysis tab.
    """

    st.subheader("📊 Skill Gap Analysis")

    analysis = result.get("skill_gap_analysis", "")

    if not analysis.strip():
        st.info("No skill gap analysis available.")
        return

    st.info(analysis)