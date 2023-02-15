# Contributing

All VBL projects are licensed open-source and your pull requests are welcome.

## Guidelines

## Code style

### Unity

#### Variables

private type _camelCase;
[SerializeField] private type _camelCase;

public type PascalCase;

public void PascalCase(type camelCase) {}

#### Coordinates

Use the suffix `Coord` to make it clear that a variable is a coordinate in a CoordinateSpace. Add `CoordU` or `CoordT` to clarify if it is transformed or not. Use `WorldU` and `WorldT` to refer to coordinates in Unity space.

#### Editor Conventions

GameObjects are defined in PascalCase

### Python