from __future__ import annotations

from dataclasses import dataclass

from generali.models.org.w3.pkg_2005.pkg_08.addressing.endpoint_reference_type import (
    EndpointReferenceType,
)

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class From(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"
