# 16-831 Homework 3

The submission contains the completed `rob831` package and the required
TensorBoard run logs for Questions 1--3.

## Setup

From the extracted `submit` directory, install the provided requirements and package:

```bash
pip install -r requirements.txt
pip install -e .
```

## Reproducing experiments

Run the commands specified in the assignment handout. The included Q1 runs use
`gamma=0.99`, target-network updates every 2,000 steps, and epsilon decay over
the first 90,000 steps. They retain the required experiment names. To
regenerate the report figures from the included logs, run:

```bash
python plot_hw3.py
```

The script writes the three PDF figures to `figures/`.

No special code changes or extra Python dependencies beyond the provided
requirements are needed. On macOS, InvertedPendulum also requires the native
GLFW library (for example, `conda install -c conda-forge glfw`).
