from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_information_5 import AccountInformation5
from travelport.models.agency_information_5 import AgencyInformation5
from travelport.models.custom_profile_information_5 import (
    CustomProfileInformation5,
)
from travelport.models.policy_information_6 import PolicyInformation6
from travelport.models.shop_information_5 import ShopInformation5
from travelport.models.traveler_information_5 import TravelerInformation5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class FileFinishingInfo5:
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
        namespace = "http://www.travelport.com/schema/common_v34_0"

    shop_information: None | ShopInformation5 = field(
        default=None,
        metadata={
            "name": "ShopInformation",
            "type": "Element",
        },
    )
    policy_information: list[PolicyInformation6] = field(
        default_factory=list,
        metadata={
            "name": "PolicyInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    account_information: None | AccountInformation5 = field(
        default=None,
        metadata={
            "name": "AccountInformation",
            "type": "Element",
        },
    )
    agency_information: None | AgencyInformation5 = field(
        default=None,
        metadata={
            "name": "AgencyInformation",
            "type": "Element",
        },
    )
    traveler_information: list[TravelerInformation5] = field(
        default_factory=list,
        metadata={
            "name": "TravelerInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    custom_profile_information: None | CustomProfileInformation5 = field(
        default=None,
        metadata={
            "name": "CustomProfileInformation",
            "type": "Element",
        },
    )
