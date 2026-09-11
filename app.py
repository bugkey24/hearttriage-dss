"""Streamlit dashboard for HeartTriage DSS.

Run with:
    streamlit run app.py
"""

from pathlib import Path

import pandas as pd
import streamlit as st

DATA_PATH = Path("data/processed/cleve_triage.csv")

st.set_page_config(page_title="HeartTriage DSS", page_icon="", layout="wide")
st.title(" HeartTriage DSS")
st.caption("_Smart Triage, Faster Decisions_ — SAW-based cardiac ER triage")

if not DATA_PATH.exists():
    st.warning("No triage results found. Run `python scripts/run_pipeline.py` first.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# --- Sidebar filters -------------------------------------------------------
st.sidebar.header("Filters")
triage_options = sorted(df["triage"].unique())
selected = st.sidebar.multiselect("Triage category", triage_options, default=triage_options)
age_min, age_max = int(df["age"].min()), int(df["age"].max())
age_range = st.sidebar.slider("Age range", age_min, age_max, (age_min, age_max))

view = df[df["triage"].isin(selected) & df["age"].between(*age_range)]

# --- Metrics ---------------------------------------------------------------
st.subheader("Triage Overview")
cols = st.columns(4)
cols[0].metric("Total Patients", len(view))
cols[1].metric("P1 — Emergency", int((view["triage"] == "P1 - Emergency").sum()))
cols[2].metric("P2 — Urgent", int((view["triage"] == "P2 - Urgent").sum()))
cols[3].metric("P3 — Non-Urgent", int((view["triage"] == "P3 - Non-Urgent").sum()))

# --- Charts ----------------------------------------------------------------
left, right = st.columns(2)
with left:
    st.subheader("Triage Distribution")
    st.bar_chart(view["triage"].value_counts())
with right:
    st.subheader("Score Distribution")
    st.bar_chart(view["score"], height=350)

# --- Table -----------------------------------------------------------------
st.subheader("Patient Results")
st.dataframe(
    view[["age", "sex", "cp", "trestbps", "chol", "thalach", "score", "triage"]],
    use_container_width=True,
)

st.download_button(
    label="Download filtered results (CSV)",
    data=view.to_csv(index=False).encode("utf-8"),
    file_name="hearttriage_results.csv",
    mime="text/csv",
)

st.caption(" Decision support only — does not replace clinical judgment.")
