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

    house_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    building_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    address_line1: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "AddressLine1",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    address_line2: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "AddressLine2",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    street: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    town: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Town",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suburb: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Suburb",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    post_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    post_code_extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostCodeExtension",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_region: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalRegion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    province: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Province",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_address_ref: Optional[AddressRefStructure] = field(
        default=None,
        metadata={
            "name": "RoadAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
