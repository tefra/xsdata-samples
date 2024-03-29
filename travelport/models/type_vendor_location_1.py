from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class TypeVendorLocation1:
    """
    Parameters
    ----------
    provider_code
        The code of the provider (e.g. 1G, 1S)
    vendor_code
        The code of the vendor (e.g.  HZ, etc.)
    preferred_option
        Preferred Option marker for Location.
    vendor_location_id
        Location identifier
    key
        Key which maps vendor location with vehicles
    more_rates_token
        Enter the Token when provided by hotel property, more rates exist.
        HADS/HSS  support only.
    """

    class Meta:
        name = "typeVendorLocation"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    preferred_option: None | bool = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        },
    )
    vendor_location_id: None | str = field(
        default=None,
        metadata={
            "name": "VendorLocationID",
            "type": "Attribute",
            "min_length": 1,
            "white_space": "collapse",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    more_rates_token: None | str = field(
        default=None,
        metadata={
            "name": "MoreRatesToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        },
    )
