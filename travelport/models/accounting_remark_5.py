from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_6 import TypeElementStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class AccountingRemark5:
    """
    An accounting remark container to hold any printable text.

    Parameters
    ----------
    remark_data
        Actual remarks data.
    booking_traveler_ref
        Reference to Booking Traveler.
    key
    category
        A category to group and organize the various remarks. This is not
        required, but it is recommended.
    type_in_gds
    provider_reservation_info_ref
        Provider reservation reference key.
    provider_code
        Contains the Provider Code of the provider for which this accounting
        remark is used
    use_provider_native_mode
        Will be true when terminal process required, else false
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
        name = "AccountingRemark"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    remark_data: None | str = field(
        default=None,
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "required": True,
        },
    )
    booking_traveler_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "max_length": 14,
        },
    )
    type_in_gds: None | str = field(
        default=None,
        metadata={
            "name": "TypeInGds",
            "type": "Attribute",
            "max_length": 30,
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
    use_provider_native_mode: bool = field(
        default=False,
        metadata={
            "name": "UseProviderNativeMode",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus6 = field(
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
