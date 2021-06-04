from dataclasses import dataclass, field
from typing import Optional
from netex.models.infrastructure_link_restriction_version_structure import InfrastructureLinkRestrictionVersionStructure
from netex.models.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RestrictedManoeuvreVersionStructure(InfrastructureLinkRestrictionVersionStructure):
    class Meta:
        name = "RestrictedManoeuvre_VersionStructure"

    vehicle_type_ref: Optional[VehicleTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
