from dataclasses import dataclass, field
from typing import Optional

from ..core.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    TelExplicit,
)
from ..core.voc import (
    NullFlavor,
    RoleClassServiceDeliveryLocation,
)
from .coct_mt150003_uv03 import CoctMt150003Uv03Organization
from .coct_mt710000_uv01 import CoctMt710000Uv01Place

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt240003Uv02ServiceDeliveryLocation:
    class Meta:
        name = "COCT_MT240003UV02.ServiceDeliveryLocation"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    addr: list[AdExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    telecom: list[TelExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    location: Optional[CoctMt710000Uv01Place] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    service_provider_organization: Optional[CoctMt150003Uv03Organization] = (
        field(
            default=None,
            metadata={
                "name": "serviceProviderOrganization",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Optional[RoleClassServiceDeliveryLocation] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
