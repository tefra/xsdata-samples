from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ReferenceDataSearchRsp(BaseRsp1):
    """
    Response the sought reference data item.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    airport: list[ReferenceDataSearchRsp.Airport] = field(
        default_factory=list,
        metadata={
            "name": "Airport",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    carrier: list[ReferenceDataSearchRsp.Carrier] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    city: list[ReferenceDataSearchRsp.City] = field(
        default_factory=list,
        metadata={
            "name": "City",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    country: list[ReferenceDataSearchRsp.Country] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    currency: list[ReferenceDataSearchRsp.Currency] = field(
        default_factory=list,
        metadata={
            "name": "Currency",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    equipment: list[ReferenceDataSearchRsp.Equipment] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    passenger_type: list[ReferenceDataSearchRsp.PassengerType] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    state: list[ReferenceDataSearchRsp.State] = field(
        default_factory=list,
        metadata={
            "name": "State",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ssr_type: list[ReferenceDataSearchRsp.SsrType] = field(
        default_factory=list,
        metadata={
            "name": "SsrType",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class Airport:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 3,
            }
        )
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )
        city_code: None | str = field(
            default=None,
            metadata={
                "name": "CityCode",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            }
        )
        country_code: None | str = field(
            default=None,
            metadata={
                "name": "CountryCode",
                "type": "Attribute",
                "length": 2,
            }
        )

    @dataclass
    class Carrier:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 2,
            }
        )
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )

    @dataclass
    class City:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 3,
                "white_space": "collapse",
            }
        )
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
                "required": True,
            }
        )
        state_code: None | str = field(
            default=None,
            metadata={
                "name": "StateCode",
                "type": "Attribute",
            }
        )
        country_code: None | str = field(
            default=None,
            metadata={
                "name": "CountryCode",
                "type": "Attribute",
                "length": 2,
            }
        )

    @dataclass
    class Country:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 2,
            }
        )
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )
        extended_code: None | str = field(
            default=None,
            metadata={
                "name": "ExtendedCode",
                "type": "Attribute",
            }
        )
        currency_code: None | str = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Attribute",
            }
        )
        iata_code: None | str = field(
            default=None,
            metadata={
                "name": "IataCode",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            }
        )
        continent: None | str = field(
            default=None,
            metadata={
                "name": "Continent",
                "type": "Attribute",
            }
        )

    @dataclass
    class Currency:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "length": 3,
            }
        )
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
                "required": True,
            }
        )
        decimal: None | str = field(
            default=None,
            metadata={
                "name": "Decimal",
                "type": "Attribute",
            }
        )

    @dataclass
    class Equipment:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
            }
        )
        description: None | str = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Attribute",
            }
        )

    @dataclass
    class PassengerType:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "min_length": 3,
                "max_length": 5,
            }
        )
        description: None | str = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class State:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "max_length": 6,
            }
        )
        name: None | str = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Attribute",
            }
        )
        country_code: None | str = field(
            default=None,
            metadata={
                "name": "CountryCode",
                "type": "Attribute",
                "required": True,
                "length": 2,
            }
        )

    @dataclass
    class SsrType:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
            }
        )
        description: None | str = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Attribute",
                "required": True,
            }
        )
        providers: None | str = field(
            default=None,
            metadata={
                "name": "Providers",
                "type": "Attribute",
            }
        )
        level: None | str = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Attribute",
                "required": True,
            }
        )
        free_text_required: None | str = field(
            default=None,
            metadata={
                "name": "FreeTextRequired",
                "type": "Attribute",
                "required": True,
            }
        )
        pattern: None | str = field(
            default=None,
            metadata={
                "name": "Pattern",
                "type": "Attribute",
            }
        )
        help_text: None | str = field(
            default=None,
            metadata={
                "name": "HelpText",
                "type": "Attribute",
            }
        )
