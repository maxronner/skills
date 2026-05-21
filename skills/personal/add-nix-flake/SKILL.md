---
name: add-nix-flake
description: Add or improve a minimal Nix flake for repo-local development shells and checks without over-engineering packaging. Use when the user wants to create a flake, nixify a project, add a devShell, or debug first-time flake setup.
---

# Add Nix Flake

Add or improve a small repo-local `flake.nix` for development. Optimize for repeatable shells and verification, not elaborate packaging.

Core footgun: Nix flakes only evaluate files known to Git. If a new file is referenced by the flake or by code evaluated during flake checks, run `git add` or `git add -N` before `nix flake check` / `nix develop`.

## Default Posture

- Keep the flake minimal.
- Prefer `devShells.default` before packaging the app.
- Do not replace existing project tooling; expose it inside Nix.
- Prefer putting language toolchains and package managers in the shell; do not translate the project's dependency graph into Nix unless asked.
- Do not add `direnv`, overlays, NixOS modules, Cachix, deployment, or custom builders unless asked.
- Do not update existing pins unless asked or required.
- If the repo already has Nix, follow its style instead of introducing a new one.

## Process

### 1. Inspect

Read likely entry points before writing:

- existing `flake.nix`, `flake.lock`, `shell.nix`, `default.nix`, `.envrc`
- `README.md`, `AGENTS.md`, `CLAUDE.md`
- language/tool files: `package.json`, `pnpm-lock.yaml`, `Cargo.toml`, `pyproject.toml`, `go.mod`, `justfile`, `Makefile`
- CI files for expected checks

Identify:

- package manager and lockfile
- dev tools needed in the shell
- existing test/lint/build commands
- whether the goal is dev shell only, checks, package output, or app runtime

Ask before adding packaging if the user only requested a shell.

### 2. Choose The Smallest Useful Shape

Usually create:

- `description`
- `inputs.nixpkgs`
- `outputs = { self, nixpkgs }: ...`
- one target system if personal/local, or a tiny systems loop if the repo needs multiple systems
- `devShells.default`
- optional `formatter`
- optional `checks` that wrap existing fast repo commands

Prefer boring `pkgs.mkShell` unless the repo already uses another pattern.

### 3. Add Files Carefully

When creating or changing files that Nix must see:

```bash
git add -N flake.nix
test -f flake.lock && git add -N flake.lock
```

If a check imports newly-created source files, add those too before evaluating:

```bash
git add -N path/to/new-file
```

Use real `git add` when the user is comfortable staging, otherwise use `git add -N` so flakes can see the paths without staging content.

For first-time flakes, `nix flake check` may create `flake.lock`; running `nix flake lock` explicitly is also fine. Do not silently update existing pins unless the user asked or the change is required.

### 4. Example Minimal Flake

Use as a starting point, then adapt packages to the repo. Do not invent Nix package attribute names; confirm uncertain tools with `nix search nixpkgs <tool>` or `nix eval nixpkgs#<attr>.name`.

```nix
{
  description = "Development shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          git
        ];
      };

      formatter.${system} = pkgs.nixfmt-rfc-style;
    };
}
```

For another system, use the current machine's system from `nix eval --impure --expr builtins.currentSystem` if needed.

### 5. Verify

Run the narrowest useful commands:

```bash
nix flake check
nix develop -c <repo-check-command>
```

If `nix flake check` says a path does not exist but it does, check whether the file is untracked and run `git add -N <path>`.

If a tool is missing from the shell, find the correct Nix package attribute, add it to `devShells.default`, and retry with `nix develop -c ...`.

### 6. Report

Summarize:

- whether this is devShell-only or includes checks/packages
- which tools the shell provides
- what verification ran
- any files that needed `git add -N` for flake visibility
- what was intentionally not added, such as direnv, packaging, overlays, or deployment
