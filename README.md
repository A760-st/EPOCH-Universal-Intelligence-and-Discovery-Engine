# EPOCH

### An evidence-grounded discovery and experimentation workspace

EPOCH is a proposed workspace for taking a bounded research question and
dataset through a transparent, reproducible investigation. It connects
evidence, competing hypotheses, approved computational tests, results, and
revisions so researchers and reviewers can see how a conclusion was reached.

> **Project status:** Research and architecture proposal. This repository
> currently contains planning documents; the application has not yet been
> implemented. Product assumptions, the initial research domain, and dataset
> still need to be validated.

## Why EPOCH?

Research work often spans separate tools for exploring data, drafting
hypotheses, running analyses, and recording decisions. That can make it hard
to trace a result back to its data, assumptions, method, and limitations.

EPOCH is designed to make those connections explicit. It assists the
researcher and records the process; it does not certify truth, guarantee
novelty, or replace human judgment.

## The investigation workflow

1. Define a research question and select an approved dataset.
2. Explore the data and record relevant evidence.
3. Draft competing hypotheses.
4. Plan an allow-listed test and review its assumptions.
5. The researcher approves the test or sends it back for revision.
6. Run the approved test reproducibly.
7. Review the results and limitations, then revise the hypotheses and report.

Each investigation is intended to preserve the links between:

- **Evidence** — sources, dataset fields, analyses, and researcher annotations.
- **Hypotheses** — claims, assumptions, predictions, supporting evidence, and
  counter-evidence.
- **Tests and runs** — approved methods, dataset versions, parameters,
  environment details, metrics, and artifacts.
- **Revisions** — the reasoning behind retaining, changing, or rejecting a
  hypothesis.

## Proposed MVP

The first demonstrator is intentionally narrow: one research domain, one
documented public tabular dataset, and one complete investigation workflow.

Planned capabilities include:

- A workspace for research investigations.
- Dataset upload, versioning, schema inspection, and data-quality summaries.
- Exploratory analysis and saved observations.
- Structured editing of competing, falsifiable hypotheses.
- AI-assisted drafting and critique, with human review.
- A small catalogue of appropriate, allow-listed statistical or ML tests.
- Explicit approval before a test runs.
- Isolated experiment execution with recorded inputs and outputs.
- Result review, hypothesis history, and a traceable report.

Arbitrary code execution, automated causal discovery, broad cross-domain
claims, and multi-agent orchestration are outside the initial scope.

## Principles and safeguards

- **Human judgment stays central.** People choose the question, approve tests,
  interpret results, and decide how conclusions change.
- **AI is an assistant, not a source of results.** Computed results come from
  the analysis; AI must not invent them or fabricate citations.
- **Methods are inspectable.** Show assumptions, limitations, and the basis
  for each test and conclusion.
- **Runs are reproducible.** Preserve dataset versions, parameters, software
  versions, logs, and artifacts.
- **Execution is constrained.** Use allow-listed tests and an isolated,
  resource-limited worker; do not run arbitrary generated code in the web
  server.
- **Claims remain bounded.** Observational correlations alone do not establish
  causation, and a result does not prove a hypothesis.

## Proposed architecture

The consolidated proposal describes a modular application with a React and
TypeScript frontend, a Python and FastAPI API, PostgreSQL for records, queue,
and audit chain, and isolated executors for approved experiments. Object
storage is part of the hosted deployment path. AI is optional and does not
perform statistical computation.

These are proposed choices, not implemented technologies. See the
[consolidated system architecture](./EPOCH_Final_System_Architecture_v2.md)
for the design, data model, safeguards, build order, and open decisions.

## Project documents

| Document | Description |
| --- | --- |
| [Consolidated system architecture](./EPOCH_Final_System_Architecture_v2.md) | Current architecture baseline, integrity core, data model, safeguards, build order, and open decisions. |
| [Adithya — Technical Lead and Integrity Engine](./EPOCH_Work_Division_1_Adithya.pdf) | 30% allocation: engine contract, data and split logic, prediction validation, verdict evaluation, CLI, and integration. |
| [Sushma Gouda — Backend Platform and Workflow API](./EPOCH_Work_Division_2_Sushma_Gouda.pdf) | 30% allocation: API, database and migrations, access control, workflow state, run ledger, and audit persistence. |
| [Atul Dhull — Execution, Sandbox, and Verification](./EPOCH_Work_Division_3_Atul_Dhull.pdf) | 25% allocation: executor lifecycle, job execution, sandbox isolation, artifact handling, security tests, and reproducibility. |
| [Pranav Aditya — Frontend and User Documentation](./EPOCH_Person_4_Pranav_Aditya_Work_Plan.pdf) | 15% allocation: investigation workflow UI, evidence and result presentation, API integration, frontend tests, and user/demo documentation. |

The work plans assign ownership, deliverables, dependencies, and acceptance
criteria for each role. They are plans, not claims that the assigned work has
been completed.

## Current focus

Before implementation, the team needs to decide on the initial scientific
domain, dataset, research question, and methodologically appropriate tests.
The proposal also calls for validating data quality and licensing, assessing
competitor coverage, and defining team ownership and evaluation criteria.

## Contributing

This repository is at the proposal stage. Contributions that help validate
the product scope, choose a suitable public dataset, review the research
methods, or refine the architecture are welcome. Please keep claims about
capabilities and differentiation evidence-based.
