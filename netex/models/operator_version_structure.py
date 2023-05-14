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
    postal_address_or_road_address_or_address: Optional[object] = field(
        default=None,
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
            ),
        }
    )
    primary_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "PrimaryMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_activities: List[OperatorActivitiesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OperatorActivities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    customer_service_contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "CustomerServiceContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departments: Optional[DepartmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
