from __future__ import annotations

from dataclasses import dataclass

from .service_access_right_version_structure import (
    ServiceAccessRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceAccessRight1(ServiceAccessRightVersionStructure):
    class Meta:
        name = "ServiceAccessRight"
        namespace = "http://www.netex.org.uk/netex"
