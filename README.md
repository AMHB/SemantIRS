# SemantIRS: IRS-Enhanced Semantic Offloading for Intelligent Transportation Systems

**Developer:** Ali Mehrban

---

## Overview

This repository contains all simulation codes, architectural assets, LaTeX tables, figures, and workflow diagrams for the SemantIRS framework—a state-of-the-art architecture that combines Intelligent Reflecting Surfaces (IRS) with edge-deployed lightweight LLMs and semantic offloading, optimized for Space-Air-Ground Integrated Networks (SAGIN) in next-generation Intelligent Transportation Systems (ITS).

- **SemantIRS** provides robust low-latency V2X connectivity, 82.6% latency reduction, 12dB IRS SNR gain, and 90% bandwidth savings validated through journal-level Python simulations.

---

## Contents

- **/simulation/**  
  Python simulation code for generating all performance results and data tables, including:
    - Raw, Semantic, Semantic+IRS simulation engines
    - Performance metric computation
    - Output CSV files
    - Jupyter/Notebook scripts

- **/assets/**  
  Architectural diagrams, draw.io XML files (e.g., Fig1 architecture), illustrative figures, and LaTeX table source code.

- **/results/**  
  Performance artifacts: CSV summary tables, multi-panel publication charts, finalized images for insertion into papers.

- **/docs/**  
  Complete LaTeX manuscript blocks, recommended text snippets for IEEE submissions, and summary explanation files.

---

## How to Reproduce Simulation Results

1. **Set up the Python environment**  
   - Requires Python 3.8+, numpy, pandas, matplotlib
   - (Optional: Jupyter Notebook for interactive runs)

2. **Run the main simulation script**  
   - Generates all baseline and optimized performance results
   - Outputs: `FINAL_OPTIMIZED_results.csv`, `FINAL_OPTIMIZED_comparison.csv`, and plots

3. **Open/modify draw.io diagrams**  
   - Use included `*.xml` files with [draw.io](https://draw.io) for custom visualizations

4. **Insert figures and tables**  
   - Provided as ready-to-use LaTeX tabular/code or figure PNGs

---

## Key Features

- **Full SAGIN architecture with real-world constraints**
- V2I (green), I2A (blue), and A2S (purple) links for full network realism
- Realistic CAV, RSU (with IRS), UAV, HAP, and LEO satellite assets
- Federated Learning, Semantic Compression, Security Overlay visualized
- All performance claims traced to simulation or referenced literature

---

## Contact

For questions, discussion, or academic collaboration, contact:  
**Ali Mehrban**  
a.mehrban@ieee.org

---

Collaborations and further contributions are welcome.
