# EPOCH Engine

The EPOCH Engine is the deterministic statistical and integrity core of the
Universal Intelligence and Discovery Engine.

## Responsibilities

The engine is intended to provide reusable functionality for:

- Dataset profiling
- Deterministic dataset splitting
- Dataset lineage and sticky split assignment
- Structured prediction validation
- Statistical verdict evaluation
- Confirmatory test-budget policy validation

## Architecture Boundary

The engine is designed as an independent Python package.

It must not directly depend on:

- FastAPI
- PostgreSQL
- Frontend implementation
- User-interface logic
- Backend persistence

The backend and isolated executor should interact with the engine through
defined interfaces.

## Source Layout

`src/epoch_engine/` contains the engine implementation.

| Module | Responsibility |
|---|---|
| profiling | Dataset profiling |
| splitting | Deterministic data splitting |
| lineage | Dataset lineage and matching |
| predictions | Structured prediction validation |
| verdicts | Statistical verdict evaluation |
| budgets | Confirmatory budget policy |

## Tests

- `tests/unit/`: individual function and module tests
- `tests/golden/`: reference-value and deterministic-output tests
- `tests/integration/`: interactions between engine components

## Development Status

Initial package structure created on 13 November 2026.

Implementation and automated verification are pending.

## Installation

From the repository root:

`python -m pip install -e "packages/epoch_engine[dev]"`

Install this only after reviewing the development environment and dependencies.
