from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_information_6 import AccountInformation6
from travelport.models.agency_information_6 import AgencyInformation6
from travelport.models.custom_profile_information_6 import CustomProfileInformation6
from travelport.models.policy_information_7 import PolicyInformation7
from travelport.models.shop_information_6 import ShopInformation6
from travelport.models.traveler_information_6 import TravelerInformation6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class FileFinishingInfo6:
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
        namespace = "http://www.travelport.com/schema/common_v38_0"

    shop_information: None | ShopInformation6 = field(
        default=None,
        metadata={
            "name": "ShopInformation",
            "type": "Element",
        }
    )
    policy_information: list[PolicyInformation7] = field(
        default_factory=list,
        metadata={
            "name": "PolicyInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    account_information: None | AccountInformation6 = field(
        default=None,
        metadata={
            "name": "AccountInformation",
            "type": "Element",
        }
    )
    agency_information: None | AgencyInformation6 = field(
        default=None,
        metadata={
            "name": "AgencyInformation",
            "type": "Element",
        }
    )
    traveler_information: list[TravelerInformation6] = field(
        default_factory=list,
        metadata={
            "name": "TravelerInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    custom_profile_information: None | CustomProfileInformation6 = field(
        default=None,
        metadata={
            "name": "CustomProfileInformation",
            "type": "Element",
        }
    )
