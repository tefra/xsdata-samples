from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


class AirTripType(Enum):
    """
    Identifies the trip type - one way, return, circle trip, open jaw.
    :cvar CIRCLE:
    :cvar ONE_WAY:
    :cvar OPEN_JAW:
    :cvar OTHER:
    :cvar RETURN_VALUE:
    """
    CIRCLE = "Circle"
    ONE_WAY = "OneWay"
    OPEN_JAW = "OpenJaw"
    OTHER = "Other"
    RETURN_VALUE = "Return"


@dataclass
class CompanyNameType:
    """Identifies a company by name.

    :ivar value:
    :ivar company_short_name:
    :ivar travel_sector: Refer to OTA Code List Travel Sector (TVS).
    :ivar code: Identifies a company by the company code.
    :ivar code_context: Identifies the context of the identifying code, such as DUNS, IATA or internal code, etc.
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    company_short_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CompanyShortName",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )
    travel_sector: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TravelSector",
            type="Attribute"
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    code_context: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CodeContext",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )


class DepartureOrArrival(Enum):
    """
    :cvar ARRIVAL:
    :cvar DEPARTURE:
    """
    ARRIVAL = "Arrival"
    DEPARTURE = "Departure"


@dataclass
class EquipmentType:
    """Specifies the aircraft equipment type.

    :ivar value:
    :ivar air_equip_type: This is the 3 character IATA code.
    :ivar changeof_gauge: Indicates there is an equipment change.
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    air_equip_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AirEquipType",
            type="Attribute",
            required=True,
            min_length=3.0,
            max_length=3.0
        )
    )
    changeof_gauge: bool = field(
        default=False,
        metadata=dict(
            name="ChangeofGauge",
            type="Attribute"
        )
    )


class FareDirectionality(Enum):
    """
    :cvar FROM_VALUE:
    :cvar TO:
    """
    FROM_VALUE = "FROM"
    TO = "TO"


