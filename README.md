<div align="center">
  <img src="./banner.svg" alt="artifact-tracker" width="800">
</div>

# artifact-tracker

> Log artefacts dropped during an engagement for clean-up

Part of a red-team tooling collection for **authorised** security testing.

## Install

```bash
git clone https://github.com/amooryx/artifact-tracker.git
cd artifact-tracker
```

## Usage

```bash
python artifact_tracker.py <target>
```

| Flag | Description |
|---|---|
| `-o, --output` | Write results to a file |
| `-v, --verbose` | Verbose output |
| `-y, --yes` | Skip the authorisation prompt |

## Disclaimer

> **Authorised security testing only.** Use this against systems you own or have
> explicit written permission to test. The tool prompts for authorisation before
> acting and is provided for professional engagements, labs, and research.

## Author

**Omar Khalid** — [omareldemery.com](https://omareldemery.com) | [@amooryx](https://github.com/amooryx)

Certifications: OSCP+ · OSCP · CRTP · eWPTX · eCPPT · eCDFP · eCIR · eJPT
