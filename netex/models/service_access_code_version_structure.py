from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .travel_document_version_structure import TravelDocumentVersionStructure
from .vehicle_access_credentials_assignment_ref import (
    VehicleAccessCredentialsAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceAccessCodeVersionStructure(TravelDocumentVersionStructure):
    class Meta:
        name = "ServiceAccessCode_VersionStructure"

    access_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccessCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    expiry_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_access_credentials_assignment_ref: Optional[
        VehicleAccessCredentialsAssignmentRef
    ] = field(
        default=None,
        metadata={
            "name": "VehicleAccessCredentialsAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
