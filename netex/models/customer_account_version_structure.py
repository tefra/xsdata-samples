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

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_customer_account_ref: Optional[TypeOfCustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_status_ref: Optional[CustomerAccountStatusRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_status_type: Optional[AccountStatusTypeEnumeration] = (
        field(
            default=None,
            metadata={
                "name": "CustomerAccountStatusType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    fare_contracts: Optional[FareContractsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareContracts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_packages: Optional[
        CustomerPurchasePackageRefsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "customerPurchasePackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_payment_means_ref: Optional[CustomerPaymentMeansRef] = field(
        default=None,
        metadata={
            "name": "CustomerPaymentMeansRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_means: Optional[CustomerPaymentMeansRelStructure] = field(
        default=None,
        metadata={
            "name": "paymentMeans",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medium_access_devices: Optional[MediumAccessDeviceRefsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "mediumAccessDevices",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
