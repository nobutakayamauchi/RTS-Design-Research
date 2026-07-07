# RTS-Design-Research Next Actions

The next goal is an inventory pass, not UI implementation.

## Next Tasks

1. List existing design references, UI notes, screenshots, and layout explorations.
2. Identify which materials are ready, draft, stale, duplicate, risky, or misplaced.
3. Confirm provenance or source notes for design references and assets.
4. Separate facts, assumptions, unverified material, risks, and open questions.
5. Convert useful observations into implementation-neutral decision material.
6. Check local documentation links.
7. Decide which design materials should remain here and which belong in product or runtime repositories.

## Suggested Follow-up Files

```text
docs/inventory/design_inventory.md
docs/contracts/design_decision_material_contract.md
docs/relations/adjacent_repo_boundaries.md
```

## Inventory Categories

Use these labels during the next pass:

- READY: usable as design decision material
- DRAFT: useful but incomplete
- STALE: likely outdated or superseded
- DUPLICATE: overlaps another design note or reference
- RISKY: provenance, licensing, or product implication needs review
- MOVE: belongs in another repository
- ARCHIVE: preserve for history only

## Design Review Checklist

Each design item should explicitly describe:

- name
- path
- purpose
- source or provenance
- design observation
- assumption
- risk
- applicable product or workflow
- next smallest safe action

If a design item implies accepted product behavior, product UI implementation, or use of unclear assets, mark it as `RISKY` and do not expand it until reviewed.

## Do Not Do Yet

Do not:

- add runtime implementation code
- add product UI code by default
- add copyrighted or unclear assets
- import canonical RTS records
- import RTS-AGE implementation internals
- rewrite all design notes at once
- promote a design note to canonical product requirement without review

## Next Recommended Task

Create `docs/inventory/design_inventory.md`.

That file should list each known design reference or UI note with:

1. name
2. path
3. purpose
4. status label
5. source or provenance
6. applicable product or workflow
7. implementation-neutral observation
8. risk
9. next smallest safe action
