from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.email_type_share_market_ind import EmailTypeShareMarketInd
from sabre.models.email_type_share_synch_ind import EmailTypeShareSynchInd

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class EmailType:
    """
    Electronic email addresses, in IETF specified format.

    Attributes:
        value:
        share_synch_ind:
        share_market_ind:
        default_ind:
        email_type: Defines the purpose of the e-mail address (e.g.
            personal, business, listserve). Refer to OTA Code List Email
            Address Type (EAT).
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    share_synch_ind: None | EmailTypeShareSynchInd = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        },
    )
    share_market_ind: None | EmailTypeShareMarketInd = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        },
    )
    default_ind: bool = field(
        default=False,
        metadata={
            "name": "DefaultInd",
            "type": "Attribute",
        },
    )
    email_type: None | str = field(
        default=None,
        metadata={
            "name": "EmailType",
            "type": "Attribute",
        },
    )
