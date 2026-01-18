from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .headway_use_enumeration import HeadwayUseEnumeration
from .journey_frequency_group_version_structure import (
    JourneyFrequencyGroupVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadwayJourneyGroupVersionStructure(
    JourneyFrequencyGroupVersionStructure
):
    class Meta:
        name = "HeadwayJourneyGroup_VersionStructure"

    scheduled_headway_interval: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "ScheduledHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_headway_interval: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MinimumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_headway_interval: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headway_display: None | HeadwayUseEnumeration = field(
        default=None,
        metadata={
            "name": "HeadwayDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
