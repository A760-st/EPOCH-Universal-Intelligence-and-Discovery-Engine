# EPOCH --- Website & System Architecture

**Product:** Evidence-grounded Discovery and Experimentation Workspace\
**Document type:** Proposed architecture baseline\
**Prepared:** 10 November 2026\
**Status:** Architecture proposal for review; revise after MVP domain
and dataset selection

## 1. Architecture goals

The website should make an investigation understandable from beginning
to end. The central object is an **Investigation**, containing datasets,
evidence, hypotheses, test plans, experiment runs, results, and
revisions.

Architecture priorities: 1. Traceability from conclusion to evidence and
run. 2. Reproducibility of computational tests. 3. Safe execution of
analysis workloads. 4. Human approval before tests run and conclusions
change. 5. A modular MVP that a student team can implement.

## 2. Product boundary

EPOCH is not a general-purpose autonomous scientist. The first release
supports a bounded computational investigation over approved tabular
data and a small catalogue of tests.

## 3. Main navigation / website information architecture

  -----------------------------------------------------------------------------------
  Area                    Route                               Purpose
  ----------------------- ----------------------------------- -----------------------
  Landing                 `/`                                 Product explanation,
                                                              demo, sign-in

  Authentication          `/login`, `/register`               User access

  Workspace list          `/workspaces`                       List user's workspaces

  Workspace overview      `/workspaces/:workspaceId`          Investigations and
                                                              recent activity

  Investigations          `/investigations/:id`               Investigation overview
                                                              and workflow

  Data                    `/investigations/:id/data`          Upload, versions,
                                                              schema, quality

  Explore                 `/investigations/:id/explore`       EDA, charts,
                                                              associations

  Hypotheses              `/investigations/:id/hypotheses`    Competing hypotheses
                                                              and evidence

  Test planning           `/investigations/:id/tests`         Select and review test
                                                              plans

  Runs                    `/investigations/:id/runs`          Run history and
                                                              execution status

  Run detail              `/investigations/:id/runs/:runId`   Metrics, logs,
                                                              artifacts, diagnostics

  Evidence                `/investigations/:id/evidence`      Sources, dataset
                                                              fields, annotations

  History                 `/investigations/:id/history`       Revision and audit
                                                              timeline

  Report                  `/investigations/:id/report`        Exportable report

  Settings                `/settings`                         Profile, provider
                                                              configuration,
                                                              workspace settings
  -----------------------------------------------------------------------------------

## 4. Primary user journey

``` mermaid
flowchart TD
  A[Create investigation] --> B[Upload approved dataset]
  B --> C[Profile schema and data quality]
  C --> D[Explore data]
  D --> E[Draft competing hypotheses]
  E --> F[Attach supporting and opposing evidence]
  F --> G[Select allow-listed test]
  G --> H[Review method and assumptions]
  H --> I{Human approval}
  I -- Reject / edit --> G
  I -- Approve --> J[Queue isolated experiment]
  J --> K[Store run metadata and artifacts]
  K --> L[Review metrics and limitations]
  L --> M[Revise hypothesis status]
  M --> N[Export traceable report]
```

## 5. Page-level requirements

### 5.1 Investigation overview

Show question, domain, owner, status, selected dataset version, current
hypotheses, latest run, unresolved review items, and activity timeline.

### 5.2 Data page

-   CSV upload and file validation.
-   Dataset versioning; never silently overwrite a version used by a
    previous run.
-   Schema table: column name, inferred type, missing count, unique
    count, sample values.
-   Quality warnings: missingness, duplicate rows, constant columns,
    invalid values, possible identifiers.
-   User confirmation of target/outcome and sensitive columns.
-   Download or delete controls subject to permissions and retention
    policy.

### 5.3 Explore page

-   Summary statistics and distributions.
-   Missingness visualization.
-   Pairwise relationships and group comparisons.
-   Clear warning that exploratory patterns are not proof of causation.
-   Save a chart or observation as an EvidenceItem with dataset version
    and filters recorded.

### 5.4 Hypothesis explorer

Each hypothesis card/detail page contains: - Claim and rationale. -
Assumptions. - Predicted observations. - Supporting evidence. -
Counter-evidence. - Proposed falsification condition. -
Confidence/uncertainty explanation (not an unexplained score). - Status:
Draft, Needs review, Test planned, Supported by current evidence,
Weakened, Rejected, Inconclusive.

### 5.5 Test planning

-   Select only from an allow-listed test catalogue.
-   Show required variables, assumptions, null/alternative hypothesis
    where relevant, missing-data handling, and limitations.
-   Show planned metric and validation strategy.
-   Require user approval before queuing.

