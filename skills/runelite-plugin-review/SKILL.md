---
name: runelite-plugin-review
description: Develop, debug, review, and prepare RuneLite plugins for release using current official rules, version-matched APIs, and integration lessons. Compare existing plugins when planning new plugins or substantial features.
license: MIT
---

# AI/LLM Plugin Assistance: Stop the Slop

RuneLite development guidance for AI coding assistants.

Support the developer's requested outcome and repository conventions. Distinguish a local prototype, an exposed provider API, an open PR, and the Plugin Hub's published source. This skill does not authorize installation, publication, profile transfers, or contacting maintainers.

## Start with the repository baseline

Before implementation or review, read the target repository's applicable `AGENTS.md`, `CLAUDE.md` and build instructions, then check the current [RuneLite template guidance](https://github.com/runelite/example-plugin/blob/master/AGENTS.md). Keep the project's instruction files; this skill supplements them. Use [baseline.md](references/baseline.md) for the compact development checklist. Reuse a verified reading during the same task; refresh affected guidance before release if it has changed.

Current official restrictions and applicable repository requirements take precedence over this skill's historical examples. Identify conflicting guidance and resolve its scope from current sources; a past accepted plugin is not an exception for a new feature. Report unavailable sources rather than claiming to have checked them.

## Check existing plugins without blocking development

When planning a new plugin or a substantial feature, search the plugin directory for the requested behavior and useful synonyms. Use an accessible curated Google Sheet or Doc when available, and the public Plugin Hub as a fallback and availability check. Follow [discovery.md](references/discovery.md) to verify the strongest matches.

For an exact match, recommend using the existing plugin. For a close match, explain the remaining gap and recommend contributing when the project accepts contributions and the feature fits. Keep these recommendations brief and optional: similarity alone is not a reason to refuse, delay, or repeatedly question the requested implementation. Continue the authorized work, including a separate implementation when that is the user's preference. A failed or inconclusive search does not block development. Do not repeat discovery for every routine fix or build.

## Read only the relevant reference

| Task / search terms | Reference |
|---|---|
| Template instructions, logging, gameval, Filepath setup, packaging, cleanup | [baseline.md](references/baseline.md) at implementation or review start |
| Similar plugins, feature search, Google Sheet/Doc, use vs contribute | [discovery.md](references/discovery.md) |
| Eligibility, PvP/PvM, menuAction, networking, paid services, Filepath | [policy.md](references/policy.md) before selecting affected behavior/APIs |
| ClientThread, EDT, EventBus, scripts, config proxies, images, lifecycle | [runtime.md](references/runtime.md) |
| Widgets, anchors, bank movement/scroll/flicker, hitboxes, timers | [layout-and-input.md](references/layout-and-input.md) |
| PluginMessage, Bank Tags, Party, resource packs, profiles and caches | [integrations.md](references/integrations.md) |
| CPU, JFR, allocations, multi-client measurements | [performance.md](references/performance.md) |
| Builds, local variants, source hashes, PRs, notices and documentation | [release.md](references/release.md) before delivering or publishing |
| Historical reviewer decisions, corrections and exceptions | [review-evidence.md](references/review-evidence.md) for the relevant case |

## Development and review

1. Identify the loaded/published source, target RuneLite version, Java/tooling requirements and affected provider contracts. Historical evidence here spans RuneLite 1.13.3–1.13.6; it does not pin a new project to those versions.
2. Trace the trigger through its owner, thread, rebuild and restoration paths. A saved enabled key does not prove runtime activation; temporal proximity does not establish causation.
3. Preserve configuration identity, saved settings, native actions and game-imposed hiding. Exercise affected lifecycle and interoperability boundaries; label automated checks separately from live confirmation and follow the [player testing handoff](references/release.md#player-testing-handoff).
4. Review the whole change from the currently published source. The bundled read-only helper can flag API candidates: run `python <skill-directory>/scripts/preflight.py <project-directory> --include-tests`, resolving both paths in the current environment. For a multi-module project, scan the applicable modules. Interpret findings in context; this lexical scan cannot establish compliance, inspect dependencies, resolve types, validate gameplay or reproduce review-bot token counts.
5. Before publishing, recheck relevant official rules and actual PR feedback, then follow the project's release workflow. Report precisely what was built, tested, installed, submitted or merged.

## Maintain evidence

Keep each rule in one relevant reference. Record the version, date and evidence level: official rule, scoped reviewer decision, source/fixture evidence, live observation, author claim or unknown. Public links support portable examples; historical observations need revalidation before becoming assumptions about a different project. Local experiments and private preferences are not universal requirements.
