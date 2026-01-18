from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .accepted_driver_permit import AcceptedDriverPermit
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AcceptedDriverPermitsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "acceptedDriverPermits_RelStructure"

    accepted_driver_permit: Iterable[AcceptedDriverPermit] = field(
        default_factory=list,
        metadata={
            "name": "AcceptedDriverPermit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
