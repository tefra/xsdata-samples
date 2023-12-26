from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_information_4 import AccountInformation4
from travelport.models.agency_information_4 import AgencyInformation4
from travelport.models.custom_profile_information_4 import (
    CustomProfileInformation4,
)
from travelport.models.policy_information_5 import PolicyInformation5
from travelport.models.shop_information_4 import ShopInformation4
from travelport.models.traveler_information_4 import TravelerInformation4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class FileFinishingInfo4:
    """Misc Data required for File Finishing.

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
        namespace = "http://www.travelport.com/schema/common_v37_0"

    shop_information: None | ShopInformation4 = field(
        default=None,
        metadata={
            "name": "ShopInformation",
            "type": "Element",
        },
    )
    policy_information: list[PolicyInformation5] = field(
        default_factory=list,
        metadata={
            "name": "PolicyInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    account_information: None | AccountInformation4 = field(
        default=None,
        metadata={
            "name": "AccountInformation",
            "type": "Element",
        },
    )
    agency_information: None | AgencyInformation4 = field(
        default=None,
        metadata={
            "name": "AgencyInformation",
            "type": "Element",
        },
    )
    traveler_information: list[TravelerInformation4] = field(
        default_factory=list,
        metadata={
            "name": "TravelerInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    custom_profile_information: None | CustomProfileInformation4 = field(
        default=None,
        metadata={
            "name": "CustomProfileInformation",
            "type": "Element",
        },
    )
