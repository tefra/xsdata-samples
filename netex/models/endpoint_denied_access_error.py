from __future__ import annotations

from dataclasses import dataclass

from .endpoint_denied_access_structure import EndpointDeniedAccessStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EndpointDeniedAccessError(EndpointDeniedAccessStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
