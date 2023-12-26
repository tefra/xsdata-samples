from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class Tax2:
    """
    Parameters
    ----------
    amount
    percentage
    code
        Code identifying fee (e.g. agency fee, bed tax etc.). Refer to OPEN
        Travel Code List for Fee Tax Type. Possible values are OTA Code
        against FTT.
    effective_date
    expiration_date
    term
        Indicates how the tax is applied. Values can be PerPerson, PerNight
        and PerStay
    collection_freq
        Indicates how often the tax is collected. Values can be Once or
        Daily
    """

    class Meta:
        name = "Tax"
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        },
    )
    percentage: None | float = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
        },
    )
    code: None | int = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        },
    )
    effective_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        },
    )
    expiration_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
        },
    )
    term: None | str = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Attribute",
        },
    )
    collection_freq: None | str = field(
        default=None,
        metadata={
            "name": "CollectionFreq",
            "type": "Attribute",
        },
    )
