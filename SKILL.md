---
name: genpark-personal-agent-postural-vestibular-cervical-vemp-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Cervical Vestibular Evoked Myogenic Potentials (cVEMP), p13-n23 latency, Interaural Asymmetry Ratio (IAR), and saccular otolith integrity.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cervical Vestibular Evoked Myogenic Potentials (cVEMP) Skill

A sovereign personal agent capability for assessing saccular macula otolith function, inferior vestibular nerve conduction velocity, and the vestibulocollic reflex maintaining head-on-body gravitational posture.

## Core Capabilities
- **Biphasic Waveform Analysis**: Evaluates positive p13 (11.5 - 15.0 ms) and negative n23 (20.0 - 25.5 ms) acoustic/mechanical evoke latencies.
- **Interaural Asymmetry Ratio (IAR)**: Computes Jongkees formula across bilateral sternocleidomastoid responses to isolate unilateral vestibular loss.
- **EMG Amplitude Normalization**: Normalizes p13-n23 microvolt amplitude against background tonic muscle activation for reproducible monitoring.
- **Gravitational Verticality Index**: Determines resilience against vestibular drop attacks, sagittal sway instability, and otolith-mediated motion sickness.

## Fast Invocation
```python
from client import CervicalVEMPClient

client = CervicalVEMPClient()
res = client.evaluate_cvemp(
    p13_latency_ms=13.2,
    n23_latency_ms=22.4,
    peak_to_peak_amplitude_uv=84.5,
    contralateral_amplitude_uv=79.0,
    mean_background_emg_uv=62.0
)
print("IAR Pct:", res["interaural_asymmetry_ratio_pct"], "%")
print("Otolith Score:", res["saccular_otolith_score"])
```
