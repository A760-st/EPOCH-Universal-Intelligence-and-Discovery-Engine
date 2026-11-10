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

The current architecture proposal describes a React and TypeScript web app,
a Python and FastAPI API, PostgreSQL for structured records, object storage
for datasets and artifacts, and a background worker for approved experiments.
An AI provider adapter is optional and should never be responsible for
statistical computation.

These are proposed choices, not implemented or finalized technologies. See
the [website and system architecture](./EPOCH_WEBSITE_ARCHITECTURE.md) for
the component design, data model, API outline, deployment topology, and open
decisions.

## Project documents

| Document | Description |
| --- | --- |
| [Product ideation and research](./EPOCH_IDEATION_AND_RESEARCH.md) | Problem framing, intended users, research landscape, proposed MVP, risks, and evaluation plan. |
| [Website and system architecture](./EPOCH_WEBSITE_ARCHITECTURE.md) | User journey, pages, components, data model, API outline, safeguards, and implementation phases. |

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
