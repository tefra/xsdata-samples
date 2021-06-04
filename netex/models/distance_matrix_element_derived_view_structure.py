from dataclasses import dataclass, field
from typing import Optional
from netex.models.derived_view_structure import DerivedViewStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "DistanceMatrixElement_DerivedViewStructure"

    start_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_tariff_zone_ref: Optional[TariffZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "StartTariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "StartName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_tariff_zone_ref: Optional[TariffZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "EndTariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "EndName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
