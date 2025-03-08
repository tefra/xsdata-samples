from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from sabre.models.cust_loyalty_type_share_market_ind import (
    CustLoyaltyTypeShareMarketInd,
)
from sabre.models.cust_loyalty_type_share_synch_ind import (
    CustLoyaltyTypeShareSynchInd,
)
from sabre.models.cust_loyalty_type_single_vendor_ind import (
    CustLoyaltyTypeSingleVendorInd,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class CustLoyaltyType:
    """
    Program rewarding frequent use by accumulating credits for services provided by
    vendors.

    Attributes:
        share_synch_ind:
        share_market_ind:
        program_id: Identifier to indicate the company owner of the
            loyalty program.
        membership_id: Unique identifier of the member in the program
            (membership number, account number, etc.).
        travel_sector: Identifies the travel sector. Refer to OTA Code
            List Travel Sector (TVS).
        loyal_level: Indicates special privileges in program assigned to
            individual.
        single_vendor_ind: Indicates if program is affiliated with a
            group of related offers accumulating credits.
        signup_date: Indicates when the member signed up for the loyalty
            program.
        effective_date: Indicates the starting date.
        expire_date: Indicates the ending date.
        rph: Reference place holder, to reference it back in the
            response.
    """

    share_synch_ind: None | CustLoyaltyTypeShareSynchInd = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        },
    )
    share_market_ind: None | CustLoyaltyTypeShareMarketInd = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        },
    )
    program_id: None | str = field(
        default=None,
        metadata={
            "name": "ProgramID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    membership_id: None | str = field(
        default=None,
        metadata={
            "name": "MembershipID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    travel_sector: None | str = field(
        default=None,
        metadata={
            "name": "TravelSector",
            "type": "Attribute",
        },
    )
    loyal_level: None | str = field(
        default=None,
        metadata={
            "name": "LoyalLevel",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    single_vendor_ind: None | CustLoyaltyTypeSingleVendorInd = field(
        default=None,
        metadata={
            "name": "SingleVendorInd",
            "type": "Attribute",
        },
    )
    signup_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "SignupDate",
            "type": "Attribute",
        },
    )
    effective_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        },
    )
    expire_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ExpireDate",
            "type": "Attribute",
        },
    )
    rph: None | str = field(
        default=None,
        metadata={
            "name": "RPH",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        },
    )
