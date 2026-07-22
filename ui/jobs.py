import streamlit as st


def render_jobs(result):
    """
    Render the Jobs tab.
    """

    st.subheader("💼 Live Job Opportunities")

    jobs_text = result.get("jobs_found", "")

    if not jobs_text.strip():
        st.info("No jobs were returned.")
        return

    jobs = jobs_text.split("=" * 60)

    displayed = False

    for job in jobs:

        if not job.strip():
            continue

        title = "Job Opportunity"
        company = "N/A"
        location = "N/A"
        description = ""

        for line in job.splitlines():

            line = line.strip()

            if line.startswith("Job Title"):
                title = line.replace("Job Title:", "").strip()

            elif line.startswith("Company"):
                company = line.replace("Company:", "").strip()

            elif line.startswith("Location"):
                location = line.replace("Location:", "").strip()

            elif line.startswith("Description"):
                description = job.split("Description:")[-1].strip()

        with st.container():

            st.markdown(f"## 💼 {title}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**🏢 Company**")
                st.write(company)

            with col2:
                st.markdown("**📍 Location**")
                st.write(location)

            with st.expander("View Job Description"):

                if description:
                    st.write(description)
                else:
                    st.write(job)

            st.divider()

        displayed = True

    if not displayed:
        st.info("No jobs found.")