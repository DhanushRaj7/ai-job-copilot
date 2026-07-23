import streamlit as st


def load_css():
    st.markdown(
        """
<style>

/* ==========================
   Global
========================== */

.main {
    background-color: #ffffff;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* ==========================
   Buttons
========================== */

.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: none;
    background: #0969DA;
    color: white;
    font-weight: 600;
    padding: 0.7rem;
    transition: all .2s ease;
}

.stButton > button:hover {
    background: #0550AE;
}

/* ==========================
   Text Input
========================== */

.stTextInput input {
    border-radius: 10px;
}

/* ==========================
   Expanders
========================== */

.streamlit-expanderHeader {
    font-weight: 600;
    font-size: 16px;
}

/* ==========================
   Metrics
========================== */

[data-testid="stMetric"] {
    background: #F6F8FA;
    border: 1px solid #D0D7DE;
    border-radius: 12px;
    padding: 15px;
}

/* ==========================
   Tabs
========================== */

button[data-baseweb="tab"] {
    font-weight: 600;
}

/* ==========================
   Footer
========================== */

footer {
    visibility: hidden;
}

</style>
""",
        unsafe_allow_html=True,
    )