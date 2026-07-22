import streamlit as st


def render_workflow(tasks):

    st.subheader("🧠 Execution Workflow")

    if not tasks:
        st.warning("No workflow generated.")
        return

    st.info(" ➜ ".join(tasks))