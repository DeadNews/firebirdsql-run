# Changelog

## [1.1.2-beta.0](https://github.com/DeadNews/firebirdsql-run/compare/v1.1.1...v1.1.2-beta.0) - 2024-04-07

### 📚 Documentation

- _(changelog)_ add `git-cliff` - ([a9d4baf](https://github.com/DeadNews/firebirdsql-run/commit/a9d4baf4c560797b9f298e4275a534ec07a5046e))
- _(changelog)_ add `git-cliff` - ([65fe4e2](https://github.com/DeadNews/firebirdsql-run/commit/65fe4e2bd5928936dde263f5eedcc00da01d5088))
- _(mkdocs)_ update ([#130](https://github.com/DeadNews/firebirdsql-run/issues/130)) - ([dabaf63](https://github.com/DeadNews/firebirdsql-run/commit/dabaf636900d12d9ba865be08ab06a37340cf5d6))
- _(readme)_ update badges - ([0ef83eb](https://github.com/DeadNews/firebirdsql-run/commit/0ef83ebe41dfd240bd28798db48305f7364e1882))
- _(readme)_ update badges - ([f6195c9](https://github.com/DeadNews/firebirdsql-run/commit/f6195c98a8a54719b803f6763d986ba4bdd6c210))
- _(readme)_ add badges - ([10bca60](https://github.com/DeadNews/firebirdsql-run/commit/10bca6066a19a04eaa6b883fb228c74228d35775))
- update docstrings - ([860dc75](https://github.com/DeadNews/firebirdsql-run/commit/860dc75a198162093ee703d4c7dc6c7cb33f4ea7))

## [1.1.1](https://github.com/DeadNews/firebirdsql-run/compare/v1.0.7...v1.1.1) - 2024-02-26

### 🚀 Features

- add `port` attribute to `CompletedTransaction` - ([db144a4](https://github.com/DeadNews/firebirdsql-run/commit/db144a4913a76fe16c4058c9f6c9257e8da29d89))
- add new parameter `access: read_write|read_only` ([#118](https://github.com/DeadNews/firebirdsql-run/issues/118)) - ([821489a](https://github.com/DeadNews/firebirdsql-run/commit/821489a8422e067934ee78fe731a62aceaf68d3e))

### 🐛 Bug fixes

- move line from the `try` block - ([91cbe3a](https://github.com/DeadNews/firebirdsql-run/commit/91cbe3a8e9824b7126dcbf435aa66e4cf7f47b59))
- adjust typing ([#111](https://github.com/DeadNews/firebirdsql-run/issues/111)) - ([43c2e7e](https://github.com/DeadNews/firebirdsql-run/commit/43c2e7ee9ce1a458f5d11f3d45e2640603a52df8))

### 🚜 Refactor

- `execute` function ([#122](https://github.com/DeadNews/firebirdsql-run/issues/122)) - ([ae3b993](https://github.com/DeadNews/firebirdsql-run/commit/ae3b99399bf374926cb5b3267cc486b21c36978e))

### 📚 Documentation

- _(readme)_ fix typo - ([3ff59a2](https://github.com/DeadNews/firebirdsql-run/commit/3ff59a2cfaaef6673adf5d32c59b58df9f0f63c8))
- add `mkdocs` ([#125](https://github.com/DeadNews/firebirdsql-run/issues/125)) - ([fb002ed](https://github.com/DeadNews/firebirdsql-run/commit/fb002ed85cd31c94b8e16c3d25a61adc1b462596))

### 🧹 Chores

- add config for `toml` formatter - ([8671ed2](https://github.com/DeadNews/firebirdsql-run/commit/8671ed22d9eae76b99d23960ae30ff47feda6088))
- update `ruff` settings - ([19894ca](https://github.com/DeadNews/firebirdsql-run/commit/19894caada7de2608a96610eb0b7734f29361be7))
- replace `black` with `ruff` - ([2c90e26](https://github.com/DeadNews/firebirdsql-run/commit/2c90e261a92a85fc5a5d033ff5e4c1d3bd37d050))

### ⚙️ CI/CD

- _(pre-commit)_ add `checkmake` hook - ([3baa8d6](https://github.com/DeadNews/firebirdsql-run/commit/3baa8d6d1ac7a0efba93f1155b4bb48f0ef1385b))
- _(pre-commit)_ add `actionlint` hook - ([2cd0df6](https://github.com/DeadNews/firebirdsql-run/commit/2cd0df6b93ef362b79cc8bafbaa8a8bceafd82dc))
- update `firebird` versions in tests matrix ([#121](https://github.com/DeadNews/firebirdsql-run/issues/121)) - ([69330a8](https://github.com/DeadNews/firebirdsql-run/commit/69330a89bfe059a2a899206395129c8814d735e3))
- add `python 3.12` to tests matrix ([#93](https://github.com/DeadNews/firebirdsql-run/issues/93)) - ([ab7978e](https://github.com/DeadNews/firebirdsql-run/commit/ab7978e834654cc5b63c328ac895f620ef65e5f1))

### ⬆️ Dependencies

- _(deps)_ update dependency firebirdsql to v1.2.5 ([#124](https://github.com/DeadNews/firebirdsql-run/issues/124)) - ([e72e63b](https://github.com/DeadNews/firebirdsql-run/commit/e72e63b292d4b8c3635897da42952cb516b0901a))
- _(deps)_ update dependency firebirdsql to v1.2.3 ([#110](https://github.com/DeadNews/firebirdsql-run/issues/110)) - ([623fbbc](https://github.com/DeadNews/firebirdsql-run/commit/623fbbcb361a2c3134a5990cb119a7004fccc0e3))

## [1.0.7](https://github.com/DeadNews/firebirdsql-run/compare/v1.0.6...v1.0.7) - 2023-09-12

### 📚 Documentation

- update `README` - ([b8cc602](https://github.com/DeadNews/firebirdsql-run/commit/b8cc6028a06b8be398e6b4fe0b9adf44bbf32db5))

### 🧹 Chores

- update docstrings ([#88](https://github.com/DeadNews/firebirdsql-run/issues/88)) - ([1e66d51](https://github.com/DeadNews/firebirdsql-run/commit/1e66d514d7b11b4278776e7392b9fb93d81e69fb))
- specify python `target-version` - ([b2a354a](https://github.com/DeadNews/firebirdsql-run/commit/b2a354a253b613d3aa4b1f9c4912e7260e41b003))

### ⚙️ CI/CD

- _(pre-commit)_ use `black` mirror ([#87](https://github.com/DeadNews/firebirdsql-run/issues/87)) - ([078ee6d](https://github.com/DeadNews/firebirdsql-run/commit/078ee6d99b63d0239dfc1661a2e278ff38418d7e))
- disable `codeql` on `schedule` - ([1b3afc8](https://github.com/DeadNews/firebirdsql-run/commit/1b3afc84d701461d4dbb2f8348f80286adaa9eb6))

## [1.0.6](https://github.com/DeadNews/firebirdsql-run/compare/v1.0.5...v1.0.6) - 2023-07-18

### 🚜 Refactor

- force ipv4 `localhost` - ([7834fef](https://github.com/DeadNews/firebirdsql-run/commit/7834fef4fa047b0f91025854f946aa77bb2225aa))

### ⚙️ CI/CD

- move `pytest` command - ([5b3018f](https://github.com/DeadNews/firebirdsql-run/commit/5b3018fe10c01f134b7bcc8512b072bb221258a9))

## [1.0.5](https://github.com/DeadNews/firebirdsql-run/compare/v1.0.4...v1.0.5) - 2023-07-08

### 🐛 Bug fixes

- move connection close to `finally` block ([#78](https://github.com/DeadNews/firebirdsql-run/issues/78)) - ([83f4fbb](https://github.com/DeadNews/firebirdsql-run/commit/83f4fbba59f6db8d18a41f415b6b0b6dcb43c7da))

### 🧹 Chores

- ignore `PLR0913` ruff rule - ([3a50234](https://github.com/DeadNews/firebirdsql-run/commit/3a502341355a51977bc39142b591fb4bf6bcad67))

### ⚙️ CI/CD

- _(renovate)_ adjust schedule - ([957e8d0](https://github.com/DeadNews/firebirdsql-run/commit/957e8d0e1f2de9440c04a9f5ecce89104ccdb51a))
- use `digest pinning` - ([2ff20ff](https://github.com/DeadNews/firebirdsql-run/commit/2ff20ff20396edd660a8f39eb50da755ed721ef7))

## [1.0.4](https://github.com/DeadNews/firebirdsql-run/compare/v1.0.3...v1.0.4) - 2023-05-30

### 🚜 Refactor

- separate modules ([#69](https://github.com/DeadNews/firebirdsql-run/issues/69)) - ([42eb6f1](https://github.com/DeadNews/firebirdsql-run/commit/42eb6f147cafa6affe6b1bd7ccd5a109f0a5be99))

### 📚 Documentation

- _(README)_ update - ([e84ba3e](https://github.com/DeadNews/firebirdsql-run/commit/e84ba3e8e2f72a8dcad43f8ac3c768527ca199bd))

## [1.0.3](https://github.com/DeadNews/firebirdsql-run/compare/v1.0.2...v1.0.3) - 2023-05-25

### 🚀 Features

- get passwd from `env` by default ([#68](https://github.com/DeadNews/firebirdsql-run/issues/68)) - ([da76539](https://github.com/DeadNews/firebirdsql-run/commit/da7653955cb8c4501fc917df0822f8be2405fb22))

### ⚙️ CI/CD

- _(pre-commit)_ add `typos` hook - ([a0a0731](https://github.com/DeadNews/firebirdsql-run/commit/a0a0731c906bb60a881633217a135a23f38a00ca))
- _(pre-commit)_ adjust schedule and rules - ([60d18c3](https://github.com/DeadNews/firebirdsql-run/commit/60d18c384eba08d57e07f0c2594de4a07463ddb0))
- _(renovate)_ use shared config - ([4a83cc4](https://github.com/DeadNews/firebirdsql-run/commit/4a83cc46b63fe1d75e5f95719f4f4bb652b3b5d8))
- update `workflows` ([#64](https://github.com/DeadNews/firebirdsql-run/issues/64)) - ([a437498](https://github.com/DeadNews/firebirdsql-run/commit/a4374984035d5f77d20639d94a35e68dc4eeb152))

## [1.0.2] - 2023-05-07

### 🚀 Features

- dev pr ([#55](https://github.com/DeadNews/firebirdsql-run/issues/55)) - ([de9b63e](https://github.com/DeadNews/firebirdsql-run/commit/de9b63eaafe6e90aff540aa1e8c50be08f72da02))

<!-- generated by git-cliff -->
