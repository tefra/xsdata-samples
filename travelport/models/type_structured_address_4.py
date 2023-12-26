from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_reservation_info_ref_4 import (
    ProviderReservationInfoRef4,
)
from travelport.models.type_element_status_4 import TypeElementStatus4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class TypeStructuredAddress4:
    """
    A fully structured address.

    Parameters
    ----------
    address_name
    street
    city
    state
    postal_code
    country
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
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_length": 128,
        },
    )
    street: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
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
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "min_length": 2,
            "max_length": 50,
        },
    )
    state: None | str = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "min_length": 1,
            "max_length": 15,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "length": 2,
        },
    )
    provider_reservation_info_ref: list[ProviderReservationInfoRef4] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus4 = field(
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
