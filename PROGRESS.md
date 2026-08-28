# Progress

## State

The Norway repository scaffold exists. The wealth-tax source intake is committed
in `axiom-corpus` at `65abb900660864d3b217b612369076ee05e9aba7`; CI and the
signed corpus binding still need to be finalized.

## Done

- Created the jurisdiction-scoped repository layout and empty validation ratchets.
- Identified the immutable upstream source-intake commit.

## Next

- Pin CI dependency checkouts to immutable commits.
- Ingest the Norway manifests, cut and sign the first `no` corpus release, and
  replace the non-validating toolchain state with its three-key binding.
- Encode and validate the first modules through `axiom-encode`.
