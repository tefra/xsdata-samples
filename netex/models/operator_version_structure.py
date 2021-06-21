from dataclasses import dataclass, field
from typing import List, Optional
from .contact_structure import ContactStructure
from .country_ref import CountryRef
from .departments_rel_structure import DepartmentsRelStructure
from .operator_activities_enumeration import OperatorActivitiesEnumeration
from .organisation_version_structure import OrganisationVersionStructure
from .postal_address import PostalAddress
from .postal_address_version_structure import PostalAddressVersionStructure
from .road_address import RoadAddress
from .vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatorVersionStructure(OrganisationVersionStructure):
    class Meta:
        name = "Operator_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Address",
                    "type": PostalAddressVersionStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PrimaryMode",
                    "type": VehicleModeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorActivities",
                    "type": List[OperatorActivitiesEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": lambda: [
            OperatorActivitiesEnumeration.PASSENGER,
        ],
                    "tokens": True,
                },
                {
                    "name": "CustomerServiceContactDetails",
                    "type": ContactStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "departments",
                    "type": DepartmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 4,
        }
    )
