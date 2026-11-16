# Layout, anchors, bank and input

Historical engineering evidence: RuneLite 1.13.6 fixtures and live reports through 2026-11-14. These are failure mechanisms to test in the target project, not guarantees for every implementation. Policy eligibility is separate: [policy.md](policy.md#gameplay-and-ui).

## Native geometry and input

`Widget.getBounds()` can describe the last drawn frame while relative/forced positions and parent geometry already changed. Mixing those time bases caused bank movement to drift, resize handles to miss, and anchor measurements to be wrong. For layout mutations, compute current absolute geometry from current relative coordinates and ancestor scroll offsets. Preserve cycle safety. Use drawn bounds when the intended contract really is the displayed frame; do not globally replace all widget bounds calls without tracing their purpose.

A stale-bounds fixture reproduced incorrect displacement that an immediate-coordinate fixture missed. Use a consistent current-geometry calculation for movement, resize and anchor measurement. Native inventory rebuilds must not overwrite the saved independent bank placement.

`Client.isDraggingWidget()` may remain true when `getDraggedWidget()` is null after a completed drag. Treat a native drag as active only when both indicate one. This reproduced all anchor headers and resize corners becoming unresponsive, and also affected input-dock buttons. Preserve rejection while a real native drag is active. Do not use an arbitrary timeout to clear the game's drag state.

AWT mouse handling should use the last rendered immutable hit map. Revalidate generation, active mode, current occlusion and relevant availability on the client thread before applying the action. Full-button world-click blocking and full-button activation are separate behaviors; test both corners and empty padding, not only text/icon pixels.

Chat dock input selection must remain separate from visible chat-tab selection. Public can appear correctly selected while the game's default routing still directs the message to Clan. Test native script routing, input preview refresh, explicit user prefixes, typed-text preservation, modal dialogs, item selection and completed widget drags. Do not turn a performance optimization into outgoing-text rewriting or generated input.

## Bank rebuilds and scrolling

The bank's custom wheel handler updated widget scrollY but left native `VarClientID.BANK_SCROLLPOS` (51) stale. `BANKMAIN_FINISHBUILDING` (script 505) restored that old value during deposits and withdrawals. Update the native scroll state and widget together inside the existing client-thread callback. Test repeated deposits/withdrawals after scrolling, native tab/search resets, clamping, and the separate Bank Tags scroll area.

When the active UI and an anchor adapter must share a layout controller, ensure they receive the same instance, for example through the appropriate singleton scope. Otherwise membership can appear correct while the adapter updates an inactive controller and the window does not follow. Repairing that ownership defect does not establish the cause of separate coordinate, scroll or input regressions.

Native bank scripts can rebuild button positions between plugin events. Restore only owned changes before native script work and reapply after the relevant script finishes/before drawing. Test deposit/withdraw rebuilds, right-click menus, Alt without dragging, moving, resize corners and reopen. A cached/rendered helper rectangle must not feed back into saved bank size; prior live reports included shrinking on Alt and incremental shrink/bounce while dragging.

For axis-constrained button strips, preserve the intended sliding direction and gaps. On shrink, resolve collisions and overflow according to the chosen layout policy while retaining order. Keep preferred positions separate from the fitted render plan so expanding restores them. Reflow should not write a permanently compacted layout during every render. The Bank Tags divider's minimum space must include fitted/overflow buttons.

## Anchor ownership, occlusion and editing

- Distinguish AVAILABLE, OCCLUDED and UNAVAILABLE. A custom circular renderer may intentionally hide native minimap/compass widgets while an interface covers them. Treating that as UNAVAILABLE released the anchor lease, restored old coordinates, and produced repeated detach/reattach flicker. Preserve membership and last valid dimensions through rendering-owned occlusion. Genuine game hiding and destroyed widget identities remain unavailable; never force game-hidden UI visible.
- Start a drag from the visible clamped anchor rectangle, and resize from its current content-expanded dimensions. Starting from persisted off-screen coordinates or smaller saved minima created dead zones. Preserve click-without-movement, reference-point placement, negative Free offsets and Undo.
- If headers are designed outside an anchor, reserve their space; near the canvas edge use the visible header/hit region consistently. Reaching the top edge is not a mouse-exit cancellation. Convert stretched/device/canvas coordinates exactly once.
- A valid drop outside every anchor but inside the canvas detaches at the new location. Commit the provider geometry before releasing with keep-position semantics. The initial planner treated every outside drop as cancellation; that was an implementation gap, not proven fallout from the bank singleton change. Locked targets, expired generations and off-canvas drops still cancel safely.
- Disabled anchors release members; re-enabling reclaims them. Locked anchors retain layout and membership while blocking edits. Test at least two anchors, expanded members, headers and resize corners after ordinary native drags.
- Providers and owners need explicit generation/lease semantics. A stale asynchronous callback must not move or release members belonging to a newer profile, owner or lifecycle. Restore only state actually owned, and do not resurrect an overlay removed by its plugin.
- Explicit adapters can cover supported native controls and plugin-specific containers. Generic attachment is limited to compatible movable RuneLite overlays and infobox groups, not every arbitrary DYNAMIC overlay or native widget. If drag-to-attach is offered, make eligibility and any opt-in discoverable; do not imply every overlay can attach.
- `OverlayManager.add` loads saved placement. In fixtures and integrations, applying a desired starting position before add can be overwritten. Test the manager's real load/reset/save behavior and final rendered layer.

## Layering, timers and sprite identity

Layer choice alone does not prove final ordering. RuneLite's manager can promote positioned overlays (see [runtime.md](runtime.md)). Native minimap contents, POH facility icons, compass, free orbs and bank interfaces also involve native widget/script ordering. Validate the complete stack with overlap, movement and cover/uncover. Compass and orbs may overlap the minimap, while modal interfaces still cover them. Render-layer changes must also update click/scroll occlusion.

Mirror and align against the displayed circle or displayed number-tab geometry, not the hidden tab footprint. Include SRA's separate extra-special overlay, shield special, attached meters, timers, click masks and screen-edge release. Test every supported timer style in each display mode, amount-only/countdown-only/both where offered, fast prayer drain, changed prayer bonus and rapid prayer toggles. Avoid reintroducing phase jumps by replacing observed per-point timing with a naive modulo of every recalculated drain interval. Preserve the existing prayer-dose/low-prayer cues independently of timer artwork.

Resource-pack identity/readiness and the deletion report are covered in [integrations.md](integrations.md#resource-packs).

## Independent layout controls and item spacing

Saved window geometry and optional custom controls are separate settings. Turning off a toolbar should not reset the saved window position unless that behavior is explicitly intended. Test each toggle against layout/plugin disable, fixed mode, native rebuilds and saved custom placements.

For tighter bank columns, retain native item dimensions and separate withdrawal areas. One tested design preserves ordinary 36x32 slots and a minimum gap, leaves designed Bank Tags/equipment layouts alone, and skips compact reflow for nonstandard widget sizes. Select spacing from the actual geometry; do not assume these dimensions apply to every future client or plugin. This cannot guarantee control over arbitrary artwork drawn outside widget bounds. Check large artwork, quantities/outlines, edge clicks, saved layouts and narrow-bank resizing.

## Resource timer estimate boundaries

Distinguish actual resource changes, observed rates, natural regeneration, and known potion pulses from predicted future food effects. An observed prayer gain is not a model of every prayer-restoring food. A natural HP-full estimate must not imply that a pending delayed heal, such as antelope, is predicted. State the supported estimates, invalidate them when their assumptions change, and evaluate gameplay restrictions separately.
