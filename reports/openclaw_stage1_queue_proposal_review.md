# OpenClaw Stage 1 Queue-Only Proposal Review

Date: 2026-05-12
Prepared by: Codex

## Decision

Accepted with edits.

OpenClaw complied with the queue-only boundary: no source collection, no profile generation, and no recovery details were included. Codex converted the proposal into a local proposed queue file for owner review.

## Adjustments Applied

- Did not preserve the stray `json` marker from OpenClaw's text output.
- Did not write any `incoming/`, `reviewed/`, or `final/` data.
- Preserved ASUS RT-AX86U, NETGEAR R7000, and Xiaomi AX3600 as proposed candidates.
- Replaced the ambiguous `TP-Link Archer AX3000` marketing-style label with `TP-Link Archer AX55` as an exact-model placeholder for owner review.
- Owner accepted `TP-Link Archer AX55` as the exact TP-Link first-batch candidate.

## TP-Link AX Planning Note

Owner provided TP-Link FAQ 1482: `https://www.tp-link.com/us/support/faq/1482/`.

Codex reviewed the page as a planning signal only. The page is useful because it explicitly discusses TP-Link Archer AX series recovery at the official support level and includes macOS network setup context. It should not be treated as model-specific `Archer AX55` profile evidence by itself because the page speaks at the Archer AX series level rather than proving AX55 hardware-version-specific behavior.

For real collection, OpenClaw should verify whether the FAQ applies to `Archer AX55` by checking model-specific official download/support pages and any hardware-version-specific notes before creating an incoming profile.

## Proposed Queue File

- `data/stage1_candidate_queue.proposed.jsonl`

This file is not an incoming profile and does not contain recovery methods, IP addresses, firmware filenames, TFTP direction, evidence snippets, or confidence assignments.

## Owner Decision Needed

The TP-Link candidate is confirmed as `TP-Link Archer AX55` for queue planning.

## Next Step

Run local validation, then ask the owner to approve or revise the proposed first batch before any real collection starts.
