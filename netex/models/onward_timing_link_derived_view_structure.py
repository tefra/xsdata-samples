from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDuration

from .derived_view_structure import DerivedViewStructure
from .timing_link_in_journey_pattern_ref import TimingLinkInJourneyPatternRef
from .timing_link_ref import TimingLinkRef
from .timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnwardTimingLinkDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "OnwardTimingLink_DerivedViewStructure"

    timing_link_in_journey_pattern_ref: (
        TimingLinkInJourneyPatternRef | None
    ) = field(
        default=None,
        metadata={
            "name": "TimingLinkInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_link_ref: TimingLinkRef | None = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_ref: TimingPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Decimal | None = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_time: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
