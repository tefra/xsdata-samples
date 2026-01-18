from dataclasses import dataclass, field
from typing import Optional, Union

from .access_zone_ref import AccessZoneRef
from .administrative_zone_ref import AdministrativeZoneRef
from .fare_zone_ref import FareZoneRef
from .group_of_points_version_structure import GroupOfPointsVersionStructure
from .mobility_service_constraint_zone_ref import (
    MobilityServiceConstraintZoneRef,
)
from .stop_area_ref import StopAreaRef
from .tariff_zone_ref import TariffZoneRef
from .transport_administrative_zone_ref import TransportAdministrativeZoneRef
from .zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleFeatureVersionStructure(GroupOfPointsVersionStructure):
    class Meta:
        name = "SimpleFeature_VersionStructure"

    zone_ref_or_tariff_zone_ref: MobilityServiceConstraintZoneRef | StopAreaRef | TransportAdministrativeZoneRef | AccessZoneRef | AdministrativeZoneRef | FareZoneRef | TariffZoneRef | ZoneRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityServiceConstraintZoneRef",
                    "type": MobilityServiceConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopAreaRef",
                    "type": StopAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZoneRef",
                    "type": TransportAdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneRef",
                    "type": ZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
