from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_7 import TypeElementStatus7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class CommissionRemark6:
    """Identifies the agency commision remarks.

    Specifically used for Worldspan.

    Parameters
    ----------
    provider_reservation_level
        Specify commission which is applicable to PNR level.
    passenger_type_level
        Specify commission which is applicable to per PTC level.
    key
        Key to be used for internal processing.
    provider_reservation_info_ref
        Provider reservation reference key.
    provider_code
        Contains the Provider Code of the provider for which this accounting
        remark is used
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "CommissionRemark"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    provider_reservation_level: (
        None | CommissionRemark6.ProviderReservationLevel
    ) = field(
        default=None,
        metadata={
            "name": "ProviderReservationLevel",
            "type": "Element",
        },
    )
    passenger_type_level: list[CommissionRemark6.PassengerTypeLevel] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTypeLevel",
            "type": "Element",
            "max_occurs": 4,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    el_stat: None | TypeElementStatus7 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )

    @dataclass
    class ProviderReservationLevel:
        """
        Parameters
        ----------
        amount
            The monetary amount of the commission.
        percentage
            The percent of the commission.
        commission_cap
            Commission cap for the Airline.
        """

        amount: None | str = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
            },
        )
        percentage: None | str = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
                "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
            },
        )
        commission_cap: None | str = field(
            default=None,
            metadata={
                "name": "CommissionCap",
                "type": "Attribute",
            },
        )

    @dataclass
    class PassengerTypeLevel:
        """
        Parameters
        ----------
        traveler_type
        amount
            The monetary amount of the commission.
        percentage
            The percent of the commission.
        commission_cap
            Commission cap for the Airline.
        """

        traveler_type: None | str = field(
            default=None,
            metadata={
                "name": "TravelerType",
                "type": "Attribute",
                "required": True,
                "min_length": 3,
                "max_length": 5,
            },
        )
        amount: None | str = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
            },
        )
        percentage: None | str = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
                "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
            },
        )
        commission_cap: None | str = field(
            default=None,
            metadata={
                "name": "CommissionCap",
                "type": "Attribute",
            },
        )
