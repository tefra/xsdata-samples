# AUTOSAR [Foundation](https://www.autosar.org/standards/foundation/)

## Notes

This suite is following some unique patterns with a lot of naming conflicts
and inner types. Also demonstrates most likely a bug in mypy that doesn't allow
an outer class sharing the same name with an inner class.

- Auto generated models
- Verify parsing from sample


## Makefile commands

```console
$ make build-autosar
$ make test-autosar
```