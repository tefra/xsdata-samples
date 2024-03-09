from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import XmlDateTime
from .customer_account_ref import CustomerAccountRef
from .emv_card_ref import EmvCardRef
from .entity_in_version_structure import VersionedChildStructure
from .mobile_device_ref import MobileDeviceRef
from .multilingual_string import MultilingualString
from .payment_method_enumeration import PaymentMethodEnumeration
from .smartcard_ref import SmartcardRef
from .type_of_payment_method_ref import TypeOfPaymentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPaymentMeansVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "CustomerPaymentMeans_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medium_access_device_ref: Optional[
        Union[MobileDeviceRef, EmvCardRef, SmartcardRef]
    ] = field(
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
    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    last_verified_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastVerifiedDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
