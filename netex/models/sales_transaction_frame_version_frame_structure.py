from __future__ import annotations

from dataclasses import dataclass, field

from .blacklists_in_frame_rel_structure import BlacklistsInFrameRelStructure
from .common_version_frame_structure import CommonVersionFrameStructure
from .customer_accounts_in_frame_rel_structure import (
    CustomerAccountsInFrameRelStructure,
)
from .customer_purchase_packages_in_frame_rel_structure import (
    CustomerPurchasePackagesInFrameRelStructure,
)
from .customers_in_frame_rel_structure import CustomersInFrameRelStructure
from .fare_contracts_in_frame_rel_structure import (
    FareContractsInFrameRelStructure,
)
from .medium_access_devices_in_frame_rel_structure import (
    MediumAccessDevicesInFrameRelStructure,
)
from .retail_consortiums_in_frame_rel_structure import (
    RetailConsortiumsInFrameRelStructure,
)
from .retail_devices_in_frame_rel_structure import (
    RetailDevicesInFrameRelStructure,
)
from .sales_transactions_in_frame_rel_structure import (
    SalesTransactionsInFrameRelStructure,
)
from .travel_documents_in_frame_rel_structure import (
    TravelDocumentsInFrameRelStructure,
)
from .travel_specifications_in_frame_rel_structure import (
    TravelSpecificationsInFrameRelStructure,
)
from .types_of_travel_document_in_frame_rel_structure import (
    TypesOfTravelDocumentInFrameRelStructure,
)
from .whitelists_in_frame_rel_structure import WhitelistsInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesTransactionFrameVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "SalesTransactionFrame_VersionFrameStructure"

    retail_consortiums: None | RetailConsortiumsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "retailConsortiums",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_devices: None | RetailDevicesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "retailDevices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customers: None | CustomersInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_accounts: None | CustomerAccountsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "customerAccounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contracts: None | FareContractsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "fareContracts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medium_access_devices: None | MediumAccessDevicesInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "mediumAccessDevices",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    blacklists: None | BlacklistsInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    whitelists: None | WhitelistsInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specifications: None | TravelSpecificationsInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "travelSpecifications",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    sales_transactions: None | SalesTransactionsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "salesTransactions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types_of_travel_documents: (
        None | TypesOfTravelDocumentInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "typesOfTravelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_documents: None | TravelDocumentsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "travelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_packages: (
        None | CustomerPurchasePackagesInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "customerPurchasePackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
