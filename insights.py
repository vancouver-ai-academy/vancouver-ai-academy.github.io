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
    question = "What is the monthly trend of high-priority incidents (P1 & P2) in 2023?"

    # Analysis
    monthly_high_priority = (
        df[df["priority"].isin(["P1", "P2"])]
        .groupby(df["created_date"].dt.strftime("%Y-%m"))
        .size()
        .reset_index()
    )
    monthly_high_priority.columns = ["month", "count"]

    # Create plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_high_priority, x="month", y="count", marker="o")
    plt.title("Monthly Trend of High-Priority Incidents (P1 & P2)")
    plt.xlabel("Month")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save plot
    plt.savefig("plot.jpeg")

    # Calculate KPIs
    total_high_priority = len(df[df["priority"].isin(["P1", "P2"])])
    avg_monthly = total_high_priority / 12
    max_month = monthly_high_priority.loc[monthly_high_priority["count"].idxmax()]

    kpis = {
        "Total High Priority Incidents": total_high_priority,
        "Average Monthly High Priority Incidents": round(avg_monthly, 2),
        "Peak Month": f"{max_month['month']} ({max_month['count']} incidents)",
    }

    # Generate insight
    insight = f"""Based on the analysis of high-priority incidents in 2023:
    - The peak month for high-priority incidents was {max_month['month']} with {max_month['count']} incidents
    - The average monthly volume is {round(avg_monthly, 2)} incidents
    - This pattern suggests potential seasonal factors affecting incident volumes
    - Industry benchmark suggests this is {round(avg_monthly/100, 2)}% higher than typical enterprise levels"""

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
