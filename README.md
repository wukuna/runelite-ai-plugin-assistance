# AI/LLM Plugin Assistance: Stop the Slop

**RuneLite development guidance for AI coding assistants.**

An assistant skill and reference library for developers using AI to build, debug, review, and release RuneLite plugins. It helps assistants check real APIs, preserve settings and native behavior, handle plugin interactions, and distinguish tested results from assumptions.

The aim is useful, maintainable work: understand the problem, make the smallest suitable change, and verify the behavior before claiming it works.

This is an independent community resource, not an official RuneLite or Jagex project. Current official rules and repository requirements take precedence over historical examples.

## Use alongside RuneLite's template

Keep your project's `AGENTS.md` and `CLAUDE.md`. The skill supplements them and checks the current [RuneLite template guidance](https://github.com/runelite/example-plugin/blob/master/AGENTS.md) before implementation or review. Current official restrictions and repository requirements take precedence over historical examples.

- A [compact baseline checklist](skills/runelite-plugin-review/references/baseline.md) covers logging, API identifiers, Filepath setup, lifecycle cleanup, packaging and image sizes.
- A [player testing handoff](skills/runelite-plugin-review/references/release.md#player-testing-handoff) separates automated checks from player-confirmed behavior. The assistant does not drive RuneScape input to test a plugin.
- [AI attribution](skills/runelite-plugin-review/references/release.md#ai-attribution) names the assistant that actually contributed when following Plugin Hub submission requirements.

A case-specific TFA merge does not remove the broader restriction on new high-end PvM boss plugins. [Policy guidance](skills/runelite-plugin-review/references/policy.md#gameplay-and-ui) keeps those scopes separate.

## Start here

Use the [installable skill](skills/runelite-plugin-review/SKILL.md) for the working instructions. The [Google Doc companion](https://docs.google.com/document/d/1BoORYQXSyqYnQInRbOBOFJfqXPgt-5dRx1wE5rYsvFc) provides a readable introduction and links back to the maintained references.

## Install and use

This is a skill for your AI assistant, not a RuneLite client plugin. Open your plugin's source project when asking the assistant to change code. The skill name is `runelite-plugin-review`.

### Codex

Paste this into Codex:

```text
Use $skill-installer to install
https://github.com/wukuna/runelite-ai-plugin-assistance/tree/main/skills/runelite-plugin-review
```

After installation, send your task in a new message, for example:

```text
Use $runelite-plugin-review to review this plugin and suggest fixes.
```

Codex normally detects the skill automatically. If it does not appear, restart Codex. See the [official Codex skill instructions](https://developers.openai.com/codex/skills/).

### Claude Code

1. On the [GitHub repository](https://github.com/wukuna/runelite-ai-plugin-assistance), choose **Code → Download ZIP** and extract it.

2. Copy the complete `skills/runelite-plugin-review` folder into your plugin project's `.claude/skills/` folder. The entrypoint should be `.claude/skills/runelite-plugin-review/SKILL.md`.

3. Open that project in Claude Code and enter:

```text
/runelite-plugin-review Review this plugin and suggest fixes.
```

To use it across projects on this computer, put the folder in `~/.claude/skills/` instead; `~` means your home folder. See the [official Claude Code skill instructions](https://code.claude.com/docs/en/skills).

### Claude web or desktop

1. Download and extract the repository as above, then ZIP just the `runelite-plugin-review` folder inside `skills`. Keep `SKILL.md`, `references`, `scripts`, and `agents` together inside that folder.

2. Enable code execution in **Settings → Capabilities**. Under **Customize → Skills**, choose **+ → Create skill → Upload a skill**, upload your ZIP, and enable it.

3. Ask Claude: “Use runelite-plugin-review to help with this RuneLite plugin,” and provide your code or repository access.

If skill uploads are unavailable in your account, use the manual method below. See the [official Claude skill instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Other AI assistants, or manual use

If your assistant supports Agent Skills, import the complete `runelite-plugin-review` folder using its documented method. Otherwise:

1. Attach `SKILL.md` and the relevant files from `references`, or provide their links if the assistant can open them.

2. Ask: “Read these skill instructions and references, then use them for this task: [describe your change].”

3. Provide the plugin source and ask the assistant to identify anything it cannot access or test. Supply the files again in new chats unless your app saves them as project knowledge.

### Check that it is working

Ask: “Which skill did you load, and which reference files apply to this task?” The answer should identify `runelite-plugin-review` and the relevant references. The Google Doc is a companion; it does not replace those files.

To update, download or reinstall the latest complete skill folder, preserving any changes you made to your copy.

### Example task

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
| Repository baseline | [Template guidance and practical development checks](skills/runelite-plugin-review/references/baseline.md) |
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
