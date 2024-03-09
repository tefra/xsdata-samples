from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .headway_use_enumeration import HeadwayUseEnumeration
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrequencyStructure:
    scheduled_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ScheduledHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headway_display: Optional[HeadwayUseEnumeration] = field(
        default=None,
        metadata={
            "name": "HeadwayDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frequency_regulated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrequencyRegulated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
