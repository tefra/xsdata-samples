from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDuration

from .derived_view_structure import DerivedViewStructure
from .timing_link_in_journey_pattern_ref import TimingLinkInJourneyPatternRef
from .timing_link_ref import TimingLinkRef
from .timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnwardTimingLinkDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "OnwardTimingLink_DerivedViewStructure"

    timing_link_in_journey_pattern_ref: (
        None | TimingLinkInJourneyPatternRef
    ) = field(
        default=None,
        metadata={
            "name": "TimingLinkInJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_link_ref: None | TimingLinkRef = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_ref: None | TimingPointRefStructure = field(
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
