# Migrating PyLops codes from V1 to V2

This file is intended to guide users willing to convert their codes from PyLops v1 to PyLops v2.

In the following we provide a detailed description of all the breaking changes introduced in v2, which
should be used as a checklist when converting a piece of code using PyLops from v1 to v2.

- XX
- XX
- XX

- `utils.dottest`: The relative tolerance is new set via `rtol` (before `tol`), and absolute tolerance is new supported via the keyword `atol`. When calling it with purely positional arguments, note that after `rtol` comes now first `atol` before `complexflag`. When using `raiseerror=True` it now emits an `AttributeError` instead of a `ValueError`.