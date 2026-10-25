"""Generate all HW3 report figures from TensorBoard event logs."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FIGURES = ROOT / "figures"


def event_file(prefix):
    candidates = []
    for directory in DATA.glob(f"{prefix}_*"):
        events = list(directory.glob("events*"))
        if events:
            candidates.append((max(p.stat().st_size for p in events), directory, events[0]))
    if not candidates:
        raise FileNotFoundError(f"No completed event log found for {prefix}")
    return max(candidates)[2]


def scalars(prefix, tag, x_tag="Train_EnvstepsSoFar"):
    accumulator = EventAccumulator(str(event_file(prefix)), size_guidance={"scalars": 0})
    accumulator.Reload()
    x_by_step = {event.step: event.value for event in accumulator.Scalars(x_tag)}
    points = [(x_by_step[event.step], event.value) for event in accumulator.Scalars(tag)
              if event.step in x_by_step]
    return np.asarray(points, dtype=np.float64).T


def aggregate(prefixes, tag):
    runs = [scalars(prefix, tag) for prefix in prefixes]
    common_x = runs[0][0]
    ys = []
    for x, y in runs:
        ys.append(np.interp(common_x, x, y))
    return common_x, np.vstack(ys)


def plot_q1():
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    groups = {
        "DQN": [f"q1_dqn_{seed}" for seed in (1, 2, 3)],
        "Double DQN": [f"q1_doubledqn_{seed}" for seed in (1, 2, 3)],
    }
    colors = {"DQN": "#2563eb", "Double DQN": "#dc2626"}
    for label, prefixes in groups.items():
        for tag, linestyle, suffix in (
            ("Train_AverageReturn", "-", "average return"),
            ("Train_BestReturn", "--", "best return"),
        ):
            x, ys = aggregate(prefixes, tag)
            mean, std = ys.mean(axis=0), ys.std(axis=0)
            ax.plot(x, mean, linestyle, color=colors[label], label=f"{label} {suffix}")
            ax.fill_between(x, mean - std, mean + std, color=colors[label], alpha=0.14)
    ax.axhline(0, color="black", linewidth=0.7, alpha=0.4)
    ax.set(xlabel="Environment steps", ylabel="Per-epoch return",
           title="LunarLander-v3: DQN vs. Double DQN (mean $\\pm$ 1 std, 3 seeds)")
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
    ax.grid(alpha=0.22)
    ax.legend(fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(FIGURES / "q1_dqn_ddqn.pdf")
    plt.close(fig)


def plot_ac(prefix, title, filename):
    x, y = scalars(prefix, "Eval_AverageReturn")
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.plot(x, y, color="#7c3aed", linewidth=2)
    ax.set(xlabel="Environment steps", ylabel="Evaluation average return", title=title)
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
    ax.grid(alpha=0.22)
    fig.tight_layout()
    fig.savefig(FIGURES / filename)
    plt.close(fig)


def main():
    FIGURES.mkdir(exist_ok=True)
    plot_q1()
    plot_ac("q2_10_10", "Actor-Critic on CartPole-v0", "q2_cartpole.pdf")
    plot_ac("q3_10_10", "Actor-Critic on InvertedPendulum-v4", "q3_inverted_pendulum.pdf")


if __name__ == "__main__":
    main()
