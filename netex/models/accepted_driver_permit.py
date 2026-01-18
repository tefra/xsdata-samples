from __future__ import annotations

from dataclasses import dataclass

from .accepted_driver_permit_version_structure import (
    AcceptedDriverPermitVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AcceptedDriverPermit(AcceptedDriverPermitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
