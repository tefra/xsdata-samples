from dataclasses import dataclass, field
from typing import Optional, Union
from .country_ref import CountryRef
from .online_service_refs_rel_structure import OnlineServiceRefsRelStructure
from .organisation_version_structure import OrganisationVersionStructure
from .postal_address import PostalAddress
from .postal_address_version_structure import PostalAddressVersionStructure
from .road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnlineServiceOperatorVersionStructure(OrganisationVersionStructure):
    class Meta:
        name = "OnlineServiceOperator_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    address: Optional[
        Union[PostalAddress, RoadAddress, PostalAddressVersionStructure]
    ] = field(
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
        },
    )
    services: Optional[OnlineServiceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
