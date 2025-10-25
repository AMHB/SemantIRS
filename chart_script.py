import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Load the data files
results_df = pd.read_csv("FINAL_OPTIMIZED_results.csv")
comparison_df = pd.read_csv("FINAL_OPTIMIZED_comparison.csv")

# Extract latency data for each mode
raw_data = results_df[results_df['mode'] == 'raw']['total_latency_ms'].values
semantic_data = results_df[results_df['mode'] == 'semantic']['total_latency_ms'].values
semantic_irs_data = results_df[results_df['mode'] == 'semantic_irs']['total_latency_ms'].values

# Calculate means
raw_mean = np.mean(raw_data)
semantic_mean = np.mean(semantic_data)
semantic_irs_mean = np.mean(semantic_irs_data)

print(f"Raw mean: {raw_mean:.1f} ms")
print(f"Semantic mean: {semantic_mean:.1f} ms")
print(f"Semantic+IRS mean: {semantic_irs_mean:.1f} ms")

# Create CDF data for each mode
def create_cdf(data):
    sorted_data = np.sort(data)
    n = len(sorted_data)
    cdf_values = np.arange(1, n + 1) / n
    return sorted_data, cdf_values

# Generate CDF data
raw_x, raw_cdf = create_cdf(raw_data)
semantic_x, semantic_cdf = create_cdf(semantic_data)
semantic_irs_x, semantic_irs_cdf = create_cdf(semantic_irs_data)

# Create the figure
fig = go.Figure()

# Add CDF traces with updated names that include mean values
fig.add_trace(go.Scatter(
    x=raw_x,
    y=raw_cdf,
    name=f'Raw ({raw_mean:.1f}ms)',
    line=dict(color='#DB4545', width=2),
    mode='lines'
))

fig.add_trace(go.Scatter(
    x=semantic_x,
    y=semantic_cdf,
    name=f'Semantic ({semantic_mean:.1f}ms)',
    line=dict(color='#D2BA4C', width=2),
    mode='lines'
))

fig.add_trace(go.Scatter(
    x=semantic_irs_x,
    y=semantic_irs_cdf,
    name=f'S+IRS ({semantic_irs_mean:.1f}ms)',
    line=dict(color='#2E8B57', width=2),
    mode='lines'
))

# Add vertical lines at means (without annotations per strict instructions)
fig.add_vline(x=raw_mean, line_dash="dash", line_color='#DB4545', opacity=0.7)
fig.add_vline(x=semantic_mean, line_dash="dash", line_color='#D2BA4C', opacity=0.7)
fig.add_vline(x=semantic_irs_mean, line_dash="dash", line_color='#2E8B57', opacity=0.7)

# Update layout
fig.update_layout(
    title="(a) End-to-End Latency CDF",
    xaxis_title="Latency (ms)",
    yaxis_title="CDF",
    xaxis=dict(range=[0, 200]),
    yaxis=dict(range=[0, 1], tickvals=[0, 0.2, 0.4, 0.6, 0.8, 1.0]),
    showlegend=True,
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=1.05, 
        xanchor='center', 
        x=0.5,
        font=dict(size=12)
    )
)

fig.update_xaxes(showgrid=True)
fig.update_yaxes(showgrid=True)

# Save the chart
fig.write_image("latency_cdf.png")
fig.write_image("latency_cdf.svg", format="svg")

print("Chart saved successfully!")