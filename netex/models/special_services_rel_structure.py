from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .special_service import SpecialService
from .special_service_ref import SpecialServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpecialServicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "specialServices_RelStructure"

    dated_special_service_ref_or_special_service_ref_or_special_service: Iterable[
        DatedSpecialServiceRef | SpecialServiceRef | SpecialService
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialService",
                    "type": SpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
