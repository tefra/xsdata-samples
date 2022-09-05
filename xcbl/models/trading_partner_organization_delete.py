from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Agency,
    Identifier,
)


@dataclass(kw_only=True)
class PrimaryId:
    class Meta:
        name = "PrimaryID"

    agency: Agency = field(
        metadata={
            "name": "Agency",
            "type": "Element",
            "required": True,
        }
    )
    ident: str = field(
        metadata={
            "name": "Ident",
            "type": "Element",
            "required": True,
        }
    )
    short_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortID",
            "type": "Element",
        }
    )
    primary_idurn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryIDURN",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TradingPartnerId:
    class Meta:
        name = "TradingPartnerID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerId:
    class Meta:
        name = "ListOfTradingPartnerID"

    trading_partner_id: List[TradingPartnerId] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerID",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class Identifications:
    primary_id: Optional[PrimaryId] = field(
        default=None,
        metadata={
            "name": "PrimaryID",
            "type": "Element",
        }
    )
    list_of_trading_partner_id: Optional[ListOfTradingPartnerId] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TradingPartnerIdentifications:
    identifications: Identifications = field(
        metadata={
            "name": "Identifications",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationDeletion:
    trading_partner_identifications: TradingPartnerIdentifications = field(
        metadata={
            "name": "TradingPartnerIdentifications",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_display_name: str = field(
        metadata={
            "name": "TradingPartnerDisplayName",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerOrganizationDeletion:
    trading_partner_organization_deletion: List[TradingPartnerOrganizationDeletion] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerOrganizationDeletion",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationDelete:
    list_of_trading_partner_organization_deletion: ListOfTradingPartnerOrganizationDeletion = field(
        metadata={
            "name": "ListOfTradingPartnerOrganizationDeletion",
            "type": "Element",
            "required": True,
        }
    )
