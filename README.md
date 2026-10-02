# CyberSentinel

CyberSentinel is a local-first, defensive cybersecurity assessment platform
written in Python.

It is an educational and portfolio project designed to demonstrate secure Python
development, local security assessment, network fundamentals, file integrity
monitoring, reporting, APIs, testing, Docker, and CI/CD.

> **Authorized use only**
>
> Use CyberSentinel only on localhost, systems you own, or systems and networks
> for which you have explicit authorization to perform security assessment.
> CyberSentinel is not designed for exploitation, credential attacks, stealth,
> evasion, persistence, phishing, ransomware, or unauthorized access.

## Project status

CyberSentinel is under incremental development.

- Phase 1: Project architecture and environment setup — complete
- Phase 2: Password analyzer — planned
- Phase 3: Network information — planned
- Phase 4: Authorized TCP scanner — planned
- Phase 5: File integrity monitoring — planned
- Phase 6: Deterministic risk engine — planned
- Phase 7: Reports — planned
- Phase 8: SQLite persistence — planned
- Phase 9: FastAPI backend — planned
- Phase 10: Dashboard — planned
- Phase 11: Testing and code quality — planned
- Phase 12: Docker — planned
- Phase 13: GitHub Actions — planned
- Phase 14: AI explanation layer — planned
- Phase 15: Final audit and portfolio polish — planned

## Planned features

- Local-only password-strength analysis
- Local network and system information gathering
- Controlled, authorized TCP connect scanning
- SHA-256 file-integrity baselines and comparisons
- Transparent deterministic risk scoring
- Terminal, JSON, CSV, and HTML reports
- SQLite scan history and metadata
- FastAPI REST API and OpenAPI documentation
- Responsive web dashboard
- Automated tests, Docker, and GitHub Actions

## Architecture

```text
app/
├── core/        Shared logging, scan orchestration, and risk logic
├── network/     Local network information and authorized TCP scanning
├── password/    Local-only password analysis
├── integrity/   Read-only file integrity monitoring
├── reports/     Report rendering and export
├── database/    SQLite and SQLAlchemy models
└── api/         FastAPI routes
```

## Requirements

- Python 3.12 or newer
- pip
- Git recommended

## Installation

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Current usage

Show CLI help:

```bash
python main.py --help
```

Check setup status:

```bash
python main.py status
```

Show version:

```bash
python main.py --version
```

## Testing

```bash
python -m pytest
```

## Code quality

```bash
python -m ruff check .
python -m ruff format --check .
```

## Security model

- Passwords will be analyzed locally only.
- Passwords, credentials, tokens, and private keys must never be stored or logged.
- File monitoring will be read-only.
- Network functionality will be restricted to controlled TCP connect checks.
- Users are responsible for confirming authorization before scanning any target.
- CyberSentinel will not implement exploitation, brute force, credential theft,
  persistence, evasion, phishing, ransomware, or destructive behavior.

## Limitations

CyberSentinel is an educational tool, not a replacement for professional
penetration testing, enterprise endpoint protection, vulnerability management,
or incident response processes. A reachable open TCP port does not itself prove
a vulnerability.

## License

MIT License. See `LICENSE`.