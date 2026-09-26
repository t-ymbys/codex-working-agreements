---
name: local-first-app-development
description: Keep app and game work local unless the user explicitly requests release through a named channel. Use when building, modifying, testing, previewing, packaging, publishing, releasing, or cleaning up an app or game.
---

# Local-First App Development

## Default Boundary

Keep application and game work local unless the user explicitly requests release or distribution through a named channel.

Do not treat requests such as “build it,” “make the game,” “show me,” “preview it,” or “finish it” as permission to:

- deploy or host the app;
- create a public or private production URL;
- create a cloud site or remote repository;
- upload source, builds, user data, or telemetry;
- distribute the artifact externally.

Use localhost or an equivalent local preview for validation. Stop temporary preview processes when validation is complete.

## Explicit Release Exception

Only consider external publication after the user explicitly names and requests the release or sales channel, such as the Apple App Store or Steam. Before changing external state, confirm:

- exact destination and account;
- intended audience and visibility;
- exact artifact and version;
- pricing or sales status when applicable;
- data collection and privacy behavior;
- rollback, takedown, or delisting path.

Do not infer release permission from deployment configuration, a previously deployed version, or a request to package a local build.

## Cleanup After Unintended Publication

When an app was placed online without an explicit release request:

1. Stop further deployment.
2. Restrict access immediately if complete removal is not yet available.
3. Inventory remote source, deployments, saved versions, databases, object storage, environment variables, custom domains, access grants, and automations.
4. Remove or deactivate only resources the platform supports removing, while preserving the local source.
5. Detach local deployment identifiers when doing so prevents accidental republishing.
6. Report verified removals and residual online artifacts separately. Never call access restriction, an empty data store, or a blank replacement deployment “deleted.”

## Stopping Condition

For ordinary development, stop after local validation and shut down temporary preview processes. For release or cleanup work, stop when the authorized external scope is complete, verified, and reported; do not expand to other accounts, channels, or resources without authorization.
