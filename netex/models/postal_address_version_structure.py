from dataclasses import dataclass, field
from typing import Optional

from .address_ref_structure import AddressRefStructure
from .address_version_structure import AddressVersionStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PostalAddressVersionStructure(AddressVersionStructure):
    class Meta:
        name = "PostalAddress_VersionStructure"

    house_number: str | None = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    building_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    address_line1: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "AddressLine1",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    address_line2: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "AddressLine2",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    street: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    town: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Town",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suburb: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Suburb",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    post_code: str | None = field(
        default=None,
        metadata={
            "name": "PostCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    post_code_extension: str | None = field(
        default=None,
        metadata={
            "name": "PostCodeExtension",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_region: str | None = field(
        default=None,
        metadata={
            "name": "PostalRegion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    province: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Province",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_address_ref: AddressRefStructure | None = field(
        default=None,
        metadata={
            "name": "RoadAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
