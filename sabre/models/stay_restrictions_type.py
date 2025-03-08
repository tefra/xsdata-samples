from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from sabre.models.maximum_stay_return_type import MaximumStayReturnType
from sabre.models.stay_unit_type import StayUnitType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class StayRestrictionsType:
    """
    Type defining Min and Max Stay Restrictions.

    Attributes:
        minimum_stay: Specifies restrictions for the shortest
            length/period of time or earliest day return travel can
            commence or be completed.
        maximum_stay: Specifies restrictions for the  longest
            length/period of time or last day to begin or complete the
            return.
        stay_restrictions_ind: True indicates that Stay Restrictions
            exist.
    """

    minimum_stay: None | StayRestrictionsType.MinimumStay = field(
        default=None,
        metadata={
            "name": "MinimumStay",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    maximum_stay: None | StayRestrictionsType.MaximumStay = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    stay_restrictions_ind: None | bool = field(
        default=None,
        metadata={
            "name": "StayRestrictionsInd",
            "type": "Attribute",
        },
    )

    @dataclass
    class MinimumStay:
        """
        Attributes:
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

        return_time_of_day: None | str | XmlTime = field(
            default=None,
            metadata={
                "name": "ReturnTimeOfDay",
                "type": "Attribute",
            },
        )
        min_stay: None | int = field(
            default=None,
            metadata={
                "name": "MinStay",
                "type": "Attribute",
                "min_inclusive": 1,
                "max_inclusive": 99,
            },
        )
        stay_unit: None | StayUnitType = field(
            default=None,
            metadata={
                "name": "StayUnit",
                "type": "Attribute",
            },
        )
        min_stay_date: None | str | XmlTime = field(
            default=None,
            metadata={
                "name": "MinStayDate",
                "type": "Attribute",
            },
        )

    @dataclass
    class MaximumStay:
        """
        Attributes:
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

        return_type: None | MaximumStayReturnType = field(
            default=None,
            metadata={
                "name": "ReturnType",
                "type": "Attribute",
            },
        )
        return_time_of_day: None | str | XmlTime = field(
            default=None,
            metadata={
                "name": "ReturnTimeOfDay",
                "type": "Attribute",
            },
        )
        max_stay: None | int = field(
            default=None,
            metadata={
                "name": "MaxStay",
                "type": "Attribute",
                "min_inclusive": 1,
                "max_inclusive": 99,
            },
        )
        stay_unit: None | StayUnitType = field(
            default=None,
            metadata={
                "name": "StayUnit",
                "type": "Attribute",
            },
        )
        max_stay_date: None | str | XmlTime = field(
            default=None,
            metadata={
                "name": "MaxStayDate",
                "type": "Attribute",
            },
        )
