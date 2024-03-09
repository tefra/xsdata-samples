from dataclasses import dataclass

from generali.models.org.w3.pkg_2006.pkg_02.addressing.wsdl.service_name_type import (
    ServiceNameType,
)

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


@dataclass
class ServiceName(ServiceNameType):
    class Meta:
        namespace = "http://www.w3.org/2006/02/addressing/wsdl"
