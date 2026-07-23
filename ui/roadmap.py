import re
import streamlit as st


def render_roadmap(result):
    """
    Render the Learning Roadmap tab.
    """

    st.subheader("🗺️ Personalized Learning Roadmap")

    roadmap = result.get("learning_plan", "")

    if not roadmap.strip():
        st.info("No learning roadmap available.")
        return

    if "Week" in roadmap:

        sections = re.split(r"(?=Week\s+\d+)", roadmap)

        for section in sections:

            section = section.strip()

            if not section:
                continue

            heading = section.split("\n")[0]

            with st.expander(f"📅 {heading}", expanded=False):
                st.markdown(section)

    else:
        st.markdown(roadmap)