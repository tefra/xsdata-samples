from dataclasses import dataclass, field
from typing import Optional
from .cell_versioned_child_structure import PriceableObjectVersionStructure
from .customer_account_ref import CustomerAccountRef
from .customer_purchase_package_elements_rel_structure import CustomerPurchasePackageElementsRelStructure
from .customer_purchase_package_prices_rel_structure import CustomerPurchasePackagePricesRelStructure
from .customer_purchase_package_status_enumeration import CustomerPurchasePackageStatusEnumeration
from .customer_purchase_parameter_assignments_rel_structure import CustomerPurchaseParameterAssignmentsRelStructure
from .customer_ref import CustomerRef
from .distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from .fare_contract_ref import FareContractRef
from .private_code import PrivateCode
from .sales_offer_package_ref import SalesOfferPackageRef
from .sales_transaction_ref import SalesTransactionRef
from .sales_transaction_refs_rel_structure import SalesTransactionRefsRelStructure
from .travel_documents_rel_structure import TravelDocumentsRelStructure
from .travel_specification_summary_view import TravelSpecificationSummaryView
from .travel_specifications_rel_structure import TravelSpecificationsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "CustomerPurchasePackage_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_ref: Optional[FareContractRef] = field(
        default=None,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_status: Optional[CustomerPurchasePackageStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specification_summary_view: Optional[TravelSpecificationSummaryView] = field(
        default=None,
        metadata={
            "name": "TravelSpecificationSummaryView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_specifications: Optional[TravelSpecificationsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelSpecifications",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignments: Optional[CustomerPurchaseParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_assignments: Optional[DistributionAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_elements: Optional[CustomerPurchasePackageElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction_ref: Optional[SalesTransactionRef] = field(
        default=None,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transactions: Optional[SalesTransactionRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "salesTransactions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[CustomerPurchasePackagePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_documents: Optional[TravelDocumentsRelStructure] = field(
        default=None,
        metadata={
            "name": "travelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
