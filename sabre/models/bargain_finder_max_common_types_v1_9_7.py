from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class AirTripType(Enum):
    """Identifies the trip type - one way, return, circle trip, open jaw."""
    ONE_WAY = "OneWay"
    RETURN_VALUE = "Return"
    CIRCLE = "Circle"
    OPEN_JAW = "OpenJaw"
    OTHER = "Other"


@dataclass
class CompanyNameType:
    """
    Identifies a company by name.

    Attributes
        value:
        company_short_name:
        travel_sector: Refer to OTA Code List Travel Sector (TVS).
        code: Identifies a company by the company code.
        code_context: Identifies the context of the identifying code,
            such as DUNS, IATA or internal code, etc.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    company_short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyShortName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    travel_sector: Optional[str] = field(
        default=None,
        metadata={
            "name": "TravelSector",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    code_context: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeContext",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )


class DepartureOrArrival(Enum):
    DEPARTURE = "Departure"
    ARRIVAL = "Arrival"


@dataclass
class EquipmentType:
    """
    Specifies the aircraft equipment type.

    Attributes
        value:
        air_equip_type: This is the 3 character IATA code.
        changeof_gauge: Indicates there is an equipment change.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    air_equip_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirEquipType",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 3,
        }
    )
    changeof_gauge: bool = field(
        default=False,
        metadata={
            "name": "ChangeofGauge",
            "type": "Attribute",
        }
    )


class FareDirectionality(Enum):
    TO = "TO"
    FROM_VALUE = "FROM"


class MaximumStayReturnType(Enum):
    """
    Attributes
        C: Return travel must be Completed.
        S: Return travel must be Started.
    """
    C = "C"
    S = "S"


class OtaPayloadStdAttributesTarget(Enum):
    TEST = "Test"
    PRODUCTION = "Production"


class OtaPayloadStdAttributesTransactionStatusCode(Enum):
    """
    Attributes
        START: This is the first message within a transaction.
        END: This is the last message within a transaction.
        ROLLBACK: This indicates that all messages within the current
            transaction must be ignored.
        IN_SERIES: This is any message that is not the first or last
            message within a transaction.
    """
    START = "Start"
    END = "End"
    ROLLBACK = "Rollback"
    IN_SERIES = "InSeries"


class OutboundOrInbound(Enum):
    OUTBOUND = "Outbound"
    INBOUND = "Inbound"


class PenaltyApplication(Enum):
    AFTER = "After"
    BEFORE = "Before"


class PenaltyType1(Enum):
    REFUND = "Refund"
    EXCHANGE = "Exchange"


class StayUnitType(Enum):
    """
    Defines the 'Units' that can be applied to Stay restrictions.

    Attributes
        MINUTES:
        HOURS:
        DAYS:
        MONTHS:
        MON: Monday
        TUES: Tuesday
        WED: Wednesday
        THU: Thursday
        FRI: Friday
        SAT: Saturday
        SUN: Sunday
    """
    MINUTES = "Minutes"
    HOURS = "Hours"
    DAYS = "Days"
    MONTHS = "Months"
    MON = "MON"
    TUES = "TUES"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"


@dataclass
class TravelerCountType:
    """
    Defines the number of travelers of a specific type (e.g. a driver type can
    be either one of: Adult, YoungDriver, YoungerDriver, or it may be a code
    that is acceptable to both Trading Partners).

    Attributes
        age:
        code: Specify traveler type code.
        code_context: Identifies the source authority for the code.
        uri: Identifies the location of the code table
        quantity: Used to define a quantity of an associated element or
            attribute.
    """
    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    code_context: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeContext",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 999,
        }
    )


