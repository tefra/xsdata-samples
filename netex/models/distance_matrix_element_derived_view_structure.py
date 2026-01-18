from dataclasses import dataclass, field
from typing import Optional, Union

from .derived_view_structure import DerivedViewStructure
from .multilingual_string import MultilingualString
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "DistanceMatrixElement_DerivedViewStructure"

    start_stop_point_ref_or_start_tariff_zone_ref: ScheduledStopPointRefStructure | TariffZoneRefStructure | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    start_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "StartName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_stop_point_ref_or_end_tariff_zone_ref: ScheduledStopPointRefStructure | TariffZoneRefStructure | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    end_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "EndName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
