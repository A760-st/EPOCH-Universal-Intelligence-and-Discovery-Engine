# EPOCH Integration Contract Register

## Purpose

Track interfaces shared between the engine and other EPOCH components.

## Participants

| Component | Owner | Responsibility |
|---|---|---|
| Statistical and Integrity Engine | Adithya | Pure engine logic |
| Backend Platform | Sushma Gouda | API and persistence |
| Execution Infrastructure | Atul Dhull | Isolated execution |
| Frontend | Pranav Aditya | User workflows and presentation |

## Contract Register

| Contract | Status |
|---|---|
| Dataset profiling input/output | Pending |
| Dataset splitting input/output | Pending |
| Dataset lineage interface | Pending |
| Structured prediction schema | Pending |
| Verdict evaluation interface | Pending |
| Budget policy interface | Pending |
| Engine CLI interface | Pending |

## Change Management

Shared contracts must be documented before integration.

A contract change must identify:
- Changed fields or function signatures
- Reason for the change
- Affected components
- Compatibility implications
- Required tests
- Approval or coordination evidence

No undocumented assumptions should be treated as finalized interfaces.
