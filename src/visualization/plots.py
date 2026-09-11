"""Result visualizations."""

import matplotlib

matplotlib.use("Agg")  # non-interactive backend; safe for scripts & CI
import matplotlib.pyplot as plt  # noqa: E402
import seaborn as sns  # noqa: E402

from src.config import THRESHOLDS  # noqa: E402


def plot_triage_distribution(df, save_path: str) -> None:
    """Bar chart of patient triage level distribution."""
    sns.countplot(x="triage", data=df, hue="triage", palette="Reds", legend=False)
    plt.title("Patient Triage Level Distribution")
    plt.xlabel("Triage Category")
    plt.ylabel("Number of Patients")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


def plot_correlation(df, criteria: list, save_path: str) -> None:
    """Heatmap of criteria correlation."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[criteria].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Between Criteria")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


def plot_score_boxplot(df, save_path: str) -> None:
    """Boxplot of score distribution per triage category."""
    sns.boxplot(x="triage", y="score", data=df, hue="triage", palette="Set2", legend=False)
    plt.title("Score Distribution per Triage Category")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


def plot_scatter(df, save_path: str) -> None:
    """Scatter plot: thalach vs oldpeak colored by triage."""
    sns.scatterplot(x="thalach", y="oldpeak", hue="triage", data=df)
    plt.title("Patient Distribution: Thalach vs Oldpeak")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


def plot_score_histogram(df, save_path: str) -> None:
    """Histogram of SAW scores with triage threshold markers."""
    plt.figure(figsize=(10, 5))
    sns.histplot(df["score"], bins=25, kde=True, color="#C0392B")
    plt.axvline(THRESHOLDS["P1"], color="#7B241C", linestyle="--", label=f"P1 ≥ {THRESHOLDS['P1']}")
    plt.axvline(THRESHOLDS["P2"], color="#E67E22", linestyle="--", label=f"P2 ≥ {THRESHOLDS['P2']}")
    plt.title("SAW Score Distribution")
    plt.xlabel("SAW Score")
    plt.ylabel("Number of Patients")
    plt.legend()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


def plot_radar_p1(df, criteria: list, save_path: str) -> None:
    """Interactive radar chart of the average P1 patient profile (Plotly)."""
    import plotly.express as px

    p1 = df[df["triage"].astype(str).str.startswith("P1")]
    if p1.empty:
        raise ValueError("No P1 patients found in the data.")

    profile = p1[criteria].mean()
    profile = (profile - profile.min()) / (profile.max() - profile.min())

    fig = px.line_polar(
        r=profile.values,
        theta=list(profile.index),
        line_close=True,
        title="Average Profile of P1 Patients (normalized 0-1)",
    )
    fig.write_html(save_path)
