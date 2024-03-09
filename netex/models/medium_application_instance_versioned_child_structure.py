from dataclasses import dataclass, field
from typing import Optional, Union
from .customer_account_ref import CustomerAccountRef
from .emv_card_ref import EmvCardRef
from .entity_in_version_structure import VersionedChildStructure
from .mobile_device_ref import MobileDeviceRef
from .multilingual_string import MultilingualString
from .service_access_code_ref import ServiceAccessCodeRef
from .smartcard_ref import SmartcardRef
from .travel_document_ref import TravelDocumentRef
from .type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumApplicationInstanceVersionedChildStructure(
    VersionedChildStructure
):
    class Meta:
        name = "MediumApplicationInstance_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    identity_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityToken",
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
    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_document_ref: Optional[
        Union[ServiceAccessCodeRef, TravelDocumentRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceAccessCodeRef",
                    "type": ServiceAccessCodeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentRef",
                    "type": TravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
