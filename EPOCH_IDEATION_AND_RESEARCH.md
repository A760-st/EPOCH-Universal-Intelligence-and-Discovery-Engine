# EPOCH --- Product Ideation & Research

**Working product definition:** Evidence-grounded Discovery and
Experimentation Workspace\
**Prepared:** 10 November 2026\
**Purpose:** Axiom Review 1 preparation\
**Status:** Research-informed proposal; product assumptions require
validation

## 1. Executive recommendation

Do not position EPOCH as a "universal intelligence" or an autonomous
scientist. Those claims are too broad to validate and overlap with
active AI-for-science systems.

Position EPOCH as an **auditable computational research workspace** that
helps a researcher take a bounded question and dataset through a
traceable cycle:

**Explore evidence → formulate competing hypotheses → challenge
assumptions → run reproducible computational tests → compare results →
revise conclusions.**

The human researcher remains responsible for the research question,
interpretation, and final judgment. EPOCH assists and records the
process; it does not certify truth or scientific novelty.

## 2. Problem definition

### 2.1 Problem statement

A computational investigation can involve literature review, dataset
inspection, hypothesis formulation, statistical or machine-learning
experiments, interpretation, and documentation. These activities are
often performed in separate tools and documents. As a result, it can be
difficult to preserve a clear link between: - the original research
question; - the data and literature used; - each hypothesis and its
assumptions; - the analysis or experiment used to test it; - the code,
parameters, and data version; - the observed result and its limitations;
and - the reason a conclusion was retained, revised, or rejected.

AI tools can accelerate individual activities, but a generated
explanation is not itself evidence. A useful product opportunity is to
make the transitions between evidence, hypotheses, tests, and revisions
explicit and reviewable.

### 2.2 Intended users

-   Student and early-career researchers conducting computational
    projects.
-   Small interdisciplinary teams working with public or approved
    datasets.
-   Research supervisors or reviewers who need to inspect the basis of a
    result.

### 2.3 Why it matters

Research conclusions are stronger when other people can inspect the
data, assumptions, methods, and limitations. The 2026 EXHYTE review
finds that exploration and hypothesis generation are advancing, while
connecting generated ideas to executable tests and feeding results back
into subsequent reasoning remains a major workflow bottleneck \[R3\].

### 2.4 Initial scope

For the first MVP, choose: - one clearly defined research domain; - one
public, documented tabular dataset; - one investigation question; - two
or three competing hypotheses; - a small set of pre-approved statistical
or ML tests; and - one complete, reproducible investigation run.

The domain and dataset should be selected only after checking data
quality, licensing, documentation, and whether the question can be
answered with available variables.

### 2.5 Out of scope

-   A universal system for every scientific discipline.
-   Autonomous publication or claims of guaranteed discovery.
-   Guaranteeing that a hypothesis is novel or true.
-   Wet-lab or physical instrument execution.
-   Causal claims from observational correlation alone.
-   Unrestricted use of confidential, personal, or regulated research
    data.
-   Automatically transferring mechanisms between unrelated scientific
    domains.

## 3. Research landscape and existing alternatives

### 3.1 Google AI Co-Scientist

Google's 2026 Nature paper describes Co-Scientist as a Gemini-based
multi-agent system that generates, critiques, debates, and refines
research hypotheses. It uses literature grounding, specialized agents,
and iterative evaluation \[R1\]. Google DeepMind's description outlines
generation, reflection, ranking, and refinement roles \[R2\].

**What this means for EPOCH:** Multi-agent hypothesis generation,
simulated debate, literature grounding, and ranking are not unique
differentiators. EPOCH must not claim otherwise.

### 3.2 Google Labs science experiments

Google Labs presents separate science experiments for Literature
Insights, Hypothesis Generation, and Computational Discovery. Their
described capabilities include literature search and extraction,
multi-agent generation of research directions, and generation/scoring of
code variations against user-defined metrics \[R4\]. Google's
intended-use policy explicitly describes these as assistance whose
outputs require active review and validation, not automation of the
entire research process \[R5\].

**Implication:** A dashboard that merely calls an LLM, summarizes
papers, or generates hypotheses would be weak. EPOCH needs a coherent,
inspectable workflow and a clearly bounded user problem.

### 3.3 Empirical Research Assistance (ERA)

Google Research describes ERA as a tool for scientific coding and
iterative computational experiments, and reports its role in the
Computational Discovery prototype \[R6\].

