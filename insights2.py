import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np


# Sample ServiceNow incident data (you would replace this with your actual data)
def generate_sample_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    data = {
        "incident_number": [f"INC{i:06d}" for i in range(len(dates))],
        "created_date": dates,
        "priority": np.random.choice(
            ["P1", "P2", "P3", "P4"], size=len(dates), p=[0.1, 0.2, 0.4, 0.3]
        ),
        "resolution_time": np.random.normal(24, 8, len(dates)),  # hours
        "category": np.random.choice(
            ["Hardware", "Software", "Network", "Security"], size=len(dates)
        ),
    }
    return pd.DataFrame(data)


def analyze_incidents():
    # Load data
    df = generate_sample_data()

    # Analysis question
    question = "What is the average resolution time by category across different months in 2023?"

    # Analysis
    monthly_resolution = (
        df.groupby([df["created_date"].dt.strftime("%Y-%m"), "category"])[
            "resolution_time"
        ]
        .mean()
        .reset_index()
    )

    # Create plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=monthly_resolution,
        x="created_date",
        y="resolution_time",
        hue="category",
        marker="o",
    )
    plt.title("Average Resolution Time by Category (Monthly)")
    plt.xlabel("Month")
    plt.ylabel("Resolution Time (hours)")
    plt.xticks(rotation=45)
    plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    # Save plot
    plt.savefig("plot.jpeg", bbox_inches="tight")

    # Calculate KPIs
    avg_by_category = (
        df.groupby("category")["resolution_time"].agg(["mean", "min", "max"]).round(2)
    )
    worst_category = avg_by_category["mean"].idxmax()
    best_category = avg_by_category["mean"].idxmin()

    kpis = {
        "Best Performing Category": f"{best_category} ({avg_by_category.loc[best_category, 'mean']:.2f} hours)",
        "Worst Performing Category": f"{worst_category} ({avg_by_category.loc[worst_category, 'mean']:.2f} hours)",
        "Overall Average Resolution": f"{df['resolution_time'].mean():.2f} hours",
    }

    # Generate insight
    insight = f"""Based on the analysis of resolution times in 2023:
    - {worst_category} issues take longest to resolve, averaging {avg_by_category.loc[worst_category, 'mean']:.2f} hours
    - {best_category} issues are resolved fastest, averaging {avg_by_category.loc[best_category, 'mean']:.2f} hours
    - The overall average resolution time is {df['resolution_time'].mean():.2f} hours
    - This suggests focusing improvement efforts on {worst_category} incident handling"""

    # Create markdown content
    markdown_content = f"""# ServiceNow Incident Analysis

## Question
{question}

## Answer
The analysis shows significant variations in high-priority incidents throughout 2023, with a peak in {max_month['month']}.

## Visualization
![Monthly Trend of High-Priority Incidents](plot.jpeg)

## Key Performance Indicators
- Total High Priority Incidents: {kpis['Total High Priority Incidents']}
- Average Monthly High Priority Incidents: {kpis['Average Monthly High Priority Incidents']}
- Peak Month: {kpis['Peak Month']}

## Insight
{insight}
"""

    # Save markdown file
    with open("analysis_report.md", "w") as f:
        f.write(markdown_content)

    return {
        "question": question,
        "answer": monthly_high_priority.to_dict(),
        "kpis": kpis,
        "insight": insight,
    }


if __name__ == "__main__":
    results = analyze_incidents()
    print("Analysis completed. Check analysis_report.md and plot.jpeg for results.")
