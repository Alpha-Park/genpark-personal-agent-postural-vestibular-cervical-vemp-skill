# Cervical Vestibular Evoked Myogenic Potentials (cVEMP) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Cervical Vestibular Evoked Myogenic Potentials (cVEMP), p13-n23 peak latencies, Interaural Asymmetry Ratio (IAR), and saccular otolith integrity.

```mermaid
flowchart TD
    AcousticStim["Acoustic 500 Hz Tone Burst Stimulus"] --> SaccularMacula["Saccular Macula Otolith Activation"]
    SaccularMacula --> InfVestibular["Inferior Vestibular Nerve Conduction"]
    InfVestibular --> Vestibulocollic["Vestibulospinal Reflex Arc"]
    Vestibulocollic --> SCM_EMG["Sternocleidomastoid (SCM) Inhibitory Dip (p13-n23)"]
    SCM_EMG --> MathIAR["Interaural Asymmetry Ratio (IAR) Calculation"]
    MathIAR --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Vestibular Electrophysiology Standards**: Formulates p13 and n23 peak latencies, background tonic SCM EMG normalization, and Jongkees interaural asymmetry.
- **Saccular Otolith Resilience**: Detects unilateral vestibular hypofunction, Tullio phenomenon, and linear acceleration perception decline.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CervicalVEMPClient

client = CervicalVEMPClient()
result = client.evaluate_cvemp(
    p13_latency_ms=13.2,
    n23_latency_ms=22.4,
    peak_to_peak_amplitude_uv=84.5,
    contralateral_amplitude_uv=79.0,
    mean_background_emg_uv=62.0
)
print("Interaural Asymmetry Ratio:", result["interaural_asymmetry_ratio_pct"], "%")
print("Classification:", result["classification"])
```

## License
Apache-2.0
