from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from .call_versioned_child_structure import CallVersionedChildStructure
from .driver_ref import DriverRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedCallVersionedChildStructure(CallVersionedChildStructure):
    class Meta:
        name = "DatedCall_VersionedChildStructure"

    driver_ref: None | DriverRef = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    arrival_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ArrivalDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
