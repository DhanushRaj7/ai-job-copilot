import streamlit as st


def render_workflow(result):
    tasks = result.get("tasks", [])

    if not tasks:
        return

    st.markdown("## ⚡ AI Workflow")

    cols = st.columns(len(tasks))

    for col, task in zip(cols, tasks):
        with col:
            st.markdown(
                f"""
<div style="
background:#F6F8FA;
border:1px solid #D0D7DE;
border-radius:12px;
padding:18px;
text-align:center;
">

<div style="font-size:28px;">✅</div>

<b>{task}</b>

</div>
""",
                unsafe_allow_html=True,
            )

    st.divider()