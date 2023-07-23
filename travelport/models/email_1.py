from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_reservation_info_ref_1 import ProviderReservationInfoRef1
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Email1:
    """
    Container for an email address with a type specifier (max 128 chars)

    Parameters
    ----------
    provider_reservation_info_ref
        Tagging provider reservation info with Email.
    key
    type_value
    comment
    email_id
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
        name = "Email"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    provider_reservation_info_ref: list[ProviderReservationInfoRef1] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    email_id: None | str = field(
        default=None,
        metadata={
            "name": "EmailID",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: None | TypeElementStatus1 = field(
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
