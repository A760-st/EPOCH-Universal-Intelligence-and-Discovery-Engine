# EPOCH Engineering Documentation Standard

**Status:** Mandatory project-wide standard
**Established:** 13 November 2026

## 1. Purpose

Maintain a complete, chronological and evidence-based engineering record
of EPOCH, from initial requirements and design through implementation,
testing, debugging, integration and final delivery.

Documentation is part of implementation, not a separate activity
performed only before submission.

## 2. General Rules

1. Every meaningful technical activity must be documented.
2. Record what was actually done, not what was merely planned.
3. Never fabricate test results, metrics, screenshots or verification.
4. Distinguish proposed, implemented, tested and verified functionality.
5. Record failed experiments and the corrections made.
6. Update relevant documentation when implementation changes.
7. Keep documentation consistent with the actual repository.
8. Record dates, versions, commands and relevant environment details.
9. Cross-reference related requirements, code, tests and decisions.
10. Document known limitations instead of hiding them.

## 3. Requirement Documentation

For every significant requirement, record:

- Requirement ID
- Requirement description
- Source or originating decision
- Technical interpretation
- Assumptions
- Acceptance criteria
- Dependencies
- Implementation status
- Verification evidence

## 4. Architecture and Design Documentation

Record:

- Problem being addressed
- Proposed design
- Component responsibilities
- Interfaces and data contracts
- Alternatives considered
- Reasons for design selection
- Security considerations
- Performance considerations
- Trade-offs
- Related architecture decision records

## 5. Implementation Documentation

For every meaningful implementation, record:

- Feature or module name
- Objective
- Files created or modified
- Public functions, classes and interfaces
- Input and output specifications
- Algorithm and processing steps
- Validation and error handling
- Dependencies
- Security considerations
- Relevant requirements
- Implementation status

## 6. Testing Documentation

Every test activity must record:

- Test ID
- Test category
- Test objective
- Requirement or function being verified
- Test environment and versions
- Preconditions
- Test data or fixture
- Exact execution command
- Expected result
- Actual result
- Pass, fail, blocked or not-run status
- Error output when applicable
- Root cause and correction when applicable
- Regression test evidence
- Relevant code and test file references
- Execution date

Test categories include:

- Unit testing
- Golden/reference-value testing
- Integration testing
- API/contract testing
- Boundary and negative testing
- Security testing
- Performance testing
- Reproducibility testing
- Acceptance testing

A test must not be marked passed unless its actual execution supports
that status.

## 7. Debugging and Defect Documentation

Record:

- Defect ID
- Date discovered
- Environment
- Reproduction steps
- Expected behavior
- Actual behavior
- Complete relevant error message
- Root cause
- Files affected
- Correction implemented
- Regression tests
- Final verification
- Remaining risks

## 8. Security and Performance Documentation

Security records must identify the threat, affected component, risk,
mitigation, verification method and residual risk.

Performance records must identify hardware, software versions, input
size, configuration, measurement method, observed results and limitations.

## 9. Git and Collaboration Documentation

Record significant:

- Branch creation and purpose
- Commits and changed files
- Pull requests
- Reviews and requested changes
- Merge decisions
- Integration conflicts
- Ownership and handoff evidence

Never record a commit, review or merge as successful without evidence.

## 10. Integration Documentation

Record:

- Participating components
- Owners
- Contract versions
- Request and response structures
- Compatibility requirements
- Integration procedure
- Integration test cases
- Actual results
- Unresolved issues
- Handoff status

## 11. Final Delivery Documentation

Record:

- Implemented requirements
- Verified acceptance criteria
- Test summary
- Reproducibility instructions
- Installation and execution instructions
- Architecture and deployment details
- Known limitations
- Outstanding risks
- Evidence and demonstration procedure

## 12. Evidence and Status Vocabulary

Use these statuses consistently:

- PROPOSED: design discussed but not implemented
- IMPLEMENTED: code or artifact created
- TESTED: relevant test executed
- VERIFIED: required acceptance evidence obtained
- FAILED: test or acceptance criterion failed
- BLOCKED: verification cannot proceed
- DEFERRED: intentionally postponed
- NOT RUN: no execution evidence exists

## 13. Documentation Maintenance

Update the development log chronologically.

Maintain detailed technical records in the relevant documentation files.
Do not overload the development log with every test's full output;
link to the detailed test report.

When a technical decision changes, update its decision record and explain
the reason. Preserve historical context rather than silently rewriting
the history.

Documentation completion is part of the definition of done for every
significant feature.
