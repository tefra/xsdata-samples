from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .account_status_type_enumeration import AccountStatusTypeEnumeration
from .customer_account_status_ref import CustomerAccountStatusRef
from .customer_payment_means_ref import CustomerPaymentMeansRef
from .customer_payment_means_rel_structure import (
    CustomerPaymentMeansRelStructure,
)
from .customer_purchase_package_refs_rel_structure import (
    CustomerPurchasePackageRefsRelStructure,
)
from .customer_ref import CustomerRef
from .entity_in_version_structure import DataManagedObjectStructure
from .fare_contracts_rel_structure import FareContractsRelStructure
from .medium_access_device_refs_rel_structure import (
    MediumAccessDeviceRefsRelStructure,
)
from .multilingual_string import MultilingualString
from .type_of_customer_account_ref import TypeOfCustomerAccountRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "CustomerAccount_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: CustomerRef | None = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_customer_account_ref: TypeOfCustomerAccountRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_status_ref: CustomerAccountStatusRef | None = field(
        default=None,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_status_type: AccountStatusTypeEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "CustomerAccountStatusType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    fare_contracts: FareContractsRelStructure | None = field(
        default=None,
        metadata={
            "name": "fareContracts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_packages: CustomerPurchasePackageRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "customerPurchasePackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_payment_means_ref: CustomerPaymentMeansRef | None = field(
        default=None,
        metadata={
            "name": "CustomerPaymentMeansRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_means: CustomerPaymentMeansRelStructure | None = field(
        default=None,
        metadata={
            "name": "paymentMeans",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medium_access_devices: MediumAccessDeviceRefsRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "mediumAccessDevices",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
