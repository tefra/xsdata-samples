from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDuration

from .derived_view_structure import DerivedViewStructure
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from .service_link_ref import ServiceLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnwardServiceLinkDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "OnwardServiceLink_DerivedViewStructure"

    service_link_in_journey_pattern: None | ServiceLinkInJourneyPattern = (
        field(
            default=None,
            metadata={
                "name": "ServiceLinkInJourneyPattern",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    service_link_ref: None | ServiceLinkRef = field(
        default=None,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_ref: None | ScheduledStopPointRefStructure = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: None | Decimal = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
