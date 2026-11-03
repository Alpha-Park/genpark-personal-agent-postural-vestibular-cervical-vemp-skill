"""
Cervical Vestibular Evoked Myogenic Potentials (cVEMP) & Saccular Otolith Engine.
Provides deterministic, zero-dependency modeling of p13-n23 biphasic peak latencies,
EMG-normalized amplitudes, Jongkees Interaural Asymmetry Ratio (IAR), and linear acceleration otolith integrity.
"""

from typing import Dict, Any, List, Optional


class CervicalVEMPClient:
    """
    Deterministic client for calculating Cervical Vestibular Evoked Myogenic Potentials (cVEMP).
    Assesses saccular macula otolith function, inferior vestibular nerve conduction,
    and vestibulocollic reflex pathways that maintain head-on-body gravitational posture.
    """

    def __init__(self):
        pass

    def evaluate_cvemp(
        self,
        p13_latency_ms: float,
        n23_latency_ms: float,
        peak_to_peak_amplitude_uv: float,
        contralateral_amplitude_uv: Optional[float] = None,
        mean_background_emg_uv: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates normalized amplitude and Interaural Asymmetry Ratio (IAR).
        Normative values for 500 Hz tone burst:
        - p13 latency: 11.5 - 15.0 ms
        - n23 latency: 20.0 - 25.5 ms
        - p13-n23 amplitude: 35.0 - 160.0 uV
        - IAR: < 34.0%
        """
        if p13_latency_ms <= 0 or n23_latency_ms <= p13_latency_ms:
            return {"error": "Invalid peak latencies: n23 must exceed p13 and both must be positive"}
        if peak_to_peak_amplitude_uv < 0:
            return {"error": "Peak-to-peak amplitude must be non-negative"}

        # Normalized amplitude relative to tonic sternocleidomastoid EMG contraction
        normalized_amp = None
        if mean_background_emg_uv and mean_background_emg_uv > 0:
            normalized_amp = round(peak_to_peak_amplitude_uv / mean_background_emg_uv, 2)

        # Interaural Asymmetry Ratio: IAR = (|A_L - A_R| / (A_L + A_R)) * 100
        iar_pct = None
        if contralateral_amplitude_uv is not None and contralateral_amplitude_uv >= 0:
            denom = peak_to_peak_amplitude_uv + contralateral_amplitude_uv
            if denom > 0:
                iar_pct = round((abs(peak_to_peak_amplitude_uv - contralateral_amplitude_uv) / denom) * 100.0, 1)
            else:
                iar_pct = 0.0

        # Saccular Otolith Resilience Score (0 - 100):
        # Normal p13 (12-14.5 ms) and IAR < 25% -> 88 - 98.
        # IAR > 45% or absent amplitude -> < 45.
        score = 80.0
        if 12.0 <= p13_latency_ms <= 14.5:
            score += 10.0
        elif p13_latency_ms > 16.5:
            score -= 20.0
        elif p13_latency_ms > 15.0:
            score -= 10.0

        if iar_pct is not None:
            if iar_pct <= 20.0:
                score += 10.0
            elif iar_pct > 40.0:
                score -= 30.0
            elif iar_pct > 32.0:
                score -= 15.0

        if peak_to_peak_amplitude_uv < 20.0:
            score -= 25.0

        otolith_score = round(min(100.0, max(5.0, score)), 1)

        is_asymmetric = iar_pct is not None and iar_pct >= 34.0
        has_delayed_latency = p13_latency_ms > 15.2

        if otolith_score >= 85.0 and not is_asymmetric:
            tier = "OPTIMAL_OTOLITH_GRAVITATIONAL_FUNCTION"
            interp = f"Crisp saccular vestibulocollic reflex (p13 {p13_latency_ms} ms, n23 {n23_latency_ms} ms, Amp {peak_to_peak_amplitude_uv} uV); robust otolith-cervical conduction."
            guidance = "Superior vertical gravitational and linear acceleration sensing. Optimal postural verticality preservation."
        elif not is_asymmetric and not has_delayed_latency:
            tier = "SYMMETRIC_SACCULAR_RESPONSIVENESS"
            interp = f"Preserved cVEMP waveform (p13 {p13_latency_ms} ms); balanced bilateral linear otolithic reflexes."
            guidance = "Normal otolith function. Maintain routine dynamic balance and neck mobility exercises."
        elif is_asymmetric:
            tier = "SIGNIFICANT_OTOLITH_INTERAURAL_ASYMMETRY"
            interp = f"Marked interaural amplitude asymmetry (IAR {iar_pct}% >= 34%); indicates unilateral saccular macula or inferior vestibular nerve hypofunction."
            guidance = "Significant otolithic imbalance detected. Practice stable-surface gaze anchoring and consult neuro-otology."
        else:
            tier = "DELAYED_VESTIBULOCOLLIC_LATENCY"
            interp = f"Prolonged p13 latency ({p13_latency_ms} ms > 15.0 ms); reflects slowed reticulospinal or vestibulospinal conduction."
            guidance = "Delayed reflex arc. Screen for cervical spine tension, nerve root compression, or central demyelination."

        return {
            "p13_latency_ms": p13_latency_ms,
            "n23_latency_ms": n23_latency_ms,
            "peak_to_peak_amplitude_uv": peak_to_peak_amplitude_uv,
            "contralateral_amplitude_uv": contralateral_amplitude_uv,
            "interaural_asymmetry_ratio_pct": iar_pct,
            "normalized_amplitude": normalized_amp,
            "saccular_otolith_score": otolith_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