### 5.6 Run detail

Show queued/running/succeeded/failed/cancelled status, dataset version,
test definition version, parameters, software/container version,
timestamps, logs, metrics, diagnostics, and downloadable artifacts.

### 5.7 History and report

A chronological audit log records dataset additions, hypothesis edits,
approvals, test runs, result interpretation, and status changes. The
report should link conclusions to evidence and experiment runs.

## 6. System architecture

``` mermaid
flowchart TB
  U[Researcher / Reviewer] --> FE[React + TypeScript Web App]
  FE --> API[FastAPI Application]
  API --> AUTH[Authentication & RBAC]
  API --> PG[(PostgreSQL)]
  API --> OBJ[(Object Storage)]
  API --> Q[Background Job Queue]
  API --> AI[AI Orchestration Adapter]
  AI --> LLM[External LLM Provider]
  Q --> WORKER[Experiment Worker]
  WORKER --> SANDBOX[Isolated Execution Container]
  SANDBOX --> LIB[Allow-listed Analysis Libraries]
  WORKER --> PG
  WORKER --> OBJ
  API --> AUDIT[Audit Event Service]
  AUDIT --> PG
```

### Component responsibilities

-   **Web app:** navigation, forms, tables, charts, workflow state,
    report viewer.
-   **FastAPI:** authentication checks, validation, business rules,
    APIs, orchestration.
-   **PostgreSQL:** users, workspaces, investigations, metadata,
    hypotheses, evidence links, test definitions, runs, revisions, audit
    events.
-   **Object storage:** original dataset files, immutable dataset
    versions, run artifacts, generated reports.
-   **AI adapter:** prompt templates, provider abstraction, structured
    output validation, source/citation capture, token/cost logging.
-   **Job queue:** asynchronous execution and status transitions.
-   **Experiment worker:** validates a selected test definition and runs
    approved code in a sandbox.
-   **Audit service:** append-only event records for consequential
    user/system actions.

## 7. Suggested technology stack

  -----------------------------------------------------------------------
  Layer                   MVP choice              Notes
  ----------------------- ----------------------- -----------------------
  Frontend                React + TypeScript +    Component-based web UI
                          Vite                    

  UI styling              Tailwind CSS or CSS     Choose one; avoid
                          modules                 unnecessary UI
                                                  complexity

  API                     Python + FastAPI        Typed request/response
                                                  schemas

  Database                PostgreSQL              Relational integrity
                                                  and audit metadata

  ORM/migrations          SQLAlchemy + Alembic    Schema evolution

  Validation              Pydantic                API and AI
                                                  structured-output
                                                  validation

  Analysis                pandas, NumPy, SciPy,   Only libraries required
                          scikit-learn,           by chosen tests
                          statsmodels             

  Charts                  Recharts or Plotly      Pick one

  Queue                   RQ + Redis, or Celery + Select based on team
                          Redis                   familiarity

  Storage                 Local filesystem in     Keep storage interface
                          development;            abstract
                          S3-compatible in        
                          deployment              

  Packaging               Docker                  Separate API and worker
                                                  containers

  Testing                 pytest + frontend test  Unit, integration, and
                          framework               workflow tests
  -----------------------------------------------------------------------

## 8. Core database entities

``` text
User
- id, email, password_hash / identity_provider_id, created_at

Workspace
- id, name, owner_id, created_at

WorkspaceMember
- workspace_id, user_id, role

Investigation
- id, workspace_id, title, research_question, domain, status, created_by

Dataset
- id, investigation_id, name, source_description, license, created_by

DatasetVersion
- id, dataset_id, object_key, checksum, schema_json, profile_json, created_at

EvidenceItem
- id, investigation_id, evidence_type, title, content, source_uri, locator, created_by

Hypothesis
- id, investigation_id, title, claim, rationale, assumptions_json, predictions_json, status

HypothesisEvidenceLink
- hypothesis_id, evidence_item_id, relation_type [supports / contradicts / contextualizes]

TestDefinition
- id, name, version, description, input_schema, assumptions_json, implementation_key

ExperimentRun
- id, investigation_id, hypothesis_id, dataset_version_id, test_definition_id,
  parameters_json, status, code_version, environment_digest, started_at, ended_at

RunArtifact
- id, run_id, artifact_type, object_key, checksum, metadata_json

HypothesisRevision
- id, hypothesis_id, prior_state_json, new_state_json, reason, created_by, created_at

AuditEvent
- id, actor_id, investigation_id, event_type, entity_type, entity_id, payload_json, created_at
```

Use foreign keys and immutable references for dataset versions and
experiment runs. Avoid storing large files or raw result tables directly
in relational rows.

