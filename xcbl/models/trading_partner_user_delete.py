from dataclasses import dataclass, field
from typing import List
from xcbl.models.trading_partner_user_information import (
    TradingPartnerOrganizationReference,
    UserId,
)


@dataclass(kw_only=True)
class TradingPartnerUserDeletion:
    trading_partner_organization_reference: TradingPartnerOrganizationReference = field(
        metadata={
            "name": "TradingPartnerOrganizationReference",
            "type": "Element",
            "required": True,
        }
    )
    user_id: UserId = field(
        metadata={
            "name": "UserID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerUserDeletion:
    trading_partner_user_deletion: List[TradingPartnerUserDeletion] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerUserDeletion",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerUserDelete:
    list_of_trading_partner_user_deletion: ListOfTradingPartnerUserDeletion = field(
        metadata={
            "name": "ListOfTradingPartnerUserDeletion",
            "type": "Element",
            "required": True,
        }
    )
