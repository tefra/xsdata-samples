from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_line_2 import AddressLine2
from travelport.models.type_contact_purpose_2 import TypeContactPurpose2
from travelport.models.type_key_tagged_element_2 import TypeKeyTaggedElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeAddressHistory2(TypeKeyTaggedElement2):
    """
    Profile Address.

    Parameters
    ----------
    address_line
        An Address can have 1 to 3 address lines for any use. The Address
        Lines are assumed in order.
    city
        The city of which this address is located.
    state
        The state of which this address is located.
    other_state_province
        Alternate freeform state value
    country
        The country of which this address is located.
    postal
        The postal code of which this address is located.
    type_value
        Category of address (Mailing, Shipping, ...)
    purpose
        A code for categorizing a contact mechanism based on purpose or use.
        Examples include business, persona., etc.
    provisioned
        Indicator to show if this address is used as the provisioned
        address.
    priority_order
        Priority order associated with this Address.
    delivery_description
        An optional description detailing the delivery.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "typeAddressHistory"

    address_line: list[AddressLine2] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 3,
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "max_length": 128,
        },
    )
    state: None | str = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    other_state_province: None | str = field(
        default=None,
        metadata={
            "name": "OtherStateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "length": 2,
        },
    )
    postal: None | str = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Attribute",
            "max_length": 12,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    purpose: None | TypeContactPurpose2 = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        },
    )
    provisioned: None | bool = field(
        default=None,
        metadata={
            "name": "Provisioned",
            "type": "Attribute",
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    delivery_description: None | str = field(
        default=None,
        metadata={
            "name": "DeliveryDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        },
    )