## 9. API design (initial)

  ------------------------------------------------------------------------------------------
  Method                  Endpoint                                   Purpose
  ----------------------- ------------------------------------------ -----------------------
  POST                    `/api/v1/investigations`                   Create investigation

  GET                     `/api/v1/investigations/:id`               Read overview

  POST                    `/api/v1/investigations/:id/datasets`      Upload dataset

  GET                     `/api/v1/datasets/:id/versions`            List dataset versions

  POST                    `/api/v1/datasets/:id/profile`             Start or retrieve
                                                                     profiling

  GET                     `/api/v1/investigations/:id/exploration`   Retrieve EDA results

  POST                    `/api/v1/investigations/:id/hypotheses`    Create hypothesis

  PATCH                   `/api/v1/hypotheses/:id`                   Edit hypothesis

  POST                    `/api/v1/hypotheses/:id/evidence-links`    Link evidence

  GET                     `/api/v1/test-definitions`                 List approved tests

  POST                    `/api/v1/hypotheses/:id/test-plans`        Create test plan

  POST                    `/api/v1/test-plans/:id/approve`           Human approval

  POST                    `/api/v1/test-plans/:id/runs`              Queue approved run

  GET                     `/api/v1/runs/:id`                         Run status/details

  GET                     `/api/v1/investigations/:id/history`       Audit timeline

  POST                    `/api/v1/investigations/:id/reports`       Generate report
  ------------------------------------------------------------------------------------------

All endpoints must enforce workspace membership and role permissions.
Use pagination, request IDs, structured errors, and idempotency for job
submission.

## 10. AI design and guardrails

AI may: - help rewrite a research question into a structured form; -
suggest candidate hypotheses based on supplied evidence; - identify
missing assumptions and counter-arguments; - draft a test plan from the
approved test catalogue; - summarize run results after receiving the
actual computed outputs.

AI must not: - invent statistical results; - claim a hypothesis is
proven; - silently select or execute arbitrary code; - change a
hypothesis status without user confirmation; - fabricate citations or
imply that a source supports a claim without a locator.

Validate AI output against schemas. Keep prompts, model/provider
identifiers, timestamps, and output hashes for auditability where
appropriate.

## 11. Security, privacy, and reliability

-   Passwords handled by a reputable identity provider or secure
    password hashing.
-   Role-based access control at workspace and investigation level.
-   TLS in deployment; secrets stored outside source control.
-   File type, size, and content validation.
-   Malware scanning if accepting untrusted files in a public
    deployment.
-   Isolated worker execution with no network by default and strict
    resource quotas.
-   Encryption at rest where supported by storage provider.
-   Explicit retention and deletion policy.
-   Avoid personal/sensitive data in the first MVP.
-   Audit events for upload, access-sensitive actions, approvals,
    execution, export, and deletion.
-   Backups and restore test before any real research use.

## 12. Deployment topology

### Local development

-   `frontend` container or Vite dev server.
-   `api` container.
-   `postgres` container.
-   `redis` container if queue selected.
-   `worker` container.
-   local object-storage adapter.

### Demonstration deployment

Use one frontend deployment, one API service, one worker service,
managed PostgreSQL, and object storage. Do not deploy arbitrary code
execution until sandbox isolation has been tested.

## 13. Implementation phases

1.  **Foundation:** auth, workspace, investigation, PostgreSQL schema.
2.  **Data:** upload, immutable versioning, schema/profile.
3.  **Explore:** EDA and saved observations.
4.  **Hypotheses:** structured hypothesis editor and evidence links.
5.  **Tests:** allow-listed test catalogue and approval workflow.
6.  **Execution:** isolated worker, run metadata, artifacts.
7.  **Revision/report:** hypothesis history and traceable export.
8.  **Hardening:** permissions, failure handling, tests, deployment.

## 14. Architecture decisions still open

-   Final domain, dataset, and investigation question.
-   Whether LLM features are essential for the first demo or can be
    mocked behind an adapter.
-   Exact statistical tests.
-   Queue choice and sandbox technology.
-   Hosting and API budget.
-   Team ownership and acceptable data policy.

## 15. Architecture acceptance criteria

The MVP architecture is acceptable when: - every run points to an
immutable dataset version; - no experiment can run without explicit
approval; - only allow-listed tests can execute; - runs preserve
parameters, environment version, logs, and artifacts; - hypotheses link
to supporting and contradicting evidence; - a conclusion can be traced
to its evidence and test results; - one complete investigation can be
exported and reproduced.

------------------------------------------------------------------------

This is a proposed architecture, not a claim that the system has been
implemented or security-certified.
