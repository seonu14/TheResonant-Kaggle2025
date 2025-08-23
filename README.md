# The Resonant – Red-Teaming Challenge Submission

## 🔍 Overview

This repository contains the full writeup for **"The Resonant"**, a red-teaming investigation submitted to the Kaggle Red Teaming Challenge. The project explores how large language models—specifically `gpt-oss-20b`—exhibit structural reasoning flaws under layered ethical, symbolic, and systemic pressures.

Rather than focusing on content correctness, this analysis examines *when, how, and why* the model’s judgment crystallizes prematurely, trading ambiguity for rhetorical polish. Five scenarios (A–E) were used to probe different dimensions of model reasoning.

## 📚 Full Report

The full writeup is available in this repository:  
**👉 [`TheResonant_Report_KaggleReady.md`](./TheResonant_Report_KaggleReady.md)**  
It is also [viewable on GitHub](https://github.com/seonu14/TheResonant-Kaggle2025).

This report includes:
- Introduction to framing failure in LLMs  
- Detailed analyses of five scenario types (health, ethics, legality, systems, civic)  
- Cross-scenario synthesis (convergence, divergence, propagation)  
- Strategic recommendations for model design, deployment, and governance

## 📦 Files submitted

- `TheResonant_Submission.zip`  
  – Includes the five scenario finding files (`findings_1.json` to `findings_5.json`) and a submission-level `README.md`.

- `TheResonant_ReproToolkit.zip`  
  – Contains reproducible notebooks, evaluation runner (`prompt_runner.py`), and auxiliary files.  
    Organized into `/scenarios`, `/scenarios_outputs`, `/tools`, and `/tests`; includes `README.md` for guidance.

Please note:  
`TheResonant_ReproToolkit.zip` reflects the current stabilized structure of the toolkit.  
Minor updates may occur before submission, but the core format is expected to remain consistent.

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

*This repository was prepared for the 2025 Kaggle Red-Teaming Challenge.*  
Its goal is not only to report findings, but to offer methodological approaches for surfacing hidden risks and structural failure modes in LLMs.
