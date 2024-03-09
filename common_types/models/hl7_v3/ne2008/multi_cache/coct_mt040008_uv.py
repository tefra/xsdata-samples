from dataclasses import dataclass, field
from typing import List, Optional

from ..core.datatypes_base import (
    Ce,
    Cs,
    Ii,
    IvlTsExplicit,
)
from ..core.voc import (
    NullFlavor,
    RoleClassAgent,
)
from .coct_mt030207_uv import CoctMt030207UvPerson
from .coct_mt140007_uv import CoctMt140007UvDevice
from .coct_mt150007_uv import CoctMt150007UvOrganization

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt040008UvResponsible:
    class Meta:
        name = "COCT_MT040008UV.Responsible"

    realm_code: List[Cs] = field(
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
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
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
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    agent_organization: Optional[CoctMt150007UvOrganization] = field(
        default=None,
        metadata={
            "name": "agentOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    agent_person: Optional[CoctMt030207UvPerson] = field(
        default=None,
        metadata={
            "name": "agentPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    agent_device: Optional[CoctMt140007UvDevice] = field(
        default=None,
        metadata={
            "name": "agentDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    represented_organization: Optional[CoctMt150007UvOrganization] = field(
        default=None,
        metadata={
            "name": "representedOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    represented_person: Optional[CoctMt030207UvPerson] = field(
        default=None,
        metadata={
            "name": "representedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassAgent = field(
        default=RoleClassAgent.AGNT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