**Implication:** Code generation and computational optimization are also
active areas. EPOCH should focus on controlled execution,
reproducibility, transparent assumptions, evidence lineage, and feedback
from failed as well as successful tests.

### 3.4 EXHYTE review (2026)

The EXHYTE review organizes AI-assisted scientific discovery around
exploration, hypothesis generation, and testing. It reports progress in
retrieval, knowledge assembly, and idea generation, but identifies the
transition to executable tests and feedback into subsequent reasoning as
a central bottleneck \[R3\].

**Opportunity hypothesis:** EPOCH could make the evidence → hypothesis →
test → result → revision chain the central product object. This is a
reasoned product opportunity, not proof that no competitor provides
similar functionality.

## 4. Proposed product and differentiation

### 4.1 Product proposition

EPOCH is a workspace where a researcher can inspect how each candidate
explanation was derived, what it predicts, how it was challenged, which
test was run, and how the result changed the investigation.

### 4.2 Proposed differentiators to validate

1.  **Hypotheses as structured records:** claim, rationale, assumptions,
    predicted observations, supporting evidence, counter-evidence, and
    status.
2.  **Explicit falsification planning:** for each hypothesis, record
    what result would weaken or contradict it.
3.  **Reproducible test runs:** store dataset version, code/version,
    parameters, environment, metrics, and outputs.
4.  **Evidence lineage:** link every claim and conclusion to a source,
    data field, analysis, or user annotation.
5.  **Revision history:** preserve why a hypothesis was retained,
    revised, downgraded, or rejected after a test.
6.  **Human approval gates:** users approve a proposed test before
    execution and review the result before it changes a conclusion.

These are proposed product requirements. Competitor feature coverage
must be checked with hands-on trials and current documentation before
claiming a unique market gap.

## 5. Core user journey

1.  Create an investigation and state a research question.
2.  Upload or select an approved dataset and review its schema and
    quality.
3.  Explore distributions, missingness, relationships, and notable
    patterns.
4.  Draft two or more competing hypotheses.
5.  For each hypothesis, inspect assumptions, supporting evidence,
    counter-evidence, and falsifiable predictions.
6.  Select a test from an allow-listed catalogue.
7.  Review the proposed method and approve execution.
8.  Execute in an isolated, resource-limited environment.
9.  Inspect metrics, diagnostics, warnings, and limitations.
10. Update hypothesis status and write a conclusion with links to
    evidence.
11. Export a reproducible investigation report.

## 6. MVP definition

### Required for first demonstrator

-   User sign-in and project/investigation workspace.
-   CSV upload with schema and data-quality summary.
-   Basic exploratory data analysis.
-   Structured competing-hypothesis editor.
-   AI-assisted drafting and critique with citations/links where
    available.
-   A small allow-listed set of tests (for example, descriptive
    comparison, correlation, group comparison, and a simple baseline
    model---chosen to fit the selected dataset).
-   Human approval before execution.
-   Isolated execution and stored run metadata.
-   Result comparison and hypothesis status/revision history.
-   Exportable report.

### Defer

-   Multi-agent orchestration as a core requirement.
-   Large-scale literature ingestion.
-   Arbitrary code execution.
-   Automated causal discovery.
-   Cross-domain knowledge transfer.
-   Real-time collaboration and enterprise integrations.

## 7. Feasibility and proposed technical approach

A student team can build a constrained MVP using conventional web
technologies and a controlled analysis service. The difficult work is
not the dashboard; it is designing a safe, reproducible execution and
provenance model.

Suggested initial stack: - Frontend: React + TypeScript. - Backend/API:
Python + FastAPI. - Database: PostgreSQL. - File/object storage: local
development storage initially; S3-compatible object storage later. -
Analysis: pandas, NumPy, SciPy, scikit-learn, statsmodels as needed. -
Background jobs: Celery/RQ or a simple task queue for MVP. - Charts: a
React charting library. - AI integration: provider-agnostic adapter; use
an LLM for drafting and critique, never as the source of statistical
results. - Deployment: Docker-based services; managed hosting only after
security and cost review.

### Execution safety

Never execute arbitrary user- or LLM-generated code directly inside the
web server process. Use a separate worker/container with: - no default
network access; - CPU, memory, and time limits; - read-only input
data; - restricted output directory; - dependency allow-list; -
execution logs and run identifiers.

