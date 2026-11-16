# Builds, testing and publication

Use the project's actual checkout, build instructions, release target and current user authorization. A local build, source push, Hub submission, merge and installed update are separate outcomes.

## Source and build identity

- Record the current Hub manifest's full source SHA, any open PR head, and the candidate being tested. A repository's default branch is not necessarily its published revision. If the previous PR merged, create a new submission for later changes.
- Reuse a suitable checkout. With downloaded snapshots, compare raw and LF-normalized Git blob hashes before declaring changes; mixed line endings can otherwise create a false whole-repository diff. Preserve untouched bytes.
- Read the project's wrapper/build files and the Hub's current `runelite.version`, [workflow](https://github.com/runelite/plugin-hub/blob/master/.github/workflows/build.yml) and [submission instructions](https://github.com/runelite/plugin-hub/blob/master/README.md). Historical checks here used Java 11 and RuneLite 1.13.6; verify the requirements for the current task. Offline `latest.release` resolution does not prove current compatibility.
- Run relevant regression checks and the appropriate full suite after behavioral changes. Text-only release edits normally need targeted checks. Archive earlier test reports if a targeted run replaces them. Record failures/skips and unresolved live checks accurately.
- Inspect jar descriptors, configuration identity, class version, dependencies, bundled resources and attribution. Check the entire public delta for test-only code and excluded experiments. Keep diagnostic executables and audit artifacts outside production packages.

## Player testing handoff

For live tests, follow the [template's testing instructions](https://github.com/runelite/example-plugin/blob/master/AGENTS.md#testing): do not use computer-use tools or scripts to drive RuneScape input. The player performs in-game actions. Builds, fixtures, screenshots and a clean JVM startup do not establish that a feature works in-game.

After a behavioral change, report automated results and give the player a short test list with the setup, action and expected result for each changed behavior, plus relevant lifecycle/compatibility cases. Offer the project's development-client launch command when useful and not already running; the template uses `./gradlew run`. Link the official [Jagex account development-client instructions](https://github.com/runelite/runelite/wiki/Using-Jagex-Accounts) when needed. Do not request account credentials or perform login for the player.

Keep live validation pending until the player confirms it, and record which build and cases were checked. Report completed code/build work separately from outstanding gameplay checks. Documentation-only changes do not require a game session. An explicit request to publish an untested build does not make its in-game behavior verified.

## Local test variants and saved settings

Use the project's existing local testing arrangement rather than imposing particular profile names or install paths. If a separate sideload identity is used, preserve its descriptor/configName and intentional feature groups while retaining normal public names/defaults in the release artifact. Verify the loaded identity separately from the filename.

For an authorized installation, back up the exact target jar, verify source and destination hashes, and replace the shared copy safely. If a client holds it open, prepare the update first and request normal shutdown; do not force-close it or modify settings to get around a lock. Verify settings preservation when promised. See [shared state](integrations.md#shared-state-across-profiles-and-clients) for profile/cloud transfers.

Respect the project's explicit local-only boundary for code, config, resources and dependencies. A locally paired provider/consumer integration is not automatically part of the public release.

## Source and Plugin Hub publication

1. Recheck relevant [policy](policy.md), actual review feedback and the deployed packager. A successful build is not a compliance certificate.
2. Publish the exact tested public source. Use an appropriate branch and expected-SHA checks where available; preserve newer remote work. Verify resulting blobs/tree against the candidate.
3. Update the fork's `plugins/<slug>` manifest to the repository and full tested commit. Use the existing open Hub PR for corrections; otherwise branch from current upstream. A source PR alone does not submit a Hub update.
4. Verify the manifest diff, source hash, upstream PR, description and checks. Use an available authorized browser fallback if a connector cannot complete the publication; a compare page is not a submitted PR.
5. Report the actual state. PR builds are not distribution, and a manifest marked unavailable may prevent delivery even after merge.

Use `build=standard` when it covers the plugin's needs. Recheck packager constraints for custom builds, dependencies, jar size and icons. Include a valid distributable license and required asset attribution; source licensing does not license unrelated artwork or sounds. Do not delete useful tests, minify code or move executable logic into data to evade review limits.

## AI attribution

Check the current template and target repository's submission requirements. The [template's submission section](https://github.com/runelite/example-plugin/blob/master/AGENTS.md#submitting) calls for a `Generated-by` footer on Plugin Hub PR descriptions. Name the assistant that actually contributed: for example, `Generated-by: Codex` for Codex or `Generated-by: Claude Code` for Claude Code. If multiple assistants contributed, identify them accurately. Do not copy a tool name mechanically from the template or infer authorship from the presence of `CLAUDE.md` or `AGENTS.md`. This belongs in the PR description, not an invented source-code attribution comment.

## Descriptions and release notices

Follow the repository template and maintainer conventions. Lead PRs with the user-visible problem and resulting behavior, then relevant implementation/validation details. Keep source hashes and manifest values synchronized. Write README/guide content for players; distinguish experimental demonstrations from released functionality.

If the plugin already uses in-game update notices, keep them concise, bundled locally and once per intended profile/release. Cancel stale callbacks after shutdown/profile changes. Keep an unmerged release's notice ID stable while editing it; use a separate local-test ID so testing does not consume the public notice. Do not add a new notification system merely because the skill mentions one.
