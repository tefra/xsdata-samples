from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.tax_code_amount_type import TaxCodeAmountType
from sabre.models.tax_code_type import TaxCodeType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ExchangeTravelPreferencesTpaExtensionsType:
    """
    Attributes:
        exempt_all_taxes: Exempt all taxes (/TE)
        exempt_all_taxes_and_fees: Exempt all taxes and fees (/TN)
        taxes: Specify Taxes (/TX)
        exempt_tax: Exempt Tax (/TE)
        settlement_method:
    """

    class Meta:
        name = "ExchangeTravelPreferencesTPA_ExtensionsType"

    exempt_all_taxes: (
        None | ExchangeTravelPreferencesTpaExtensionsType.ExemptAllTaxes
    ) = field(
        default=None,
        metadata={
            "name": "ExemptAllTaxes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    exempt_all_taxes_and_fees: (
        None | ExchangeTravelPreferencesTpaExtensionsType.ExemptAllTaxesAndFees
    ) = field(
        default=None,
        metadata={
            "name": "ExemptAllTaxesAndFees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    taxes: None | ExchangeTravelPreferencesTpaExtensionsType.Taxes = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    exempt_tax: list[TaxCodeType] = field(
        default_factory=list,
        metadata={
            "name": "ExemptTax",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    settlement_method: None | str = field(
        default=None,
        metadata={
            "name": "SettlementMethod",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[a-zA-Z0-9]{3}",
        },
    )

    @dataclass(kw_only=True)
    class ExemptAllTaxes:
        value: bool = field(
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ExemptAllTaxesAndFees:
        value: bool = field(
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Taxes:
        """
        Attributes:
            tax: Specify tax amount and code.
        """

        tax: list[TaxCodeAmountType] = field(
            default_factory=list,
            metadata={
                "name": "Tax",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
