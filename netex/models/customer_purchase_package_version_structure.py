from __future__ import annotations

from dataclasses import dataclass, field

from .customer_account_ref import CustomerAccountRef
from .customer_purchase_package_elements_rel_structure import (
    CustomerPurchasePackageElementsRelStructure,
)
from .customer_purchase_package_prices_rel_structure import (
    CustomerPurchasePackagePricesRelStructure,
)
from .customer_purchase_package_status_enumeration import (
    CustomerPurchasePackageStatusEnumeration,
)
from .customer_purchase_parameter_assignments_rel_structure import (
    CustomerPurchaseParameterAssignmentsRelStructure,
)
from .customer_ref import CustomerRef
from .distribution_assignments_rel_structure import (
    DistributionAssignmentsRelStructure,
)
from .emv_card_ref import EmvCardRef
from .fare_contract_ref import FareContractRef
from .medium_application_instance_ref import MediumApplicationInstanceRef
from .mobile_device_ref import MobileDeviceRef
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .private_code import PrivateCode
from .sales_offer_package_ref import SalesOfferPackageRef
from .sales_transaction_ref import SalesTransactionRef
from .sales_transaction_refs_rel_structure import (
    SalesTransactionRefsRelStructure,
)
from .smartcard_ref import SmartcardRef
from .travel_documents_rel_structure import TravelDocumentsRelStructure
from .travel_specification_summary_view import TravelSpecificationSummaryView
from .travel_specifications_rel_structure import (
    TravelSpecificationsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "CustomerPurchasePackage_VersionStructure"

    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_offer_package_ref: None | SalesOfferPackageRef = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: None | CustomerRef = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_ref: None | CustomerAccountRef = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contract_ref: None | FareContractRef = field(
        default=None,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_package_status: (
        None | CustomerPurchasePackageStatusEnumeration
    ) = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specification_summary_view: (
        None | TravelSpecificationSummaryView
    ) = field(
        default=None,
        metadata={
            "name": "TravelSpecificationSummaryView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specifications: None | TravelSpecificationsRelStructure = field(
        default=None,
        metadata={
            "name": "travelSpecifications",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments: (
        None | CustomerPurchaseParameterAssignmentsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_assignments: None | DistributionAssignmentsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "distributionAssignments",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    customer_purchase_package_elements: (
        None | CustomerPurchasePackageElementsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "customerPurchasePackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_transaction_ref: None | SalesTransactionRef = field(
        default=None,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_transactions: None | SalesTransactionRefsRelStructure = field(
        default=None,
        metadata={
            "name": "salesTransactions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: None | CustomerPurchasePackagePricesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_documents: None | TravelDocumentsRelStructure = field(
        default=None,
        metadata={
            "name": "travelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medium_access_device_ref: (
        None | MobileDeviceRef | EmvCardRef | SmartcardRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobileDeviceRef",
                    "type": MobileDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EmvCardRef",
                    "type": EmvCardRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SmartcardRef",
                    "type": SmartcardRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    medium_application_instance_ref: None | MediumApplicationInstanceRef = (
        field(
            default=None,
            metadata={
                "name": "MediumApplicationInstanceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
