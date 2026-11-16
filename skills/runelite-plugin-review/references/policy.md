# Policy and eligibility

Maintained 2026-11-15. This is a decision index, not an exhaustive permission list. Current official restrictions outrank older accepted plugins, author claims and product preferences. Recheck the specific rule before designing behavior and publishing.

## Official sources

| Source | Use |
|---|---|
| [Example-plugin AGENTS.md](https://github.com/runelite/example-plugin/blob/master/AGENTS.md) | Current development/testing/submission baseline; read with the target repository's instructions |
| [Rejected or Rolled Back Features](https://github.com/runelite/runelite/wiki/Rejected-or-Rolled-Back-Features) | APIs/features; rechecked Nov 15, last edit Nov 11 |
| [Jagex guidelines](https://secure.runescape.com/m=news/third-party-client-guidelines?oldschool=1) | Combat, menus, interface/click-zone boundaries |
| [April 2024 amendments](https://secure.runescape.com/m=news/undead-pirates-tweaks-varlamore-cas--more?oldschool=1) | Later spellbook movement/hiding, construction and cape exceptions |
| [Hub README](https://github.com/runelite/plugin-hub/blob/master/README.md) | Packaging/submission; rechecked Nov 15 |
| [Hub review](https://github.com/runelite/runelite/wiki/Plugin-Hub-Review) / [external-server information](https://github.com/runelite/runelite/wiki/Information-about-the-Plugin-Hub) | Scope and warnings |
| [Workflow](https://github.com/runelite/plugin-hub/blob/master/.github/workflows/build.yml) / [API signatures](https://github.com/runelite/plugin-hub-tooling/blob/v5/package/src/main/resources/net/runelite/pluginhub/packager/disallowed-apis.txt) | Enforcement; Nov 15 workflow used tooling v5 / Java 11 |

## API triage

Use Java, injected Gson/OkHttp and rooted Filepath access. Check reflection/native/process/runtime APIs, sleep/interruption, focus/input simulation, external executable code, direct filesystem calls and browser-opening APIs against the official list. `LinkBrowser.browse` differs from forbidden `open`. Do not publish under `net.runelite` packages.

`Client.menuAction` has only the exact collection-log search exception on the official page; a user click does not permit other invocations. Network I/O and `runScript` are sensitive. `hopToWorld`, `Filepath.Unchecked` and `setCanSendPackets` require manual review. Trace indirect calls/dependencies too.

Scanner hits are candidates: an inner class named `Files`, resource stream, exception type or ordinary `getClass()` is not automatically prohibited filesystem/reflection use. Separate test-only findings. Never hide code or remove useful tests to silence a lexical scan.

New-plugin Filepath use was explicitly required in [GIM Utilities](https://github.com/runelite/plugin-hub/pull/20149#issuecomment-6806930483); the older session-tracker exception is case-specific. `Unchecked` does not cure ownership violations. Use bundled streams in jars, not resource URLs assumed to be disk paths. Use injected AudioPlayer for playback; metadata-only Java Sound calls were also flagged in an Improved Looting review. See [evidence](review-evidence.md#apis-and-packaging).

## Gameplay and UI

Evaluate the information/action supplied, not just whether it reads visible state or sends packets. Check boss prediction/prayer/standing assistance, opponent freeze timers, PvP targeting/scouting, conditional menus, game-hidden widgets and simulations. Self-resource timers do not establish permission for opponent/combat guidance.

Identify the exact interface before changing click areas. Bank slots differ from the inventory, combat, worn-equipment and spell/prayer interfaces named in Jagex rules. Later amendments modify older examples. Bank rearrangement does not permit changing equipped-item click zones. Retain native actions; do not automate withdrawals.

The official list also covers core RuneLite UI/anchors, other plugins' configs, desktop window manipulation, significant asset changes, HTTP player-data exposure and autotyping/outgoing chat rewriting. Plugin-owned controls/services are not blanket exemptions. Local-only client patches are separate deliverables, not automatically eligible Hub code. Compatibility tests establish engineering behavior, not policy approval for every adapter.

Do not generalize bounded accepted NPC equipment guards into unrestricted conditional-menu engines. Likewise, a later case-specific TFA merge does not establish general acceptance of TFA helpers or repeal the broader policy: the current official list still says new high-end PvM boss plugins are not being considered. The earlier temporary TFA review hold and the broader restriction are distinct. Recheck current policy and the exact reviewed feature. [Scoped examples](review-evidence.md#gameplay-and-ui).

## Networking, warnings and paid services

Record destinations, payloads, identifiers, consent, rate/size limits, caching and failures. Validate remote paths/redirects against intended origins and bound decoding. Source licenses do not automatically license sounds/artwork.

Warnings are **scope-dependent**. The [Nov 14 Loadout Studio correction](https://github.com/runelite/plugin-hub/pull/19421#issuecomment-6878205214) removed the warning for verified Wiki-only requests with an identifying user agent. Broader integrations still need applicable warnings. Explicit sign-in satisfied consent in one case; do not invent a universal checkbox requirement. Warnings cannot authorize prohibited data collection.

Do not assume outbound HTTPS escapes the HTTP/player-data rule, or infer that every outbound account integration is forbidden. Compare exact fields, direction, purpose, controls, reviewed revision and companion distribution. Seek a scoped interpretation for material ambiguity. Deleting setup instructions does not cure an external companion dependency.

The paid-service rule concerns significant functionality locked behind paid external services in new plugins from October 14, 2026, with discretionary common-service exceptions. It is not a ban on every link, donation or paid service. [Current wording](https://github.com/runelite/runelite/wiki/Rejected-or-Rolled-Back-Features#plugins-which-interface-with-paid-external-services).

## Review is not functional certification

Review the whole executed plugin and delta, dependencies and lifecycle, not only the newest commit. The approximately 200k production-Java-token ceiling differs from `size-xl` diff labels. Recorded bot notices exclude comments/resources/tests; local estimates are approximate. Splitting PRs or deleting tests does not solve whole-plugin size. Reduce scope/duplication; do not minify or move executable logic into data to evade review.

Hub review does not certify performance, functionality or interoperability. Merged examples may be grandfathered or have removed disputed features. Read final source/later replies; [review evidence](review-evidence.md) separates decisions and historical status.
