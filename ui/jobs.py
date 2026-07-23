import streamlit as st


def render_jobs(result):
    """
    Render professional job cards.
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

        title = "Unknown Position"
        company = "Unknown Company"
        location = "Unknown Location"
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

        st.markdown(
            f"""
<div style="
background:#F6F8FA;
border:1px solid #D0D7DE;
border-radius:12px;
padding:18px;
margin-bottom:18px;
">

<h3 style="margin-bottom:6px;">💼 {title}</h3>

<p style="margin:0;color:#57606A;">
🏢 <b>{company}</b>
</p>

<p style="margin-top:6px;color:#57606A;">
📍 {location}
</p>

</div>
""",
            unsafe_allow_html=True,
        )

        with st.expander("📄 View Job Description"):

            st.write(description)

        displayed = True

    if not displayed:
        st.info("No jobs found.")