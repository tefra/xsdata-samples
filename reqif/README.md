# [Requirements Interchange Format](https://github.com/CONNECT-Solution/Common-Types/)

RIF/ReqIF is an XML file format that can be used to exchange requirements, along with
its associated metadata, between software tools from different vendors. The requirements
exchange format also defines a workflow for transmitting the status of requirements
between partners.

## CodeGen

This suite is very complex will a lot if circular imports. The only way to produce valid
python dataclass models is through the `xsdata --ns-struct` option that groups classes
by target namespace.

Test with pypy against output validate serializer output.

## Makefile commands

```console
$ ./run.py build reqif
$ ./run.py test reqif
$ ./run.py mypy reqif
```
