# Traceability Model

RTS-Design-Research requires this chain for every substantive claim:

external reference query (`reference_queries`)
-> retrieved provenance source (`research.sources`)
-> observed pattern
-> interpretation
-> UI requirement
-> implementation instruction
-> RTS design decision block
-> RTS/core or downstream repo commit

## Rule
Design findings must not appear as unsupported assertions. Each finding should cite a `source_id` from provenance sources and flow through spec, brief, and decision artifacts.
