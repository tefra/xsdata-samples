from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_information_2 import AccountInformation2
from travelport.models.agency_information_2 import AgencyInformation2
from travelport.models.custom_profile_information_2 import (
    CustomProfileInformation2,
)
from travelport.models.policy_information_3 import PolicyInformation3
from travelport.models.shop_information_2 import ShopInformation2
from travelport.models.traveler_information_2 import TravelerInformation2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class FileFinishingInfo2:
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
        namespace = "http://www.travelport.com/schema/common_v32_0"

    shop_information: None | ShopInformation2 = field(
        default=None,
        metadata={
            "name": "ShopInformation",
            "type": "Element",
        },
    )
    policy_information: list[PolicyInformation3] = field(
        default_factory=list,
        metadata={
            "name": "PolicyInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    account_information: None | AccountInformation2 = field(
        default=None,
        metadata={
            "name": "AccountInformation",
            "type": "Element",
        },
    )
    agency_information: None | AgencyInformation2 = field(
        default=None,
        metadata={
            "name": "AgencyInformation",
            "type": "Element",
        },
    )
    traveler_information: list[TravelerInformation2] = field(
        default_factory=list,
        metadata={
            "name": "TravelerInformation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    custom_profile_information: None | CustomProfileInformation2 = field(
        default=None,
        metadata={
            "name": "CustomProfileInformation",
            "type": "Element",
        },
    )
