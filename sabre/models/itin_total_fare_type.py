from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from sabre.models.fare_type import FareType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ItinTotalFareType(FareType):
    """
    Attributes:
        extras: Air Extras total summary amount
        total_with_extras: Total price with Air Extras
        total_mileage:
        service_fee:
    """

    extras: None | ItinTotalFareType.Extras = field(
        default=None,
        metadata={
            "name": "Extras",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    total_with_extras: None | ItinTotalFareType.TotalWithExtras = field(
        default=None,
        metadata={
            "name": "TotalWithExtras",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    total_mileage: None | ItinTotalFareType.TotalMileage = field(
        default=None,
        metadata={
            "name": "TotalMileage",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    service_fee: None | ItinTotalFareType.ServiceFee = field(
        default=None,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )

    @dataclass(kw_only=True)
    class Extras:
        amount: object = field(
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TotalWithExtras:
        amount: object = field(
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TotalMileage:
        amount: object = field(
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ServiceFee:
        """
        Attributes:
            amount: Service Fee Amount
            tax_amount: Service Fee Tax
        """

        amount: Decimal = field(
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "required": True,
                "fraction_digits": 3,
            }
        )
        tax_amount: Decimal = field(
            metadata={
                "name": "TaxAmount",
                "type": "Attribute",
                "required": True,
                "fraction_digits": 3,
            }
        )
