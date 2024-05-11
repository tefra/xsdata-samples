from dataclasses import dataclass

from .accepted_driver_permit_ref_structure import (
    AcceptedDriverPermitRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AcceptedDriverPermitRef(AcceptedDriverPermitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
