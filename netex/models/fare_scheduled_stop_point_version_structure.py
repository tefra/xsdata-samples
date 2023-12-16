from dataclasses import dataclass, field
from typing import Optional, Union
from .border_point_ref import BorderPointRef
from .fare_scheduled_stop_point_ref_structure import FareScheduledStopPointRefStructure
from .multilingual_string import MultilingualString
from .scheduled_stop_point_version_structure import ScheduledStopPointVersionStructure
from .site_facility_set import SiteFacilitySet
from .site_facility_set_ref import SiteFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareScheduledStopPointVersionStructure(ScheduledStopPointVersionStructure):
    class Meta:
        name = "FareScheduledStopPoint_VersionStructure"

    site_facility_set_ref_or_site_facility_set: Optional[Union[SiteFacilitySetRef, SiteFacilitySet]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SiteFacilitySetRef",
                    "type": SiteFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFacilitySet",
                    "type": SiteFacilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    name_on_routing: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameOnRouting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accounting_stop_point_ref: Optional[FareScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "AccountingStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_point_ref: Optional[BorderPointRef] = field(
        default=None,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
