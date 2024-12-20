from dataclasses import dataclass, field

from xcbl.models.trading_partner_organization_information import (
    TradingPartnerDisplayName,
    TradingPartnerIdentifications,
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
    trading_partner_display_name: TradingPartnerDisplayName = field(
        metadata={
            "name": "TradingPartnerDisplayName",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerOrganizationDeletion:
    trading_partner_organization_deletion: list[
        TradingPartnerOrganizationDeletion
    ] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerOrganizationDeletion",
            "type": "Element",
            "min_occurs": 1,
        },
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
