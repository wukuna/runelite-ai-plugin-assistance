# Repository and template baseline

Use the target project's instructions alongside the current [RuneLite example-plugin AGENTS.md](https://github.com/runelite/example-plugin/blob/master/AGENTS.md). The template's [CLAUDE.md](https://github.com/runelite/example-plugin/blob/master/CLAUDE.md) currently imports that guide. Keep these project files when installing the skill. Check the current upstream version instead of treating a copied template as permanently current.

Apply the checks relevant to the change. Do not rename established configuration or reformat unrelated code merely to resemble a fresh template. [Policy](policy.md) covers eligibility; [release](release.md) covers player testing and publication.

## Compact development checklist

- **Logging and frame cost:** use debug-level diagnostics for frequent events; reserve info-level messages for infrequent lifecycle or useful user-facing events. Track relevant entities through events instead of scanning the whole scene each tick. Keep per-frame overlay work small; measure before introducing caches.
- **API conventions:** prefer the target version's `net.runelite.api.gameval` identifiers, including full widget component IDs, over literal IDs or manually packed widget IDs. Use injected Gson and OkHttp; derive Gson customizations from the injected instance. Open browser URLs with `LinkBrowser.browse`. Avoid redeclaring dependencies already provided transitively by RuneLite. See [policy](policy.md#api-triage) for restrictions.
- **Filepath setup:** use `Filepath` for plugin file access and `Filepath.Chooser` for file selection. Set the plugin descriptor's `internalName` as required for rooted storage. When migrating a legacy plugin-owned data directory, use the supported `legacyDataDirectory` descriptor field and preserve existing data; do not use migration as access to another plugin's files.
- **Lifecycle cleanup:** keep startup/shutdown nonblocking. Cancel plugin-owned scheduled tasks, remove owned listeners/subscriptions/overlays, and shut down only executors created and owned by the plugin. Avoid blocking latches or waits on client/EDT; compose asynchronous batches with `CompletableFuture.allOf` and marshal completion back to its owning thread. See [runtime](runtime.md#thread-ownership-and-script-reentrancy).
- **Scaffolding and packaging:** for a new plugin, replace template package/class names, config group, Gradle group/project name and plugin properties consistently. For an existing plugin, migrate saved keys/groups rather than resetting users. Match the current template's Java/build requirements, retain a distributable license, and exclude compiled output, temporary files and `META-INF/services/net.runelite.client.plugins.Plugin` from the source submission.
- **Assets and cleanup:** verify image formats and appropriate pixel dimensions; compressed PNG size does not describe decoded memory use. Preserve required attribution. Remove unused code/configuration and keep unrelated reformatting out of feature diffs.

This checklist is a summary of the linked baseline, not a complete policy list. Recheck current sources when APIs, tooling or reviewer guidance change.
