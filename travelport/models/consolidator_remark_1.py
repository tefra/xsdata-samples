from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.pseudo_city_code_1 import PseudoCityCode1
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class ConsolidatorRemark1:
    """
    Authorization remark for Consolidator access to a PNR .

    Contains PCC information created by retail agent to allow a
    consolidator to service their PNR. PROVIDER SUPPORTED: Worldspan.

    Parameters
    ----------
    pseudo_city_code
    key
        Key to be used for internal processing.
    provider_reservation_info_ref
        Provider reservation reference key.
    provider_code
        Contains the Provider Code of the provider for which this element is
        used
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
        name = "ConsolidatorRemark"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    pseudo_city_code: list[PseudoCityCode1] = field(
        default_factory=list,
        metadata={
            "name": "PseudoCityCode",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
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
    el_stat: None | TypeElementStatus1 = field(
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
