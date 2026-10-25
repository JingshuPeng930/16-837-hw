# 16-831 Homework 3

The submission contains the completed `rob831` package and the required
TensorBoard run logs for Questions 1--3.

## Setup

From the homework 3 directory, install the provided requirements and package:

```bash
pip install -r requirements.txt
pip install -e .
```

## Reproducing experiments

Run the commands specified in the assignment handout. The included runs use the
default hyperparameters and experiment names. To regenerate the report figures
from logs, run:

```bash
python plot_hw3.py
```

No special code changes or extra Python dependencies beyond the provided
requirements are needed. On macOS, InvertedPendulum also requires the native
GLFW library (for example, `conda install -c conda-forge glfw`).
