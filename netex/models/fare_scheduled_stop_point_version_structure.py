from dataclasses import dataclass, field
from typing import Optional
from netex.models.border_point_ref import BorderPointRef
from netex.models.fare_scheduled_stop_point_ref_structure import FareScheduledStopPointRefStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.scheduled_stop_point_version_structure import ScheduledStopPointVersionStructure
from netex.models.site_facility_set import SiteFacilitySet
from netex.models.site_facility_set_ref import SiteFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareScheduledStopPointVersionStructure(ScheduledStopPointVersionStructure):
    class Meta:
        name = "FareScheduledStopPoint_VersionStructure"

    site_facility_set_ref: Optional[SiteFacilitySetRef] = field(
        default=None,
        metadata={
            "name": "SiteFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_facility_set: Optional[SiteFacilitySet] = field(
        default=None,
        metadata={
            "name": "SiteFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
