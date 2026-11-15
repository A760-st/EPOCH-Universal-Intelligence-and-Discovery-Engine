# ADR-001: Independent Statistical and Integrity Engine

**Status:** Accepted  
**Date:** 13 November 2026  
**Owner:** Adithya

## Context

EPOCH requires statistical analysis, deterministic dataset handling,
lineage protection and verdict evaluation.

These responsibilities must remain consistent regardless of which backend,
frontend or execution infrastructure invokes them.

## Decision

Implement these responsibilities as an independent Python package named
`epoch-engine`.

The package uses a source layout:

`packages/epoch_engine/src/epoch_engine/`

The engine exposes reusable Python interfaces rather than directly
implementing web routes or database operations.

## Ownership Boundary

Adithya owns the engine implementation.

Other team components interact with it through agreed interfaces:

- Backend: API, persistence and workflow coordination.
- Executor: isolated execution and security.
- Frontend: user workflows and evidence presentation.

## Consequences

### Benefits

- Independent testing of statistical and integrity logic.
- Reduced coupling between team modules.
- Easier reproducibility and verification.
- Clear ownership and integration boundaries.

### Constraints

- Engine interfaces must be documented.
- Backend and executor must not duplicate engine calculations.
- Runtime secrets must be injected securely.
- Changes to shared contracts require coordination.

## Verification Status

The initial Python package structure exists.

The architecture boundary is documented, but implementation-level
compliance remains to be verified.
