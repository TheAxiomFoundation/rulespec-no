# rulespec-no — agent notes

RuleSpec lane scaffold for Norway's 2022 and 2023 wealth-tax scope.

This scaffold emits scaffold-adapted layout tests; the lane grows into the full
migrated-lane suite as it fills in.

## Lane bring-up sequence

1. Publish the prepared axiom-corpus manifests listed in `data/coverage/tax-benefit-source-map.json`.
2. Ingest those sources through the corpus pipeline.
3. Cut and sign the first immutable `no` corpus release.
4. Land the dedicated gated `.axiom/toolchain.toml` PR with the real three-key binding.
5. Replace every workflow `<pin-me>` in the same dedicated post-release toolchain PR, using an encoder-supported workflow pin.
6. Encode the first module through the supervised runtime; do not hand-author RuleSpec.
7. Run `axiom-encode ci` locally with the explicit dependency checkouts and release public key.

## Listing gates

Keep `.axiom/registry.toml` experimental until the signed release binding, pinned CI,
first supervised encoding, and oracle validation or recorded disposition are complete.
