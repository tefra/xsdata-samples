from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.emdsummary import Emdsummary
from travelport.models.emdtraveler_info import EmdtravelerInfo
from travelport.models.payment_1 import Payment1
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class EmdsummaryInfo:
    """
    Container for EMD summary information.

    Supported providers are 1G/1V/1P.

    Parameters
    ----------
    emdsummary
        Summary information for EMDs conjuncted to each other.
    emdtraveler_info
        EMD traveler information.
    payment
        Payment charged to issue EMD.
    provider_reservation_info_ref
        A reference to the provider reservation with which the document is
        associated.Displayed when shown as part of UR.Not displayed in
        EMDRetrieveRsp
    key
        System generated Key
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
        name = "EMDSummaryInfo"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    emdsummary: list[Emdsummary] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummary",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    emdtraveler_info: None | EmdtravelerInfo = field(
        default=None,
        metadata={
            "name": "EMDTravelerInfo",
            "type": "Element",
            "required": True,
        },
    )
    payment: None | Payment1 = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
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
