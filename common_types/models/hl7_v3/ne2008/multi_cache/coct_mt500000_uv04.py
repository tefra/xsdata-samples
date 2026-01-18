from __future__ import annotations

from dataclasses import dataclass, field

from ..core.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    Ii,
    Int,
    IvlTsExplicit,
    OnExplicit,
    PnExplicit,
    Tn,
    TsExplicit,
)
from ..core.voc import (
    ActClass,
    ActMood,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPertainsValue,
    ActRelationshipPosting,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    EntityClass,
    EntityClassOrganization,
    EntityDeterminer,
    NullFlavor,
    ParticipationType,
    RoleClassCoveredParty,
    RoleClassEmployee,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    RoleClassRootValue,
    XAccommodationRequestorRole,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
    XSuccReplPrev,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class CoctMt500000Uv04AccommodationCoverage:
    class Meta:
        name = "COCT_MT500000UV04.AccommodationCoverage"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    code: Cs = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.ACCM,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04CarrierOrganization:
    class Meta:
        name = "COCT_MT500000UV04.CarrierOrganization"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    name: Tn = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassOrganization = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04EmployerOrganization:
    class Meta:
        name = "COCT_MT500000UV04.EmployerOrganization"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    name: None | OnExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassOrganization = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04PolicyHolderOrganization:
    class Meta:
        name = "COCT_MT500000UV04.PolicyHolderOrganization"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    name: None | Tn = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    addr: None | AdExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassOrganization = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04CarrierRole:
    class Meta:
        name = "COCT_MT500000UV04.CarrierRole"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    id: Ii = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    underwriting_carrier_organization: (
        None | CoctMt500000Uv04CarrierOrganization
    ) = field(
        default=None,
        metadata={
            "name": "underwritingCarrierOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassMutualRelationship.UNDWRT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04Employment:
    class Meta:
        name = "COCT_MT500000UV04.Employment"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
        },
    )
    employer_organization: None | CoctMt500000Uv04EmployerOrganization = field(
        default=None,
        metadata={
            "name": "employerOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassEmployee = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04Limitation:
    class Meta:
        name = "COCT_MT500000UV04.Limitation"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    accommodation_coverage: None | CoctMt500000Uv04AccommodationCoverage = (
        field(
            metadata={
                "name": "accommodationCoverage",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            }
        )
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: (
        ActRelationshipConditional
        | ActRelationshipHasComponent
        | ActRelationshipOutcome
        | ActRelationshipCostTracking
        | ActRelationshipPosting
        | str
        | ActRelationshipHasSupport
        | ActRelationshipTemporallyPertains
        | ActRelationshipPertainsValue
        | ActRelationshipSequel
        | XActRelationshipDocument
        | XActRelationshipEntry
        | XActRelationshipEntryRelationship
        | XActRelationshipExternalReference
        | XActRelationshipPatientTransport
        | XActRelationshipPertinentInfo
        | XActRelationshipRelatedAuthorizations
        | XActReplaceOrRevise
        | XSuccReplPrev
    ) = field(
        init=False,
        default=ActRelationshipPertainsValue.LIMIT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04Author:
    class Meta:
        name = "COCT_MT500000UV04.Author"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    carrier_role: None | CoctMt500000Uv04CarrierRole = field(
        metadata={
            "name": "carrierRole",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.AUT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04PolicyHolderPerson:
    class Meta:
        name = "COCT_MT500000UV04.PolicyHolderPerson"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    name: PnExplicit = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    birth_time: None | TsExplicit = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_employment: list[CoctMt500000Uv04Employment] = field(
        default_factory=list,
        metadata={
            "name": "asEmployment",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.PSN,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04PolicyHolder:
    class Meta:
        name = "COCT_MT500000UV04.PolicyHolder"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    id: None | Ii = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    policy_holder_person: None | CoctMt500000Uv04PolicyHolderPerson = field(
        default=None,
        metadata={
            "name": "policyHolderPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    policy_holder_organization: (
        None | CoctMt500000Uv04PolicyHolderOrganization
    ) = field(
        default=None,
        metadata={
            "name": "policyHolderOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassMutualRelationship.POLHOLD,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04Holder:
    class Meta:
        name = "COCT_MT500000UV04.Holder"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    policy_holder: None | CoctMt500000Uv04PolicyHolder = field(
        metadata={
            "name": "policyHolder",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.HLD,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04PolicyOrAccount:
    class Meta:
        name = "COCT_MT500000UV04.PolicyOrAccount"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    holder: None | CoctMt500000Uv04Holder = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    author: None | CoctMt500000Uv04Author = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    limitation: None | CoctMt500000Uv04Limitation = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.COV,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04Beneficiary:
    class Meta:
        name = "COCT_MT500000UV04.Beneficiary"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    sequence_number: None | Int = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    policy_or_account: None | CoctMt500000Uv04PolicyOrAccount = field(
        metadata={
            "name": "policyOrAccount",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.BEN,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt500000Uv04CoveredParty:
    class Meta:
        name = "COCT_MT500000UV04.CoveredParty"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
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
    id: Ii = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    code: None | Cs = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    beneficiary_of: None | CoctMt500000Uv04Beneficiary = field(
        metadata={
            "name": "beneficiaryOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassCoveredParty = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
