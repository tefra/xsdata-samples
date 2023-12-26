from dataclasses import dataclass, field
from typing import Optional
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

    retail_consortiums: Optional[RetailConsortiumsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "retailConsortiums",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_devices: Optional[RetailDevicesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "retailDevices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customers: Optional[CustomersInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_accounts: Optional[CustomerAccountsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "customerAccounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contracts: Optional[FareContractsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareContracts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blacklists: Optional[BlacklistsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    whitelists: Optional[WhitelistsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specifications: Optional[
        TravelSpecificationsInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "travelSpecifications",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_transactions: Optional[SalesTransactionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "salesTransactions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types_of_travel_documents: Optional[
        TypesOfTravelDocumentInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "typesOfTravelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_documents: Optional[TravelDocumentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "travelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_packages: Optional[
        CustomerPurchasePackagesInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
