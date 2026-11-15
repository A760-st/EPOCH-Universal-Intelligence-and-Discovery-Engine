# EPOCH Engine Testing Strategy

## Purpose

Define how the statistical and integrity engine will be tested.

## Test Categories

### Unit Tests

Verify individual functions independently.

Examples:
- Dataset profiling
- Split assignment
- Lineage matching
- Prediction validation
- Verdict evaluation
- Budget policy validation

### Golden Tests

Compare deterministic outputs against independently calculated
reference values.

References should be supported by hand calculations or trusted
independent statistical implementations where appropriate.

### Integration Tests

Verify interactions between engine modules and public interfaces.

### Reproducibility Tests

Verify that identical inputs, configuration and seeds produce
the expected reproducible outputs.

## Testing Rules

- Every implemented module must have corresponding tests.
- Important statistical calculations require reference-value tests.
- Boundary conditions must be tested.
- Invalid inputs must fail explicitly.
- Tests must not silently modify input data.
- Test results must be recorded with commands and observed outcomes.

## Current Status

Test directory structure created on 13 November 2026.

No automated tests have been implemented or executed yet.
