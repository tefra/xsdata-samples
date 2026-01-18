from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ReissueInfoType:
    """
    Defines the data fields available for the reissue info type.
    """

    change_fees: None | ReissueInfoType.ChangeFees = field(
        default=None,
        metadata={
            "name": "ChangeFees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    residual_idicator: None | str = field(
        default=None,
        metadata={
            "name": "ResidualIdicator",
            "type": "Attribute",
        },
    )
    type_of_service_fee: None | str = field(
        default=None,
        metadata={
            "name": "TypeOfServiceFee",
            "type": "Attribute",
        },
    )
    type_of_reissue_transaction: None | str = field(
        default=None,
        metadata={
            "name": "TypeOfReissueTransaction",
            "type": "Attribute",
        },
    )
    reissue_result_from_tag: None | bool = field(
        default=None,
        metadata={
            "name": "ReissueResultFromTag",
            "type": "Attribute",
        },
    )
    form_of_refund: None | str = field(
        default=None,
        metadata={
            "name": "FormOfRefund",
            "type": "Attribute",
        },
    )
    reissue_requires_electronic_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "ReissueRequiresElectronicTicket",
            "type": "Attribute",
        },
    )
    reissue_does_not_allow_electronic_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "ReissueDoesNotAllowElectronicTicket",
            "type": "Attribute",
        },
    )
    tax_refundable: None | bool = field(
        default=None,
        metadata={
            "name": "TaxRefundable",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ChangeFees:
        change_fee: ReissueInfoType.ChangeFees.ChangeFee = field(
            metadata={
                "name": "ChangeFee",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "required": True,
            }
        )

        @dataclass(kw_only=True)
        class ChangeFee:
            """
            Attributes:
                highest_change_fee:
                amount:
                currency_code: A currency code (e.g. USD, EUR, PLN)
                decimal_places: Indicates the number of decimal places
                    for a particular currency. This is equivalent to the
                    ISO 4217 standard "minor unit".
                change_fee_waived:
                change_fee_not_applicable:
            """

            highest_change_fee: None | bool = field(
                default=None,
                metadata={
                    "name": "HighestChangeFee",
                    "type": "Attribute",
                },
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
            change_fee_waived: None | bool = field(
                default=None,
                metadata={
                    "name": "ChangeFeeWaived",
                    "type": "Attribute",
                },
            )
            change_fee_not_applicable: None | bool = field(
                default=None,
                metadata={
                    "name": "ChangeFeeNotApplicable",
                    "type": "Attribute",
                },
            )
