from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.trading_partner_organization_delete import Identifications


@dataclass
class UserId:
    class Meta:
        name = "UserID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    user_short_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserShortID",
            "type": "Attribute",
        }
    )


@dataclass
class TradingPartnerOrganizationReference:
    identifications: Optional[Identifications] = field(
        default=None,
        metadata={
            "name": "Identifications",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TradingPartnerUserDeletion:
    trading_partner_organization_reference: Optional[TradingPartnerOrganizationReference] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationReference",
            "type": "Element",
            "required": True,
        }
    )
    user_id: Optional[UserId] = field(
        default=None,
        metadata={
            "name": "UserID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfTradingPartnerUserDeletion:
    trading_partner_user_deletion: List[TradingPartnerUserDeletion] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerUserDeletion",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TradingPartnerUserDelete:
    list_of_trading_partner_user_deletion: Optional[ListOfTradingPartnerUserDeletion] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerUserDeletion",
            "type": "Element",
            "required": True,
        }
    )
