"""
MCP Server for Cervical Vestibular Evoked Myogenic Potentials (cVEMP) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating p13-n23 latencies, amplitude asymmetry, and saccular otolith integrity.
"""

import sys
import json
from typing import Dict, Any
from client import CervicalVEMPClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_cvemp",
                "description": "Calculates Cervical Vestibular Evoked Myogenic Potentials (cVEMP) parameters including p13-n23 latencies, interaural asymmetry ratio (IAR), and saccular otolith integrity score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "p13_latency_ms": {
                            "type": "number",
                            "description": "Positive p13 peak latency in milliseconds (e.g. 13.2 ms, normative 11.5 - 15.0 ms)."
                        },
                        "n23_latency_ms": {
                            "type": "number",
                            "description": "Negative n23 peak latency in milliseconds (e.g. 22.8 ms, normative 20.0 - 25.5 ms)."
                        },
                        "peak_to_peak_amplitude_uv": {
                            "type": "number",
                            "description": "Ipsilateral peak-to-peak biphasic p13-n23 amplitude in microvolts (e.g. 75.0 uV)."
                        },
                        "contralateral_amplitude_uv": {
                            "type": "number",
                            "description": "Contralateral ear peak-to-peak amplitude in microvolts for calculating Interaural Asymmetry Ratio (optional, e.g. 80.0 uV)."
                        },
                        "mean_background_emg_uv": {
                            "type": "number",
                            "description": "Mean tonic sternocleidomastoid background electromyographic activity in microvolts for amplitude normalization (optional, e.g. 60.0 uV)."
                        }
                    },
                    "required": ["p13_latency_ms", "n23_latency_ms", "peak_to_peak_amplitude_uv"]
                }
            }
        ]
    }


def handle_request(client: CervicalVEMPClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_cvemp":
            contra = args.get("contralateral_amplitude_uv")
            emg = args.get("mean_background_emg_uv")
            res = client.evaluate_cvemp(
                p13_latency_ms=float(args.get("p13_latency_ms", 13.0)),
                n23_latency_ms=float(args.get("n23_latency_ms", 22.5)),
                peak_to_peak_amplitude_uv=float(args.get("peak_to_peak_amplitude_uv", 70.0)),
                contralateral_amplitude_uv=float(contra) if contra is not None else None,
                mean_background_emg_uv=float(emg) if emg is not None else None
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = CervicalVEMPClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