## 8. Data model --- core entities

-   User
-   Workspace
-   Investigation
-   Dataset and DatasetVersion
-   DataProfile
-   EvidenceItem
-   Hypothesis
-   HypothesisEvidenceLink
-   TestDefinition
-   ExperimentRun
-   RunArtifact
-   HypothesisRevision
-   Comment/Review
-   AuditEvent

Every ExperimentRun should retain the exact dataset version, test
definition/version, parameters, code or container version, start/end
status, metrics, warnings, and artifact references.

## 9. Risks and mitigations

  -----------------------------------------------------------------------
  Risk                    Why it matters          Mitigation
  ----------------------- ----------------------- -----------------------
  Hallucinated or         Misleads the researcher Source-linked claims;
  unsupported AI claims                           explicit uncertainty;
                                                  human review

  False discovery /       Spurious patterns may   Record number of tests;
  multiple testing        look meaningful         correction where
                                                  appropriate; holdout
                                                  validation

  Correlation treated as  Invalid conclusions     Display design
  causation                                       limitations; prohibit
                                                  causal language without
                                                  a suitable design

  Unsafe generated code   Data loss or system     Allow-listed tests and
                          compromise              isolated execution

  Poor or biased data     Results may not         Data-quality profile,
                          generalize              missingness and bias
                                                  notes

  Weak novelty claim      Overstates product      Position as workflow
                          differentiation         integration; validate
                                                  competitor coverage

  Scope expansion         MVP becomes             One domain, one
                          unfinishable            dataset, one end-to-end
                                                  workflow
  -----------------------------------------------------------------------

## 10. Evaluation plan

Evaluate the MVP on: - Completion rate of the end-to-end workflow. -
Percentage of claims linked to evidence. - Reproducibility of a repeated
run with the same inputs and environment. - Correct handling of missing
values and invalid inputs. - Whether users can identify assumptions and
counter-evidence. - Time taken to move from dataset to reviewed test
result. - Expert review of whether the workflow is understandable and
scientifically responsible.

Do not evaluate "scientific discovery" by counting AI-generated
hypotheses.

## 11. Review 1 presentation outline

1.  Problem and affected users.
2.  Current workflow fragmentation and evidence.
3.  Existing alternatives: Co-Scientist, Google Labs science
    experiments, ERA.
4.  What is already solved and what remains difficult.
5.  EPOCH's proposed workflow and bounded MVP.
6.  Website/system architecture.
7.  Feasibility, risks, evaluation.
8.  Team ownership and execution plan.
9.  References and limitations.

## 12. Open decisions before implementation

-   Which scientific domain and public dataset will anchor the MVP?
-   What precise research question can be investigated with that
    dataset?
-   Which three or four tests are methodologically appropriate?
-   Which LLM/API can the team afford and access?
-   Who owns data ingestion, hypothesis workflow, experiment execution,
    UI, and evaluation?
-   What will be demonstrated at Review 1 versus a later technical
    review?

## References

-   \[R1\] Gottweis, J. et al. (2026). "Accelerating scientific
    discovery with Co-Scientist." *Nature*.
    https://www.nature.com/articles/s41586-026-10644-y
-   \[R2\] Google DeepMind (19 May 2026). "Co-Scientist: A multi-agent
    AI partner to accelerate research."
    https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/
-   \[R3\] Hasib, M. M. et al. (9 October 2026). "Unifying AI-assisted
    scientific discovery around exploration, hypothesis generation, and
    testing." *Patterns*.
    https://www.sciencedirect.com/science/article/pii/S2666389926001698
-   \[R4\] Google Labs. "Experiments on the future of AI-driven
    science." https://labs.google/science/
-   \[R5\] Google. "Intended Use Policy for Science experiments by
    Google Labs."
    https://support.google.com/hypothesis-generation/answer/17106905
-   \[R6\] Google Research (19 May 2026; updated 3 November 2026).
    "Empirical Research Assistance (ERA): From Nature publication to
    catalyzing Computational Discovery."
    https://research.google/blog/empirical-research-assistance-era-from-nature-publication-to-catalyzing-computational-discovery/

------------------------------------------------------------------------

**Research caveat:** This is a focused initial landscape, not an
exhaustive systematic review. Competitor claims and the proposed
differentiation should be validated with product trials, current
documentation, and additional domain-specific literature before final
submission.
