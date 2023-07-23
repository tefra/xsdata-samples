from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_tckey_element import TypeTckeyElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeAddress1(TypeTckeyElement):
    """
    Profile Address.

    Parameters
    ----------
    address_line
        An Address can have 1 to 3 address lines for any use.  The Address
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
        Category of address (Mailing, Shipping, Collection, Other, Delivery,
        Location, Billing, LocalLangInvoice, Home, Work). Util:
        ReferenceDataRetrieveReq, TypeCode PostalAddressType
    """
    class Meta:
        name = "typeAddress"

    address_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            "min_occurs": 1,
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 128,
        }
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    state: None | str = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    other_state_province: None | str = field(
        default=None,
        metadata={
            "name": "OtherStateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "length": 2,
        }
    )
    postal: None | str = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Attribute",
            "max_length": 12,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
