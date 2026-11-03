"""
Example Usage: Cervical Vestibular Evoked Myogenic Potentials (cVEMP).
Demonstrates zero-dependency calculation of p13-n23 latency, normalized amplitude, and interaural asymmetry ratio (IAR).
"""

from client import CervicalVEMPClient


def main():
    client = CervicalVEMPClient()
    print("=== Cervical Vestibular Evoked Myogenic Potentials (cVEMP) Demo ===")

    # Test Case 1: Healthy symmetric saccular otolith response
    res1 = client.evaluate_cvemp(
        p13_latency_ms=13.2,
        n23_latency_ms=22.4,
        peak_to_peak_amplitude_uv=84.5,
        contralateral_amplitude_uv=79.0,
        mean_background_emg_uv=62.0
    )
    print("\nTest Case 1: Healthy Bilateral Saccular Balance")
    print(f"  p13 Latency: {res1['p13_latency_ms']} ms | n23 Latency: {res1['n23_latency_ms']} ms")
    print(f"  Peak-to-Peak Amplitude: {res1['peak_to_peak_amplitude_uv']} uV")
    print(f"  Interaural Asymmetry Ratio (IAR): {res1['interaural_asymmetry_ratio_pct']}%")
    print(f"  Normalized Amplitude: {res1['normalized_amplitude']}")
    print(f"  Saccular Otolith Score: {res1['saccular_otolith_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Asymmetric saccular hypofunction (high IAR)
    res2 = client.evaluate_cvemp(
        p13_latency_ms=14.8,
        n23_latency_ms=24.2,
        peak_to_peak_amplitude_uv=24.0,
        contralateral_amplitude_uv=88.0,
        mean_background_emg_uv=58.0
    )
    print("\nTest Case 2: Unilateral Saccular / Inferior Vestibular Nerve Deficit")
    print(f"  p13 Latency: {res2['p13_latency_ms']} ms | n23 Latency: {res2['n23_latency_ms']} ms")
    print(f"  Peak-to-Peak Amplitude: {res2['peak_to_peak_amplitude_uv']} uV vs Contra {res2['contralateral_amplitude_uv']} uV")
    print(f"  Interaural Asymmetry Ratio (IAR): {res2['interaural_asymmetry_ratio_pct']}%")
    print(f"  Saccular Otolith Score: {res2['saccular_otolith_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
