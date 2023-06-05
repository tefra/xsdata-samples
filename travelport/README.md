# Travelport: GDS

## Universal [AIR Schema](https://support.travelport.com/webhelp/uapi/uAPI.htm#Air/Air_Schema_Overview.htm)

- Auto generated models and services from the `air_v48_0/Air.wsdl`
- Serialization test for `LowFareSearchReq` sample from json -> python -> xml

The given schema is an excellent example for grouping together multiple root models,
and mixing namespaces.

## Makefile commands

```console
$ ./run.py build travelport
$ ./run.py test travelport
$ ./run.py mypy travelport
```
