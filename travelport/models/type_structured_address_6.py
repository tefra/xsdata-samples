from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_reservation_info_ref_6 import (
    ProviderReservationInfoRef6,
)
from travelport.models.state_6 import State6
from travelport.models.type_element_status_6 import TypeElementStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeStructuredAddress6:
    """
    A fully structured address.

    Parameters
    ----------
    address_name
    street
        The Address street and number, e.g. 105 Main St.
    city
        The city name for the requested address, e.g. Atlanta.
    state
        The State or Province of address requested, e.g. CA, Ontario.
    postal_code
        The 5-15 alphanumeric postal Code for the requested address, e.g.
        90210.
    country
        The Full country name or two letter ISO country code e.g. US,
        France. A two letter country code is required for a Postal Code
        Searches.
    provider_reservation_info_ref
        Tagging provider reservation info with Address.
    key
        Key for update/delete of the element
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "typeStructuredAddress"

    address_name: None | str = field(
        default=None,
        metadata={
            "name": "AddressName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "max_length": 128,
        },
    )
    street: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 255,
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "min_length": 2,
            "max_length": 50,
        },
    )
    state: None | State6 = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "min_length": 1,
            "max_length": 15,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "length": 2,
        },
    )
    provider_reservation_info_ref: list[ProviderReservationInfoRef6] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
            "max_occurs": 99,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus6 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