class OutboundOrInbound(Enum):
    """
    :cvar INBOUND:
    :cvar OUTBOUND:
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class StayUnitType(Enum):
    """Defines the 'Units' that can be applied to Stay restrictions.

    :cvar DAYS:
    :cvar FRI: Friday
    :cvar HOURS:
    :cvar MON: Monday
    :cvar MINUTES:
    :cvar MONTHS:
    :cvar SAT: Saturday
    :cvar SUN: Sunday
    :cvar THU: Thursday
    :cvar TUES: Tuesday
    :cvar WED: Wednesday
    """
    DAYS = "Days"
    FRI = "FRI"
    HOURS = "Hours"
    MON = "MON"
    MINUTES = "Minutes"
    MONTHS = "Months"
    SAT = "SAT"
    SUN = "SUN"
    THU = "THU"
    TUES = "TUES"
    WED = "WED"


@dataclass
class TravelerCountType:
    """Defines the number of travelers of a specific type (e.g. a driver type can
    be either one of: Adult, YoungDriver, YoungerDriver, or it may be a code that
    is acceptable to both Trading Partners).

    :ivar age:
    :ivar code: Specify traveler type code.
    :ivar code_context: Identifies the source authority for the code.
    :ivar uri: Identifies the location of the code table
    :ivar quantity: Used to define a quantity of an associated element or attribute.
    """
    age: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute",
            min_inclusive=0.0,
            max_inclusive=999.0
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    code_context: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CodeContext",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    uri: Optional[str] = field(
        default=None,
        metadata=dict(
            name="URI",
            type="Attribute"
        )
    )
    quantity: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute",
            min_inclusive=1.0,
            max_inclusive=999.0
        )
    )


@dataclass
class VoluntaryChangesType:
    """Specifies charges and/or penalties associated with making ticket changes
    after purchase.

    :ivar penalty: Specifies penalty charges as either a currency amount or a percentage of the fare.
    :ivar vol_change_ind: Indicator used to specify whether voluntary change and other penalties are involved in the search or response.
    """
    penalty: Optional["VoluntaryChangesType.Penalty"] = field(
        default=None,
        metadata=dict(
            name="Penalty",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    vol_change_ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="VolChangeInd",
            type="Attribute"
        )
    )

    @dataclass
    class Penalty:
        """
        :ivar penalty_type: Indicates the type of penalty involved in the search or response.
        :ivar departure_status: Identifier used to indicate whether the change occurs before or after departure from the origin city.
        :ivar amount:
        :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
        :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
        :ivar percent: The penalty charge conveyed as a percent of the total fare.
        """
        penalty_type: Optional[str] = field(
            default=None,
            metadata=dict(
                name="PenaltyType",
                type="Attribute"
            )
        )
        departure_status: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DepartureStatus",
                type="Attribute"
            )
        )
        amount: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                name="Amount",
                type="Attribute",
                fraction_digits=3
            )
        )
        currency_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="CurrencyCode",
                type="Attribute",
                pattern=r"[a-zA-Z]{3}"
            )
        )
        decimal_places: Optional[int] = field(
            default=None,
            metadata=dict(
                name="DecimalPlaces",
                type="Attribute"
            )
        )
        percent: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                name="Percent",
                type="Attribute",
                min_inclusive=0.01,
                max_inclusive=100.0
            )
        )


@dataclass
class AdvResTicketingType:
    """Container used to hold information regarding advance reservation and/or
    advance ticketing.

    :ivar adv_reservation: Specifies constraints on date of advance reservations.
    :ivar adv_ticketing: Specifies advance ticketing restrictions.
    :ivar adv_res_ind: Indicator for identifying whether or not advance reservation restrictions are involved in the request or response.
    :ivar adv_ticketing_ind: Indicator for identifying whether or not advance ticketing restrictions are involved in the request or response.
    """
    adv_reservation: Optional["AdvResTicketingType.AdvReservation"] = field(
        default=None,
        metadata=dict(
            name="AdvReservation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    adv_ticketing: Optional["AdvResTicketingType.AdvTicketing"] = field(
        default=None,
        metadata=dict(
            name="AdvTicketing",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    adv_res_ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvResInd",
            type="Attribute"
        )
    )
    adv_ticketing_ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AdvTicketingInd",
            type="Attribute"
        )
    )

    @dataclass
    class AdvReservation:
        """
        :ivar latest_time_of_day: The time of day by which reservations must be made on the last day that advance reservations can be made.
        :ivar latest_period: The amount of elapsed time or number of occurrences of a day of the week before departure needed to satisfy an advance reservation requirement.
        :ivar latest_unit: The unit of elapsed time or the day of the week to be applied to the LatestPeriod value.
        """
        latest_time_of_day: Optional[str] = field(
            default=None,
            metadata=dict(
                name="LatestTimeOfDay",
                type="Attribute"
            )
        )
        latest_period: Optional[str] = field(
            default=None,
            metadata=dict(
                name="LatestPeriod",
                type="Attribute",
                pattern=r"[0-9]{1,3}"
            )
        )
        latest_unit: Optional[StayUnitType] = field(
            default=None,
            metadata=dict(
                name="LatestUnit",
                type="Attribute"
            )
        )

    @dataclass
    class AdvTicketing:
        """
        :ivar from_res_time_of_day: The time of day after reservations are made by which a ticket must be purchased.
        :ivar from_res_period: A length of time expressed as either an amount of time or the number of occurrences of a day of the week after reservations are made that a ticket must be purchased.
        :ivar from_res_unit: The unit of elapsed time or the day of the week to be applied to the period after reservation are made that a ticket must be purchased.
        :ivar from_depart_time_of_day: The time of day prior to departure when the ticket must be purchased.
        :ivar from_depart_period: A length of time expressed as either an amount of time or the number of occurrences of a day of the week before departure that a ticket must be purchased.
        :ivar from_depart_unit: The unit of elapsed time or the day of the week to be applied to the the period before departure that a ticket must be purchased.
        """
        from_res_time_of_day: Optional[str] = field(
            default=None,
            metadata=dict(
                name="FromResTimeOfDay",
                type="Attribute"
            )
        )
        from_res_period: Optional[str] = field(
            default=None,
            metadata=dict(
                name="FromResPeriod",
                type="Attribute",
                pattern=r"[0-9]{1,3}"
            )
        )
        from_res_unit: Optional[StayUnitType] = field(
            default=None,
            metadata=dict(
                name="FromResUnit",
                type="Attribute"
            )
        )
        from_depart_time_of_day: Optional[str] = field(
            default=None,
            metadata=dict(
                name="FromDepartTimeOfDay",
                type="Attribute"
            )
        )
        from_depart_period: Optional[str] = field(
            default=None,
            metadata=dict(
                name="FromDepartPeriod",
                type="Attribute",
                pattern=r"[0-9]{1,3}"
            )
        )
        from_depart_unit: Optional[StayUnitType] = field(
            default=None,
            metadata=dict(
                name="FromDepartUnit",
                type="Attribute"
            )
        )


@dataclass
class PassengerTypeQuantityType(TravelerCountType):
    """
    Specifies a PTC (Passenger Type Code) and the associated number of PTC's - for use in specifying passenger lists.
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar changeable:
    :ivar index: Allows to identify which one of requested passengers this solution relates to.
    """
    tpa_extensions: Optional["PassengerTypeQuantityType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    changeable: bool = field(
        default=True,
        metadata=dict(
            name="Changeable",
            type="Attribute"
        )
    )
    index: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Index",
            type="Attribute"
        )
    )

    @dataclass
    class TpaExtensions:
        """
        :ivar birth_date:
        :ivar age: Exchange-specific
        :ivar state: Exchange-specific
        :ivar total_number: Exchange-specific
        :ivar voluntary_changes: Identifies whether penalties associated with voluntary changes should be included in the search results.
        """
        birth_date: Optional["PassengerTypeQuantityType.TpaExtensions.BirthDate"] = field(
            default=None,
            metadata=dict(
                name="BirthDate",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        age: Optional["PassengerTypeQuantityType.TpaExtensions.Age"] = field(
            default=None,
            metadata=dict(
                name="Age",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        state: Optional["PassengerTypeQuantityType.TpaExtensions.State"] = field(
            default=None,
            metadata=dict(
                name="State",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        total_number: Optional["PassengerTypeQuantityType.TpaExtensions.TotalNumber"] = field(
            default=None,
            metadata=dict(
                name="TotalNumber",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        voluntary_changes: Optional["PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges"] = field(
            default=None,
            metadata=dict(
                name="VoluntaryChanges",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class BirthDate:
            """
            :ivar date:
            """
            date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Date",
                    type="Attribute"
                )
            )

        @dataclass
        class Age:
            """
            :ivar years:
            """
            years: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Years",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class State:
            """
            :ivar code:
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class TotalNumber:
            """
            :ivar value:
            """
            value: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Value",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class VoluntaryChanges:
            """Specifies charges and/or penalties associated with making ticket changes
            after purchase.

            :ivar penalty: Specifies penalty charges as either a currency amount or a percentage of the fare.
            :ivar match: Indicates relation between conditions.
            """
            penalty: List["PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges.Penalty"] = field(
                default_factory=list,
                metadata=dict(
                    name="Penalty",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=2
                )
            )
            match: Optional["PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges.Match"] = field(
                default=None,
                metadata=dict(
                    name="Match",
                    type="Attribute"
                )
            )

            @dataclass
            class Penalty:
                """
                :ivar type: Indicates the type (Refund or Exchange) of penalty involved in the search or response.
                :ivar exclude: Indicate that specific penalty type should be excluded from the response.
                :ivar application: Identifier used to indicate whether the change occurs before or after departure from the origin city.
                :ivar amount:
                :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
                :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
                """
                type: Optional["PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges.Penalty.Type"] = field(
                    default=None,
                    metadata=dict(
                        name="Type",
                        type="Attribute"
                    )
                )
                exclude: Optional[bool] = field(
                    default=None,
                    metadata=dict(
                        name="Exclude",
                        type="Attribute"
                    )
                )
                application: Optional["PassengerTypeQuantityType.TpaExtensions.VoluntaryChanges.Penalty.Application"] = field(
                    default=None,
                    metadata=dict(
                        name="Application",
                        type="Attribute"
                    )
                )
                amount: Optional[Decimal] = field(
                    default=None,
                    metadata=dict(
                        name="Amount",
                        type="Attribute",
                        fraction_digits=3
                    )
                )
                currency_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="CurrencyCode",
                        type="Attribute",
                        pattern=r"[a-zA-Z]{3}"
                    )
                )
                decimal_places: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="DecimalPlaces",
                        type="Attribute"
                    )
                )

                class Type(Enum):
                    """
                    :cvar EXCHANGE:
                    :cvar REFUND:
                    """
                    EXCHANGE = "Exchange"
                    REFUND = "Refund"

                class Application(Enum):
                    """
                    :cvar AFTER:
                    :cvar BEFORE:
                    """
                    AFTER = "After"
                    BEFORE = "Before"

            class Match(Enum):
                """
                :cvar ALL: Conditions are joined by logical conjunction - fare needs to fulfill all the conditions to be returned in response.
                :cvar ANY: Conditions are joined by logical disjunction - fare needs to fulfill at least one of the conditions to be returned in response.
                :cvar INFO: Return penalty information
                """
                ALL = "All"
                ANY = "Any"
                INFO = "Info"


