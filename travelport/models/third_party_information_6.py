from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_element_status_7 import TypeElementStatus7
from travelport.models.type_general_reference_6 import TypeGeneralReference6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class ThirdPartyInformation6:
    """Third party supplier locator information.

    Specifically applicable for SDK booking.

    Parameters
    ----------
    segment_ref
        Air/Passive Segment Reference
    third_party_code
        Third party supplier code.
    third_party_locator_code
        Confirmation number for third party supplier.
    third_party_name
        Third party supplier name.
    provider_reservation_info_ref
        Provider Reservation  reference
    key
        Unique identifier of the third party supplier. Key can be used to
        modify or delete saved third party information.
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
        name = "ThirdPartyInformation"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    segment_ref: list[TypeGeneralReference6] = field(
        default_factory=list,
        metadata={
            "name": "SegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    third_party_code: None | str = field(
        default=None,
        metadata={
            "name": "ThirdPartyCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    third_party_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ThirdPartyLocatorCode",
            "type": "Attribute",
            "max_length": 36,
        }
    )
    third_party_name: None | str = field(
        default=None,
        metadata={
            "name": "ThirdPartyName",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    el_stat: None | TypeElementStatus7 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
