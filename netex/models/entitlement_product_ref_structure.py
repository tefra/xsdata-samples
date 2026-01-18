from __future__ import annotations

from dataclasses import dataclass

from .service_access_right_ref_structure import ServiceAccessRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementProductRefStructure(ServiceAccessRightRefStructure):
    pass
