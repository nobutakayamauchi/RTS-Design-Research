# Reference Intelligence Layer

## Purpose

RTS-Design-Research should not ask an AI to invent taste from a blank prompt. When ChatGPT, Codex, or another design-capable agent is uncertain about visual direction, it should retrieve proven references first, extract reusable principles, and only then generate or revise a design.

The goal is not imitation. The goal is evidence-backed taste calibration.

## Core idea

A reference becomes useful only when the system can answer four questions:

1. What is the source?
2. Why is it considered strong or relevant?
3. Which visual principles are reusable?
4. Which parts must not be copied?

## Canonical flow

`DESIGN_NEED -> SEMANTIC_DECOMPOSITION -> REFERENCE_RETRIEVAL -> PREFERENCE_EVIDENCE -> PRINCIPLE_EXTRACTION -> DESIGN.md -> GENERATION -> REFERENCE_AUDIT -> HUMAN_GATE`

### 1. DESIGN_NEED
Capture the actual design problem, not only the requested artifact.

Examples:
- inheritance consultation logo
- recruiting landing page
- B2B dashboard

### 2. SEMANTIC_DECOMPOSITION
Decompose the problem into traits that can retrieve references across industries.

Example:
`inheritance consultation -> trust + calm + professional expertise + mature audience + reduced anxiety + high-stakes decision`

The system SHOULD search by these traits as well as by industry. It MUST NOT assume that the best reference comes from the same industry.

### 3. REFERENCE_RETRIEVAL
Retrieve a small set of references from sources with provenance. Candidate reference classes include:

- award-recognized design
- widely adopted long-lived brand systems
- products repeatedly cited as design references
- designs with observable user preference signals
- strong examples from adjacent industries that express the required trait

Reference popularity alone is not sufficient evidence of quality.

### 4. PREFERENCE_EVIDENCE
For every selected reference, record why it deserves weight.

Evidence can include:
- recognized design award or curated publication
- explicit expert critique or design-system documentation
- durable repeated use by a successful product or organization
- substantial save/share/like preference signals when context is known
- direct user preference tests
- project-specific human approval

Evidence strength MUST be recorded separately from the visual observation itself.

### 5. PRINCIPLE_EXTRACTION
Extract reusable visual principles instead of copying surface appearance.

Examples:
- one dominant focal point
- restrained color count
- generous negative space
- strong typographic hierarchy
- low decorative noise
- geometric consistency
- predictable alignment rhythm

Also record `do_not_copy` items such as logos, proprietary icons, illustrations, exact layouts, distinctive trade dress, or copyrighted assets.

### 6. DESIGN.md GENERATION
Generate a project-local `DESIGN.md` from the selected principles. `DESIGN.md` is an execution constraint for the agent, not a source-of-truth artifact.

It SHOULD define:
- design intent
- audience
- visual traits
- composition
- spacing
- typography
- color behavior
- shape/icon rules
- accessibility constraints
- anti-patterns
- reference IDs and provenance pointers

### 7. GENERATION
The design agent creates or revises the artifact under the `DESIGN.md` constraints.

### 8. REFERENCE_AUDIT
Before approval, compare the result against the extracted principles, not against pixel similarity.

Audit questions:
- Does the result express the intended traits?
- Did generic AI visual clichés appear?
- Did the agent copy a reference too literally?
- Is hierarchy clear?
- Is visual noise controlled?
- Does the result work for the actual audience and medium?

### 9. HUMAN_GATE
A human makes the final aesthetic and contextual decision.

## Retrieval behavior for ChatGPT / Codex

When a design task is underspecified, visually weak, or explicitly described as "dull", "generic", or "ugly", agents SHOULD:

1. search this repository for matching `traits`, `audience`, `artifact_type`, and `sector`;
2. select 3-5 high-confidence references;
3. explain the transferable principles;
4. generate a project `DESIGN.md`;
5. use that file during generation or redesign;
6. run the reference audit before presenting the result.

If no credible reference exists, the agent MUST report a `REFERENCE_GAP` rather than fabricate design authority.

## Cross-industry retrieval

Same-industry references are optional. Trait similarity is often more useful.

Example:

`funeral / inheritance`
may retrieve from
`premium hospitality + healthcare + financial services + editorial minimalism`

when those references better express calm, trust, dignity, and legibility.

## Non-goals

This layer is not:
- a screenshot dumping ground
- a cloning system
- an automated claim that popularity equals beauty
- a replacement for human taste
- a license to reuse protected assets

## Principle

**Do not ask the model to invent taste when taste can be grounded in evidence.**
