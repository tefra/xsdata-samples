from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate

from sabre.models.penalty_application import PenaltyApplication
from sabre.models.penalty_type import PenaltyType
from sabre.models.traveler_count_type import TravelerCountType
from sabre.models.voluntary_changes_match import VoluntaryChangesMatch

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class PassengerTypeQuantityType(TravelerCountType):
    """
    Specifies a PTC (Passenger Type Code) and the associated number of
    PTC's - for use in specifying passenger lists.

    Attributes:
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        changeable:
        index: Allows to identify which one of requested passengers this
            solution relates to.
    """

    tpa_extensions: None | PassengerTypeQuantityType.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    changeable: bool = field(
        default=True,
        metadata={
            "name": "Changeable",
            "type": "Attribute",
        },
    )
    index: None | int = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class TpaExtensions:
        """
        Attributes:
            birth_date:
            age: Exchange-specific
            state: Exchange-specific
            total_number: Exchange-specific
            voluntary_changes: Identifies whether penalties associated
                with voluntary changes should be included in the search
                results.
        """

        birth_date: (
            None | PassengerTypeQuantityType.TpaExtensions.BirthDate
        ) = field(
            default=None,
            metadata={
                "name": "BirthDate",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        age: None | PassengerTypeQuantityType.TpaExtensions.Age = field(
            default=None,
            metadata={
                "name": "Age",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        state: None | PassengerTypeQuantityType.TpaExtensions.State = field(
            default=None,
            metadata={
                "name": "State",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        total_number: (
            None | PassengerTypeQuantityType.TpaExtensions.TotalNumber
        ) = field(
            default=None,
            metadata={
                "name": "TotalNumber",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        voluntary_changes: (
            None | PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges
        ) = field(
            default=None,
            metadata={
                "name": "VoluntaryChanges",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass(kw_only=True)
        class BirthDate:
            date: None | XmlDate = field(
                default=None,
                metadata={
                    "name": "Date",
                    "type": "Attribute",
                },
            )

        @dataclass(kw_only=True)
        class Age:
            years: int = field(
                metadata={
                    "name": "Years",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class State:
            code: str = field(
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class TotalNumber:
            value: int = field(
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class VoluntaryChanges:
            """
            Specifies charges and/or penalties associated with making
            ticket changes after purchase.

            Attributes:
                penalty: Specifies penalty charges as either a currency
                    amount or a percentage of the fare.
                match: Indicates relation between conditions.
            """

            penalty: list[
                PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges.Penalty
            ] = field(
                default_factory=list,
                metadata={
                    "name": "Penalty",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "max_occurs": 2,
                },
            )
            match: None | VoluntaryChangesMatch = field(
                default=None,
                metadata={
                    "name": "Match",
                    "type": "Attribute",
                },
            )

            @dataclass(kw_only=True)
            class Penalty:
                """
                Attributes:
                    type_value: Indicates the type (Refund or Exchange)
                        of penalty involved in the search or response.
                    exclude: Indicate that specific penalty type should
                        be excluded from the response.
                    application: Identifier used to indicate whether the
                        change occurs before or after departure from the
                        origin city.
                    amount:
                    currency_code: A currency code (e.g. USD, EUR, PLN)
                    decimal_places: Indicates the number of decimal
                        places for a particular currency. This is
                        equivalent to the ISO 4217 standard "minor
                        unit".
                """

                type_value: None | PenaltyType = field(
                    default=None,
                    metadata={
                        "name": "Type",
                        "type": "Attribute",
                    },
                )
                exclude: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Exclude",
                        "type": "Attribute",
                    },
                )
                application: None | PenaltyApplication = field(
                    default=None,
                    metadata={
                        "name": "Application",
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