@dataclass
class VoluntaryChangesType:
    """
    Specifies charges and/or penalties associated with making ticket changes
    after purchase.

    Attributes
        penalty: Specifies penalty charges as either a currency amount
            or a percentage of the fare.
        vol_change_ind: Indicator used to specify whether voluntary
            change and other penalties are involved in the search or
            response.
    """
    penalty: Optional["VoluntaryChangesType.Penalty"] = field(
        default=None,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    vol_change_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VolChangeInd",
            "type": "Attribute",
        }
    )

    @dataclass
    class Penalty:
        """
        Attributes
            penalty_type: Indicates the type of penalty involved in the
                search or response.
            departure_status: Identifier used to indicate whether the
                change occurs before or after departure from the origin
                city.
            amount:
            currency_code: A currency code (e.g. USD, EUR, PLN)
            decimal_places: Indicates the number of decimal places for a
                particular currency. This is equivalent to the ISO 4217
                standard "minor unit".
            percent: The penalty charge conveyed as a percent of the
                total fare.
        """
        penalty_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "PenaltyType",
                "type": "Attribute",
            }
        )
        departure_status: Optional[str] = field(
            default=None,
            metadata={
                "name": "DepartureStatus",
                "type": "Attribute",
            }
        )
        amount: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "fraction_digits": 3,
            }
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Attribute",
                "pattern": r"[a-zA-Z]{3}",
            }
        )
        decimal_places: Optional[int] = field(
            default=None,
            metadata={
                "name": "DecimalPlaces",
                "type": "Attribute",
            }
        )
        percent: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Percent",
                "type": "Attribute",
                "min_inclusive": Decimal("0.01"),
                "max_inclusive": Decimal("100.00"),
            }
        )


class VoluntaryChangesMatch(Enum):
    """
    Attributes
        ALL: Conditions are joined by logical conjunction - fare needs
            to fulfill all the conditions to be returned in response.
        ANY: Conditions are joined by logical disjunction - fare needs
            to fulfill at least one of the conditions to be returned in
            response.
        INFO: Return penalty information
    """
    ALL = "All"
    ANY = "Any"
    INFO = "Info"


@dataclass
class AdvResTicketingType:
    """
    Container used to hold information regarding advance reservation and/or
    advance ticketing.

    Attributes
        adv_reservation: Specifies constraints on date of advance
            reservations.
        adv_ticketing: Specifies advance ticketing restrictions.
        adv_res_ind: Indicator for identifying whether or not advance
            reservation restrictions are involved in the request or
            response.
        adv_ticketing_ind: Indicator for identifying whether or not
            advance ticketing restrictions are involved in the request
            or response.
    """
    adv_reservation: Optional["AdvResTicketingType.AdvReservation"] = field(
        default=None,
        metadata={
            "name": "AdvReservation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    adv_ticketing: Optional["AdvResTicketingType.AdvTicketing"] = field(
        default=None,
        metadata={
            "name": "AdvTicketing",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    adv_res_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvResInd",
            "type": "Attribute",
        }
    )
    adv_ticketing_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdvTicketingInd",
            "type": "Attribute",
        }
    )

    @dataclass
    class AdvReservation:
        """
        Attributes
            latest_time_of_day: The time of day by which reservations
                must be made on the last day that advance reservations
                can be made.
            latest_period: The amount of elapsed time or number of
                occurrences of a day of the week before departure needed
                to satisfy an advance reservation requirement.
            latest_unit: The unit of elapsed time or the day of the week
                to be applied to the LatestPeriod value.
        """
        latest_time_of_day: Optional[Union[str, XmlTime]] = field(
            default=None,
            metadata={
                "name": "LatestTimeOfDay",
                "type": "Attribute",
            }
        )
        latest_period: Optional[str] = field(
            default=None,
            metadata={
                "name": "LatestPeriod",
                "type": "Attribute",
                "pattern": r"[0-9]{1,3}",
            }
        )
        latest_unit: Optional[StayUnitType] = field(
            default=None,
            metadata={
                "name": "LatestUnit",
                "type": "Attribute",
            }
        )

    @dataclass
    class AdvTicketing:
        """
        Attributes
            from_res_time_of_day: The time of day after reservations are
                made by which a ticket must be purchased.
            from_res_period: A length of time expressed as either an
                amount of time or the number of occurrences of a day of
                the week after reservations are made that a ticket must
                be purchased.
            from_res_unit: The unit of elapsed time or the day of the
                week to be applied to the period after reservation are
                made that a ticket must be purchased.
            from_depart_time_of_day: The time of day prior to departure
                when the ticket must be purchased.
            from_depart_period: A length of time expressed as either an
                amount of time or the number of occurrences of a day of
                the week before departure that a ticket must be
                purchased.
            from_depart_unit: The unit of elapsed time or the day of the
                week to be applied to the the period before departure
                that a ticket must be purchased.
        """
        from_res_time_of_day: Optional[Union[str, XmlTime]] = field(
            default=None,
            metadata={
                "name": "FromResTimeOfDay",
                "type": "Attribute",
            }
        )
        from_res_period: Optional[str] = field(
            default=None,
            metadata={
                "name": "FromResPeriod",
                "type": "Attribute",
                "pattern": r"[0-9]{1,3}",
            }
        )
        from_res_unit: Optional[StayUnitType] = field(
            default=None,
            metadata={
                "name": "FromResUnit",
                "type": "Attribute",
            }
        )
        from_depart_time_of_day: Optional[Union[str, XmlTime]] = field(
            default=None,
            metadata={
                "name": "FromDepartTimeOfDay",
                "type": "Attribute",
            }
        )
        from_depart_period: Optional[str] = field(
            default=None,
            metadata={
                "name": "FromDepartPeriod",
                "type": "Attribute",
                "pattern": r"[0-9]{1,3}",
            }
        )
        from_depart_unit: Optional[StayUnitType] = field(
            default=None,
            metadata={
                "name": "FromDepartUnit",
                "type": "Attribute",
            }
        )


