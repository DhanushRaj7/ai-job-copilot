import streamlit as st


def render_sidebar():
    """Render the application sidebar."""

    with st.sidebar:
        st.title("🤖 AI Job Copilot")

        st.markdown("---")

        st.subheader("🛠 Tech Stack")

        technologies = [
            "LangGraph",
            "Groq LLM",
            "Adzuna API",
            "Streamlit"
        ]

        for tech in technologies:
            st.success(tech)

        st.markdown("---")

        st.subheader("⚙️ Agent Workflow")

        workflow = [
            "Planner",
            "Dependency Resolver",
            "Task Router",
            "Search Node",
            "Analysis Node",
            "Roadmap Node",
            "Interview Node"
        ]

        for index, step in enumerate(workflow):
            st.markdown(f"**{index+1}. {step}**")
            if index != len(workflow) - 1:
                st.markdown("⬇️")

        st.markdown("---")

        st.caption("Built with ❤️ by Dhanush Raj")