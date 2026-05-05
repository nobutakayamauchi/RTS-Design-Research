# Contract: RTS Design Decision Block

## Purpose
Encode UI design decisions into RTS-compatible reconstructable records.

## Required structure
- `id`
- `type`
- `project`
- `screen`
- `created_at`
- `context`
- `research`
- `findings`
- `decision`
- `constraints`
- `assumptions`
- `action`
- `outcome`

## Reconstructability alignment
The block must preserve:
- Context
- Decision
- Constraints
- Assumptions
- Action
- Outcome

## Validation rules
- `id` is stable and unique.
- `created_at` uses ISO-8601.
- `research` and `findings` reference evidence.
- `outcome` can be updated as real results arrive.