@dataclass
class StayRestrictionsType:
    """Type defining Min and Max Stay Restrictions.

    :ivar minimum_stay: Specifies restrictions for the shortest length/period of time or earliest day return travel can commence or be completed.
    :ivar maximum_stay: Specifies restrictions for the  longest length/period of time or last day to begin or complete the return.
    :ivar stay_restrictions_ind: True indicates that Stay Restrictions exist.
    """
    minimum_stay: Optional["StayRestrictionsType.MinimumStay"] = field(
        default=None,
        metadata=dict(
            name="MinimumStay",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    maximum_stay: Optional["StayRestrictionsType.MaximumStay"] = field(
        default=None,
        metadata=dict(
            name="MaximumStay",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    stay_restrictions_ind: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="StayRestrictionsInd",
            type="Attribute"
        )
    )

    @dataclass
    class MinimumStay:
        """
        :ivar return_time_of_day: The time of day when return travel may commence.
        :ivar min_stay: The amount of elapsed time or number of occurrences of a day of the week needed to satisfy a minimum stay requirement.
        :ivar stay_unit: The unit of elapsed time or the day of the week applied to the MinStay value.
        :ivar min_stay_date: The specific date for the minimum stay requirement.
        """
        return_time_of_day: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ReturnTimeOfDay",
                type="Attribute"
            )
        )
        min_stay: Optional[int] = field(
            default=None,
            metadata=dict(
                name="MinStay",
                type="Attribute",
                min_inclusive=1.0,
                max_inclusive=99.0
            )
        )
        stay_unit: Optional[StayUnitType] = field(
            default=None,
            metadata=dict(
                name="StayUnit",
                type="Attribute"
            )
        )
        min_stay_date: Optional[str] = field(
            default=None,
            metadata=dict(
                name="MinStayDate",
                type="Attribute"
            )
        )

    @dataclass
    class MaximumStay:
        """
        :ivar return_type: Code indicating whether travel must commence or be completed in order to satisfy the stay restriction.
        :ivar return_time_of_day: The time of day when return travel may commence.
        :ivar max_stay: The amount of elapsed time or number of occurrences of a day of the week that must occur to satisfy a maximum stay requirement.
        :ivar stay_unit: The unit of elapsed time or the day of the week applied to the MaxStay value.
        :ivar max_stay_date: The specific date for the maximum stay requirement.
        """
        return_type: Optional["StayRestrictionsType.MaximumStay.ReturnType"] = field(
            default=None,
            metadata=dict(
                name="ReturnType",
                type="Attribute"
            )
        )
        return_time_of_day: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ReturnTimeOfDay",
                type="Attribute"
            )
        )
        max_stay: Optional[int] = field(
            default=None,
            metadata=dict(
                name="MaxStay",
                type="Attribute",
                min_inclusive=1.0,
                max_inclusive=99.0
            )
        )
        stay_unit: Optional[StayUnitType] = field(
            default=None,
            metadata=dict(
                name="StayUnit",
                type="Attribute"
            )
        )
        max_stay_date: Optional[str] = field(
            default=None,
            metadata=dict(
                name="MaxStayDate",
                type="Attribute"
            )
        )

        class ReturnType(Enum):
            """
            :cvar C: Return travel must be Completed.
            :cvar S: Return travel must be Started.
            """
            C = "C"
            S = "S"