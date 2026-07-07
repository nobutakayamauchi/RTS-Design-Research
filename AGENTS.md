# AGENTS.md

## Scope

This file applies to the entire repository.

## Required reading

Before editing, read:

1. `README.md`
2. `docs/STATUS.md`
3. `docs/NEXT.md`

## Repository guardrails

- Keep this repository as the RTS design reference and UI decision material shelf.
- Do not add runtime implementation code by default.
- Do not add product UI code by default.
- Do not import RTS core canonical records.
- Do not import RTS-AGE implementation internals.
- Do not present speculative UI notes as accepted product requirements.
- Do not add copyrighted or unclear assets without provenance notes.
- Prefer implementation-neutral design observations over broad redesigns.

## Inventory pass boundary

- Treat the next pass as design inventory and provenance review, not UI implementation.
- Prefer adding or improving index, inventory, and boundary documentation before changing design materials.
- Do not promote a design note to canonical product requirement without a separate review decision.
- If a design item implies accepted product behavior, product UI implementation, or unclear asset use, mark it as `RISKY` in inventory documentation instead of expanding it immediately.
- If a design item belongs in another repository, mark it as `MOVE` instead of moving it immediately.

## Documentation rules

- Separate confirmed facts, assumptions, unverified material, risks, and open questions.
- Record source or provenance when referencing external design material.
- Keep design notes inspectable and attributable.
- Use minimal additive edits over broad refactors.

## Validation

- Check for broken local doc links when adding index or onboarding docs.
- For documentation-only changes, report changed files and confirm that no runtime, product UI, asset library, or canonical design system implementation was added.
