from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .assistance_booking_service import AssistanceBookingService
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceBookingServicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "assistanceBookingServices_RelStructure"

    assistance_booking_service_ref_or_assistance_booking_service: Sequence[
        AssistanceBookingServiceRef | AssistanceBookingService
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AssistanceBookingServiceRef",
                    "type": AssistanceBookingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingService",
                    "type": AssistanceBookingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
