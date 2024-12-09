# [IPEXACT](https://github.com/edaa-org/IPXACT-Schema) - 1685-2022

## Notes

- Circular imports: resolved with clusters.
- Elements and ComplexTypes with same name in the same target namespace conflicts.
- Three of the original samples fail validation and we skip them.

## Invoke Commands

```console
$ inv ipxact.build
$ inv ipxact.test
$ inv ipxact.mypy
```
