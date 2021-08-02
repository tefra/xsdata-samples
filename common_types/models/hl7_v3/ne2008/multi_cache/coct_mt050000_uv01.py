from dataclasses import dataclass, field
from typing import List, Optional, Union
from ..core.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    IvlTsExplicit,
    TelExplicit,
)
from ..core.voc import (
    NullFlavor,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    RoleClassRootValue,
    XAccommodationRequestorRole,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
)
from .coct_mt030000_uv04 import (
    CoctMt030000Uv04NonPersonLivingSubject,
    CoctMt030000Uv04Person,
)
from .coct_mt150000_uv02 import CoctMt150000Uv02Organization

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt050000Uv01Patient:
    class Meta:
        name = "COCT_MT050000UV01.Patient"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    addr: List[AdExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    telecom: List[TelExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    confidentiality_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    very_important_person_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "veryImportantPersonCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    patient_person: Optional[CoctMt030000Uv04Person] = field(
        default=None,
        metadata={
            "name": "patientPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    patient_non_person_living_subject: Optional[CoctMt030000Uv04NonPersonLivingSubject] = field(
        default=None,
        metadata={
            "name": "patientNonPersonLivingSubject",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    provider_organization: Optional[CoctMt150000Uv02Organization] = field(
        default=None,
        metadata={
            "name": "providerOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, RoleClassRootValue, XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassMutualRelationship.PAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
