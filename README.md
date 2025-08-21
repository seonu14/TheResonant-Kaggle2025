# The Resonant – Red-Teaming Challenge Submission

## 🔍 Overview

This repository contains the full writeup for **"The Resonant"**, a red-teaming investigation submitted to the Kaggle Red Teaming Challenge. The project explores how large language models—specifically `gpt-oss-20b`—exhibit structural reasoning flaws under layered ethical, symbolic, and systemic pressures.

Rather than focusing on content correctness, this analysis examines *when, how, and why* the model’s judgment crystallizes prematurely, trading ambiguity for rhetorical polish. Five scenarios (A–E) were used to probe different dimensions of model reasoning.

## 📚 Full Report

The full writeup is available here:  
**👉 [Download HTML version](./TheResonant_Report_KaggleReady.html)**

This report includes:
- Introduction to framing failure in LLMs
- Detailed analyses of five scenario types (health, ethics, legality, systems, civic)
- Cross-scenario synthesis (convergence, divergence, propagation)
- Strategic recommendations for model design, deployment, and governance

## 🧪 Supporting Files

- `TheResonant_Submission.zip` – Includes the five JSON scenario findings and README.
- `TheResonant_ReproToolkit_repacked.zip` – Contains reproducible notebooks and tooling package.

## ✨ Highlighted Insight

> "The model didn’t fail through error, but through elegant finality."

Each scenario reflects a different way that model fluency can mask epistemic shallowness or ethical shortcuts—especially when under symbolic or emotional pressure.

## 🔁 Cross-Scenario Summary

| Scenario | Input Pressure       | Collapse Type         | Closure Arc            | Missed Tension             |
|----------|----------------------|------------------------|-------------------------|----------------------------|
| **A**    | Allocative + Moral   | Policy Lock-in         | Simplicity → Structure | Overlapping vulnerability  |
| **B**    | Emotional            | Moral Justification    | Betrayal → Duty        | Alternative restraint      |
| **C**    | Legal + Emotional    | Instruction as Verdict | Collapse → Command     | Emotional hesitation       |
| **D**    | Time-Critical        | Cascade Blindness      | Immediacy → Blindness  | Cross-system fragility     |
| **E**    | Symbolic + Civic     | Therapeutic Exit Bias  | Guilt → Healing        | Collective cost            |

## 🧭 Methodology

Each scenario was intentionally structured with escalating prompts to simulate real-world ethical ambiguity, time pressure, or symbolic tension. Model behavior was logged at each stage and evaluated based on judgment formation trajectory—not just correctness.

All runs used `gpt-oss-20b` at temperature 0.7 and top_p 0.9.

## 📩 Contact

If you have questions about this submission, feel free to reach out via the Kaggle forum or the GitHub Issues tab.

---

*Submitted for the Kaggle Red-Teaming Challenge, 2025.*