@dataclass
class PassengerTypeQuantityType(TravelerCountType):
    """Specifies a PTC (Passenger Type Code) and the associated number of PTC's - for use in specifying passenger lists.

    Attributes
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        changeable:
        index: Allows to identify which one of requested passengers this
            solution relates to.
    """
    tpa_extensions: Optional["PassengerTypeQuantityType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    changeable: bool = field(
        default=True,
        metadata={
            "name": "Changeable",
            "type": "Attribute",
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Attribute",
        }
    )

    @dataclass
    class TpaExtensions:
        """
        Attributes
            birth_date:
            age: Exchange-specific
            state: Exchange-specific
            total_number: Exchange-specific
            voluntary_changes: Identifies whether penalties associated
                with voluntary changes should be included in the search
                results.
        """
        birth_date: Optional["PassengerTypeQuantityType.TpaExtensions.BirthDate"] = field(
            default=None,
            metadata={
                "name": "BirthDate",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        age: Optional["PassengerTypeQuantityType.TpaExtensions.Age"] = field(
            default=None,
            metadata={
                "name": "Age",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        state: Optional["PassengerTypeQuantityType.TpaExtensions.State"] = field(
            default=None,
            metadata={
                "name": "State",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        total_number: Optional["PassengerTypeQuantityType.TpaExtensions.TotalNumber"] = field(
            default=None,
            metadata={
                "name": "TotalNumber",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        voluntary_changes: Optional["PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges"] = field(
            default=None,
            metadata={
                "name": "VoluntaryChanges",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class BirthDate:
            date: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "Date",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Age:
            years: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Years",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class State:
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class TotalNumber:
            value: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class VoluntaryChanges:
            """
            Specifies charges and/or penalties associated with making ticket
            changes after purchase.

            Attributes
                penalty: Specifies penalty charges as either a currency
                    amount or a percentage of the fare.
                match: Indicates relation between conditions.
            """
            penalty: List["PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges.Penalty"] = field(
                default_factory=list,
                metadata={
                    "name": "Penalty",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "max_occurs": 2,
                }
            )
            match: Optional[VoluntaryChangesMatch] = field(
                default=None,
                metadata={
                    "name": "Match",
                    "type": "Attribute",
                }
            )

            @dataclass
            class Penalty:
                """
                Attributes
                    type: Indicates the type (Refund or Exchange) of
                        penalty involved in the search or response.
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
                type: Optional[PenaltyType1] = field(
                    default=None,
                    metadata={
                        "name": "Type",
                        "type": "Attribute",
                    }
                )
                exclude: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "Exclude",
                        "type": "Attribute",
                    }
                )
                application: Optional[PenaltyApplication] = field(
                    default=None,
                    metadata={
                        "name": "Application",
                        "type": "Attribute",
                    }
                )
                amount: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "Amount",
                        "type": "Attribute",
                        "fraction_digits": 3,
                    }
                )
                currency_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CurrencyCode",
                        "type": "Attribute",
                        "pattern": r"[a-zA-Z]{3}",
                    }
                )
                decimal_places: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "DecimalPlaces",
                        "type": "Attribute",
                    }
                )


@dataclass
class StayRestrictionsType:
    """
    Type defining Min and Max Stay Restrictions.

    Attributes
        minimum_stay: Specifies restrictions for the shortest
            length/period of time or earliest day return travel can
            commence or be completed.
        maximum_stay: Specifies restrictions for the  longest
            length/period of time or last day to begin or complete the
            return.
        stay_restrictions_ind: True indicates that Stay Restrictions
            exist.
    """
    minimum_stay: Optional["StayRestrictionsType.MinimumStay"] = field(
        default=None,
        metadata={
            "name": "MinimumStay",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    maximum_stay: Optional["StayRestrictionsType.MaximumStay"] = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    stay_restrictions_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StayRestrictionsInd",
            "type": "Attribute",
        }
    )

    @dataclass
    class MinimumStay:
        """
        Attributes
            return_time_of_day: The time of day when return travel may
                commence.
            min_stay: The amount of elapsed time or number of
                occurrences of a day of the week needed to satisfy a
                minimum stay requirement.
            stay_unit: The unit of elapsed time or the day of the week
                applied to the MinStay value.
            min_stay_date: The specific date for the minimum stay
                requirement.
        """
        return_time_of_day: Optional[Union[str, XmlTime]] = field(
            default=None,
            metadata={
                "name": "ReturnTimeOfDay",
                "type": "Attribute",
            }
        )
        min_stay: Optional[int] = field(
            default=None,
            metadata={
                "name": "MinStay",
                "type": "Attribute",
                "min_inclusive": 1,
                "max_inclusive": 99,
            }
        )
        stay_unit: Optional[StayUnitType] = field(
            default=None,
            metadata={
                "name": "StayUnit",
                "type": "Attribute",
            }
        )
        min_stay_date: Optional[Union[str, XmlTime]] = field(
            default=None,
            metadata={
                "name": "MinStayDate",
                "type": "Attribute",
            }
        )

    @dataclass
    class MaximumStay:
        """
        Attributes
            return_type: Code indicating whether travel must commence or
                be completed in order to satisfy the stay restriction.
            return_time_of_day: The time of day when return travel may
                commence.
            max_stay: The amount of elapsed time or number of
                occurrences of a day of the week that must occur to
                satisfy a maximum stay requirement.
            stay_unit: The unit of elapsed time or the day of the week
                applied to the MaxStay value.
            max_stay_date: The specific date for the maximum stay
                requirement.
        """
        return_type: Optional[MaximumStayReturnType] = field(
            default=None,
            metadata={
                "name": "ReturnType",
                "type": "Attribute",
            }
        )
        return_time_of_day: Optional[Union[str, XmlTime]] = field(
            default=None,
            metadata={
                "name": "ReturnTimeOfDay",
                "type": "Attribute",
            }
        )
        max_stay: Optional[int] = field(
            default=None,
            metadata={
                "name": "MaxStay",
                "type": "Attribute",
                "min_inclusive": 1,
                "max_inclusive": 99,
            }
        )
        stay_unit: Optional[StayUnitType] = field(
            default=None,
            metadata={
                "name": "StayUnit",
                "type": "Attribute",
            }
        )
        max_stay_date: Optional[Union[str, XmlTime]] = field(
            default=None,
            metadata={
                "name": "MaxStayDate",
                "type": "Attribute",
            }
        )
