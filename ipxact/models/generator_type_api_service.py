from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class GeneratorTypeApiService(Enum):
    SOAP = "SOAP"
    REST = "REST"
