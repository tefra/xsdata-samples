from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_information_3 import AccountInformation3
from travelport.models.agency_information_3 import AgencyInformation3
from travelport.models.custom_profile_information_3 import (
    CustomProfileInformation3,
)
from travelport.models.policy_information_4 import PolicyInformation4
from travelport.models.shop_information_3 import ShopInformation3
from travelport.models.traveler_information_3 import TravelerInformation3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class FileFinishingInfo3:
    """
    Misc Data required for File Finishing.

    This data is transient and not saved in database.

    Parameters
    ----------
    shop_information
    policy_information
        Policy Information required for File Finishing. Would repeat per
        Policy Type
    account_information
    agency_information
    traveler_information
    custom_profile_information
    """

    class Meta:
        name = "FileFinishingInfo"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    shop_information: None | ShopInformation3 = field(
        default=None,
        metadata={
            "name": "ShopInformation",
            "type": "Element",
        },
    )
    policy_information: list[PolicyInformation4] = field(
        default_factory=list,
        metadata={
            "name": "PolicyInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    account_information: None | AccountInformation3 = field(
        default=None,
        metadata={
            "name": "AccountInformation",
            "type": "Element",
        },
    )
    agency_information: None | AgencyInformation3 = field(
        default=None,
        metadata={
            "name": "AgencyInformation",
            "type": "Element",
        },
    )
    traveler_information: list[TravelerInformation3] = field(
        default_factory=list,
        metadata={
            "name": "TravelerInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    custom_profile_information: None | CustomProfileInformation3 = field(
        default=None,
        metadata={
            "name": "CustomProfileInformation",
            "type": "Element",
        },
    )
