from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.provider_reservation_info_ref_4 import ProviderReservationInfoRef4
from travelport.models.type_element_status_4 import TypeElementStatus4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class NameRemark3:
    """
    Text that support Name Remarks.

    Parameters
    ----------
    remark_data
        Actual remarks data.
    provider_reservation_info_ref
        Tagging provider reservation info with NameRemark.
    key
    category
        A category to group and organize the various remarks. This is not
        required, but it is recommended.
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
        name = "NameRemark"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    remark_data: None | str = field(
        default=None,
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "required": True,
        }
    )
    provider_reservation_info_ref: list[ProviderReservationInfoRef4] = field(
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
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        }
    )
    el_stat: None | TypeElementStatus4 = field(
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
