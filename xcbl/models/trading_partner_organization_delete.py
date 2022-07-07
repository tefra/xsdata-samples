from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Agency,
    Identifier,
)


@dataclass
class PrimaryId:
    class Meta:
        name = "PrimaryID"

    agency: Optional[Agency] = field(
        default=None,
        metadata={
            "name": "Agency",
            "type": "Element",
            "required": True,
        }
    )
    ident: Optional[str] = field(
        default=None,
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


@dataclass
class TradingPartnerId:
    class Meta:
        name = "TradingPartnerID"

    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
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


@dataclass
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


@dataclass
class TradingPartnerIdentifications:
    identifications: Optional[Identifications] = field(
        default=None,
        metadata={
            "name": "Identifications",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TradingPartnerOrganizationDeletion:
    trading_partner_identifications: Optional[TradingPartnerIdentifications] = field(
        default=None,
        metadata={
            "name": "TradingPartnerIdentifications",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerDisplayName",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfTradingPartnerOrganizationDeletion:
    trading_partner_organization_deletion: List[TradingPartnerOrganizationDeletion] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerOrganizationDeletion",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TradingPartnerOrganizationDelete:
    list_of_trading_partner_organization_deletion: Optional[ListOfTradingPartnerOrganizationDeletion] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerOrganizationDeletion",
            "type": "Element",
            "required": True,
        }
    )
