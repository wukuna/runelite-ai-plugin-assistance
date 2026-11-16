# Performance and multi-client diagnosis

Measure the current workload and exact build. Historical sample shares, another user's hardware, or perceived improvements are not evidence of this client's bottleneck.

## Interpret measurements

Record game/login state, visible overlays, window focus, frame caps, client count and system CPU/GPU/memory load. Compare like-for-like intervals. Capture process CPU totals and timestamps together; slow counter collection with mismatched timestamps distorts calculated utilization.

Use thread snapshots or JFR where available and authorized. Client-thread sample shares are not whole-system CPU percentages. Allocation/TLAB samples are not retained heap size or proof of a leak. No reported Java deadlock and low measured GC pauses do not exclude earlier desktop stalls. A change after opening Task Manager is a correlation to reproduce, not a diagnosis of a driver problem or malware.

Prefer bounded recordings and streaming analysis over expanding every allocation stack into huge files. Keep profiling tools out of distributed plugins. Stop task-owned diagnostic processes and release capture sessions using the environment's documented cleanup when finished.

## Optimize without changing behavior

- Reuse traversal scratch only within a safe thread/reentrancy scope; clear widget references on normal and exceptional exits. Invalidate coordinates after scripts, scrolling or movement.
- Bound discovery scans by client cycle and invalidate on provider lifecycle/config changes. Cache empty results too, but keep geometry and ownership updates timely. Removing a provider must not let stale discovery resurrect it.
- Narrow input-occlusion work to the overlay's footprint, then recheck the exact click against current state before routing. Widgets may move after rendering.
- Measure whether repeated cost is geometry, paint creation, image work or something else before adding a cache. Preserve transforms, clipping, alpha, live color changes and edge continuity.
- Benchmark the same workload after installing the verified build. Separate automated correctness checks, measured results and untested performance expectations.
