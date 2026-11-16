# AI/LLM Plugin Assistance: Stop the Slop

**RuneLite development guidance for AI coding assistants.**

An assistant skill and reference library for developers using AI to build, debug, review, and release RuneLite plugins. It helps assistants check real APIs, preserve settings and native behavior, handle plugin interactions, and distinguish tested results from assumptions.

The aim is useful, maintainable work: understand the problem, make the smallest suitable change, and verify the behavior before claiming it works.

This is an independent community resource, not an official RuneLite or Jagex project. Current official rules and repository requirements take precedence over historical examples.

## Start here

Use the [installable skill](skills/runelite-plugin-review/SKILL.md) for the working instructions. The [Google Doc companion](https://docs.google.com/document/d/1BoORYQXSyqYnQInRbOBOFJfqXPgt-5dRx1wE5rYsvFc) provides a readable introduction and links back to the maintained references.

For an assistant that supports `SKILL.md` skills, install or copy the complete `skills/runelite-plugin-review` folder using its supported workflow. Keep the `references`, `scripts`, and `agents` folders alongside `SKILL.md`. If your assistant does not load skills, give it the entrypoint and the relevant linked reference files; the Google Doc alone is not the complete skill.

The machine-readable skill name remains `runelite-plugin-review`.

Example request:

```text
Use runelite-plugin-review to implement this RuneLite feature.
Check relevant existing plugins, explain useful overlaps briefly,
then continue with the implementation I requested.
Preserve saved settings and native actions. Verify the affected
lifecycle and compatibility paths, and separate automated results
from anything that still needs an in-game test.
```

## What it covers

| Topic | Guidance |
|---|---|
| Existing alternatives | [Search directories, verify matches, and recommend use or contribution](skills/runelite-plugin-review/references/discovery.md) |
| Policy | [Current official restrictions and scoped reviewer evidence](skills/runelite-plugin-review/references/policy.md) |
| Runtime | [Client thread, Swing, events, scripts, images, and config proxies](skills/runelite-plugin-review/references/runtime.md) |
| Layout and input | [Widget geometry, anchors, banks, hitboxes, layering, and timers](skills/runelite-plugin-review/references/layout-and-input.md) |
| Integrations | [Provider contracts, shared state, resource packs, and profiles](skills/runelite-plugin-review/references/integrations.md) |
| Performance | [Measurements, allocations, and multi-client diagnosis](skills/runelite-plugin-review/references/performance.md) |
| Release | [Verified source, test variants, Plugin Hub submissions, and notices](skills/runelite-plugin-review/references/release.md) |
| Review history | [Public decisions with their scope and limitations](skills/runelite-plugin-review/references/review-evidence.md) |

## Existing plugins are useful options

Before a new plugin or substantial feature, the skill searches for the requested behavior. It recommends using an exact match, or contributing a focused change when a close match fits a receptive project.

Those recommendations do not veto development. If the user wants a separate implementation, the assistant continues within that scope. An inaccessible directory or inconclusive search also does not block progress.

Discovery can use the [shared plugin directory Doc](https://docs.google.com/document/d/1_D79a0F70xpC4xq84alpB3lkt8UVHrB5OcP4st4X7h8), an authorized Google Sheet directory, the [Plugin Hub](https://runelite.net/plugin-hub/), and built-in plugins. Listings are leads; important claims are checked against documentation or released source. Private accounts and sharing changes are not required.

## Advisory source scanner

The bundled Python helper is read-only and uses the standard library:

```text
python skills/runelite-plugin-review/scripts/preflight.py /path/to/plugin --include-tests
```

It flags candidate API usage and separates production from test findings. It does not resolve Java types, inspect dependencies, validate gameplay behavior, or certify Plugin Hub eligibility. Inspect each finding in context. Projects with multiple modules should scan the relevant modules individually.

## Contributing

Corrections and focused additions are welcome. Include the relevant public source, RuneLite version or commit, and whether the evidence is an official rule, reviewer decision, source/fixture observation, live result, or unverified report.

Keep guidance concise and put each rule in one appropriate reference. Preserve corrections to old decisions, avoid turning personal preferences into universal rules, and exclude private paths, credentials, player data, and unpublished project details. Update the skill and README together when behavior changes; keep the Google Doc companion aligned with the introduction and navigation.

## License

[MIT](LICENSE). Linked third-party material retains its own license and terms.
