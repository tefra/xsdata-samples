from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class AirTaxType:
    """
    Defines the data fields available for air tax.

    Attributes:
        value:
        tax_code: Identifies the code for the tax.
        amount:
        currency_code: A currency code (e.g. USD, EUR, PLN)
        decimal_places: Indicates the number of decimal places for a
            particular currency. This is equivalent to the ISO 4217
            standard "minor unit".
        carrier_code: carrier used for this tax
        min_amount: Minumum tax amount
        max_amount: Maximum tax amount
        min_max_currency: Min/Max tax currency code
        rate_used: Tax rate used
        station_code: Airport code at which the tax or surcharge is
            being applied
        reissue_tax_type: Reissue tax type
        reissue_restriction_applies:
        reissue_tax_refundable:
        apply_to_reissue:
        reissue_max_amount:
        reissue_currency: Reissue tax max amount currency
        published_amount:
        published_currency:
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    tax_code: str = field(
        metadata={
            "name": "TaxCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        }
    )
    amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    currency_code: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    decimal_places: None | int = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        },
    )
    carrier_code: None | str = field(
        default=None,
        metadata={
            "name": "CarrierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    min_amount: None | float = field(
        default=None,
        metadata={
            "name": "MinAmount",
            "type": "Attribute",
        },
    )
    max_amount: None | float = field(
        default=None,
        metadata={
            "name": "MaxAmount",
            "type": "Attribute",
        },
    )
    min_max_currency: None | str = field(
        default=None,
        metadata={
            "name": "MinMaxCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    rate_used: None | float = field(
        default=None,
        metadata={
            "name": "RateUsed",
            "type": "Attribute",
        },
    )
    station_code: None | str = field(
        default=None,
        metadata={
            "name": "StationCode",
            "type": "Attribute",
        },
    )
    reissue_tax_type: None | str = field(
        default=None,
        metadata={
            "name": "ReissueTaxType",
            "type": "Attribute",
            "length": 1,
        },
    )
    reissue_restriction_applies: bool = field(
        default=False,
        metadata={
            "name": "ReissueRestrictionApplies",
            "type": "Attribute",
        },
    )
    reissue_tax_refundable: bool = field(
        default=False,
        metadata={
            "name": "ReissueTaxRefundable",
            "type": "Attribute",
        },
    )
    apply_to_reissue: bool = field(
        default=False,
        metadata={
            "name": "ApplyToReissue",
            "type": "Attribute",
        },
    )
    reissue_max_amount: None | float = field(
        default=None,
        metadata={
            "name": "ReissueMaxAmount",
            "type": "Attribute",
        },
    )
    reissue_currency: None | str = field(
        default=None,
        metadata={
            "name": "ReissueCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    published_amount: None | float = field(
        default=None,
        metadata={
            "name": "PublishedAmount",
            "type": "Attribute",
        },
    )
    published_currency: None | str = field(
        default=None,
        metadata={
            "name": "PublishedCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
