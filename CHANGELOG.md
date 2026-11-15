# Changelog

## [Unreleased]
### Added
- labware: 5 device-library records from NOTABLE / NOTABLE-96 Neon (keys = Neon codes; show=false, verified_ablelabs=false)
- pipettes: 8ch/1ch records with public values only (channel, working_volume, flow_rate default/max)
- aliases: new collection mapping reference keys to NOTABLE / NOTABLE-96 Neon codes and product codes (not yet checked by scripts/validate.py)

## [v1.0.0] - 2026-04-29
### Added
- Initial repository structure
- Labware, Modules, Liquid collections with JSON Schema
- Validation script with pre-commit hook
