from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class EnettVan2:
    """
    Container for all eNett Van information.

    Parameters
    ----------
    min_percentage
        The minimum percentage that will be applied on the Total price and
        sent to enett,which will denote the minimum authorized amount
        approved by eNett.uApi will default this to zero for multi-use
        Van's.
    max_percentage
        The maximum percentage that will be applied on the Total price and
        sent to enett, which will denote the maximum authorized amount as
        approved by eNett. This value will be ignored and not used for
        Multi-Use VAN’s.
    expiry_days
        The number of days from the VAN generation date that the VAN will be
        active for, after which the VAN cannot be used.
    multi_use
        Acceptable values are true or false. If set to true it will denote
        that the VAN being requested is multi-use else it will indicate a
        single -use VAN.A Single use VAN can only be debited once while the
        multiple use VAN's can be debited multiple times subjected to the
        maximum value it has been authorized for. The default value will be
        TRUE to indicate a multi-use VAN is being issued.
    """

    class Meta:
        name = "EnettVan"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    min_percentage: None | int = field(
        default=None,
        metadata={
            "name": "MinPercentage",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 100,
        },
    )
    max_percentage: None | int = field(
        default=None,
        metadata={
            "name": "MaxPercentage",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 100,
        },
    )
    expiry_days: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "ExpiryDays",
            "type": "Attribute",
            "min_inclusive": XmlDuration("P1D"),
            "max_inclusive": XmlDuration("P366D"),
        },
    )
    multi_use: bool = field(
        default=True,
        metadata={
            "name": "MultiUse",
            "type": "Attribute",
        },
    )
