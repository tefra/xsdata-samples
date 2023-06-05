# [NPO API](https://github.com/npo-poms)

## Download

```console
$ xsdata download https://rs.poms.omroep.nl/v1/schema/urn:vpro:api:2013 --output npo/schemas
```

## Notes

This suite works a lot with **xs:anyType** derived elements and the binding tests
check the lookup capabilities of the xml parser.

## Makefile commands

```console
$ ./run.py build npo
$ ./run.py test npo
$ ./run.py mypy npo
```
