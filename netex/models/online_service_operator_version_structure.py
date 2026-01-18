from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ForwardRef

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

    country_ref: CountryRef | None = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    address: (
        PostalAddress
        | RoadAddress
        | OnlineServiceOperatorVersionStructure.Address
        | None
    ) = field(
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
                    "type": ForwardRef(
                        "OnlineServiceOperatorVersionStructure.Address"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    services: OnlineServiceRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class Address(PostalAddressVersionStructure):
        members: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        key_list: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        extensions: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        branding_ref: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        validity_conditions_or_valid_between: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        alternative_texts: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
