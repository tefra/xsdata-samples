from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from sabre.models.stay_unit_type import StayUnitType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class AdvResTicketingType:
    """
    Container used to hold information regarding advance reservation and/or advance
    ticketing.

    Attributes:
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

    adv_reservation: None | AdvResTicketingType.AdvReservation = field(
        default=None,
        metadata={
            "name": "AdvReservation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    adv_ticketing: None | AdvResTicketingType.AdvTicketing = field(
        default=None,
        metadata={
            "name": "AdvTicketing",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    adv_res_ind: None | bool = field(
        default=None,
        metadata={
            "name": "AdvResInd",
            "type": "Attribute",
        },
    )
    adv_ticketing_ind: None | bool = field(
        default=None,
        metadata={
            "name": "AdvTicketingInd",
            "type": "Attribute",
        },
    )

    @dataclass
    class AdvReservation:
        """
        Attributes:
            latest_time_of_day: The time of day by which reservations
                must be made on the last day that advance reservations
                can be made.
            latest_period: The amount of elapsed time or number of
                occurrences of a day of the week before departure needed
                to satisfy an advance reservation requirement.
            latest_unit: The unit of elapsed time or the day of the week
                to be applied to the LatestPeriod value.
        """

        latest_time_of_day: None | str | XmlTime = field(
            default=None,
            metadata={
                "name": "LatestTimeOfDay",
                "type": "Attribute",
            },
        )
        latest_period: None | str = field(
            default=None,
            metadata={
                "name": "LatestPeriod",
                "type": "Attribute",
                "pattern": r"[0-9]{1,3}",
            },
        )
        latest_unit: None | StayUnitType = field(
            default=None,
            metadata={
                "name": "LatestUnit",
                "type": "Attribute",
            },
        )

    @dataclass
    class AdvTicketing:
        """
        Attributes:
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

        from_res_time_of_day: None | str | XmlTime = field(
            default=None,
            metadata={
                "name": "FromResTimeOfDay",
                "type": "Attribute",
            },
        )
        from_res_period: None | str = field(
            default=None,
            metadata={
                "name": "FromResPeriod",
                "type": "Attribute",
                "pattern": r"[0-9]{1,3}",
            },
        )
        from_res_unit: None | StayUnitType = field(
            default=None,
            metadata={
                "name": "FromResUnit",
                "type": "Attribute",
            },
        )
        from_depart_time_of_day: None | str | XmlTime = field(
            default=None,
            metadata={
                "name": "FromDepartTimeOfDay",
                "type": "Attribute",
            },
        )
        from_depart_period: None | str = field(
            default=None,
            metadata={
                "name": "FromDepartPeriod",
                "type": "Attribute",
                "pattern": r"[0-9]{1,3}",
            },
        )
        from_depart_unit: None | StayUnitType = field(
            default=None,
            metadata={
                "name": "FromDepartUnit",
                "type": "Attribute",
            },
        )
