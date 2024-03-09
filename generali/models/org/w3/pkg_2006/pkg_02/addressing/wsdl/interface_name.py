from dataclasses import dataclass

from generali.models.org.w3.pkg_2006.pkg_02.addressing.wsdl.attributed_qname_type import (
    AttributedQnameType,
)

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


@dataclass
class InterfaceName(AttributedQnameType):
    class Meta:
        namespace = "http://www.w3.org/2006/02/addressing/wsdl"
