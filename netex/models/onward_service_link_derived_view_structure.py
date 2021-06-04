from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.models.derived_view_structure import DerivedViewStructure
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from netex.models.service_link_ref import ServiceLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnwardServiceLinkDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "OnwardServiceLink_DerivedViewStructure"

    service_link_in_journey_pattern: Optional[ServiceLinkInJourneyPattern] = field(
        default=None,
        metadata={
            "name": "ServiceLinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_link_ref: Optional[ServiceLinkRef] = field(
        default=None,
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    run_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
