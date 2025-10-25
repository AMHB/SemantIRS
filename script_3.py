
# Create detailed comparison table
comparison_summary = pd.DataFrame({
    'Metric': [
        'Mean Latency (ms)',
        '95th Percentile Latency (ms)',
        'Latency Std Dev (ms)',
        'Latency Reduction (%)',
        'Mean Energy (mJ)',
        'Energy Savings (%)',
        'Mean SNR (dB)',
        'SNR with IRS (dB)',
        'IRS Gain (dB)',
        'Datarate (Mbps)',
        'Packet Success Rate (%)',
        'Bandwidth Usage (KB)',
        'Bandwidth Savings (%)',
        'Avg Distance (m)'
    ],
    'Raw (No IRS)': [
        f"{final_metrics_raw['Mean_Latency_ms']:.1f}",
        f"{final_metrics_raw['95th_Percentile_ms']:.1f}",
        f"{final_metrics_raw['Std_Latency_ms']:.1f}",
        "0.0",
        f"{final_metrics_raw['Mean_Energy_mJ']:.1f}",
        "0.0",
        f"{final_metrics_raw['Mean_SNR_dB']:.1f}",
        "N/A",
        "0.0",
        f"{final_metrics_raw['Mean_Datarate_Mbps']:.1f}",
        f"{final_metrics_raw['Success_Rate_%']:.0f}",
        f"{final_metrics_raw['Bandwidth_KB']:.0f}",
        "0.0",
        f"{final_metrics_raw['Mean_Distance_m']:.1f}"
    ],
    'Semantic (No IRS)': [
        f"{final_metrics_sem['Mean_Latency_ms']:.1f}",
        f"{final_metrics_sem['95th_Percentile_ms']:.1f}",
        f"{final_metrics_sem['Std_Latency_ms']:.1f}",
        f"{((final_metrics_raw['Mean_Latency_ms']-final_metrics_sem['Mean_Latency_ms'])/final_metrics_raw['Mean_Latency_ms']*100):.1f}",
        f"{final_metrics_sem['Mean_Energy_mJ']:.1f}",
        f"{((final_metrics_raw['Mean_Energy_mJ']-final_metrics_sem['Mean_Energy_mJ'])/final_metrics_raw['Mean_Energy_mJ']*100):.1f}",
        f"{final_metrics_sem['Mean_SNR_dB']:.1f}",
        "N/A",
        "0.0",
        f"{final_metrics_sem['Mean_Datarate_Mbps']:.1f}",
        f"{final_metrics_sem['Success_Rate_%']:.0f}",
        f"{final_metrics_sem['Bandwidth_KB']:.0f}",
        f"{final_metrics_sem['Compression_%']:.0f}",
        f"{final_metrics_sem['Mean_Distance_m']:.1f}"
    ],
    'Semantic + IRS': [
        f"{final_metrics_sem_irs['Mean_Latency_ms']:.1f}",
        f"{final_metrics_sem_irs['95th_Percentile_ms']:.1f}",
        f"{final_metrics_sem_irs['Std_Latency_ms']:.1f}",
        f"{latency_reduction:.1f}",
        f"{final_metrics_sem_irs['Mean_Energy_mJ']:.1f}",
        "N/A",  # Energy calc issue
        f"{final_metrics_sem_irs['Mean_SNR_dB']:.1f}",
        f"{final_metrics_sem_irs['Mean_SNR_dB']:.1f}",
        f"{final_metrics_sem_irs['IRS_Gain_dB']:.1f}",
        f"{final_metrics_sem_irs['Mean_Datarate_Mbps']:.1f}",
        f"{final_metrics_sem_irs['Success_Rate_%']:.0f}",
        f"{final_metrics_sem_irs['Bandwidth_KB']:.0f}",
        f"{final_metrics_sem_irs['Compression_%']:.0f}",
        f"{final_metrics_sem_irs['Mean_Distance_m']:.1f}"
    ]
})

print("\n" + "="*70)
print("DETAILED PERFORMANCE COMPARISON TABLE")
print("="*70)
print(comparison_summary.to_string(index=False))

comparison_summary.to_csv('FINAL_DETAILED_comparison.csv', index=False)

print("\n✅ Detailed comparison table saved: FINAL_DETAILED_comparison.csv")
