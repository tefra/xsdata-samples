from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferDurationStructure:
    default_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DefaultDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequent_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FrequentTravellerDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    occasional_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "OccasionalTravellerDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mobility_restricted_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MobilityRestrictedTravellerDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
