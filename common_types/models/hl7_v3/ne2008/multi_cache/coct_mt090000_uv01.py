from dataclasses import dataclass, field
from typing import Optional, Union

from ..core.datatypes_base import (
    AdExplicit,
    Bl,
    Ce,
    Cs,
    EdExplicit,
    EnExplicit,
    Ii,
    IvlTsExplicit,
    Sc,
    TelExplicit,
)
from ..core.voc import (
    EntityClass,
    EntityClassDevice,
    EntityClassOrganization,
    EntityDeterminer,
    NullFlavor,
    RoleClassAssignedEntity,
    RoleClassLicensedEntity,
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
from .coct_mt070000_uv01 import CoctMt070000Uv01LocatedEntity
from .coct_mt150000_uv02 import CoctMt150000Uv02Organization
from .coct_mt150003_uv03 import CoctMt150003Uv03Organization

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt090000Uv01Group:
    class Meta:
        name = "COCT_MT090000UV01.Group"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    code: Ce | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    name: list[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: EdExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.RGRP,
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


@dataclass
class CoctMt090000Uv01LanguageCommunication:
    class Meta:
        name = "COCT_MT090000UV01.LanguageCommunication"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    language_code: Ce | None = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    mode_code: Ce | None = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    proficiency_level_code: Ce | None = field(
        default=None,
        metadata={
            "name": "proficiencyLevelCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    preference_ind: Bl | None = field(
        default=None,
        metadata={
            "name": "preferenceInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )


@dataclass
class CoctMt090000Uv01LicensedEntity:
    class Meta:
        name = "COCT_MT090000UV01.LicensedEntity"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    code: Ce | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    issuing_organization: CoctMt150003Uv03Organization | None = field(
        default=None,
        metadata={
            "name": "issuingOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassLicensedEntity | None = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoctMt090000Uv01RoleOther:
    class Meta:
        name = "COCT_MT090000UV01.RoleOther"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    scoping_organization: CoctMt150000Uv02Organization | None = field(
        default=None,
        metadata={
            "name": "scopingOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassMutualRelationship | RoleClassPassive | str | RoleClassOntological | RoleClassPartitive | RoleClassRootValue | None = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class CoctMt090000Uv01Member:
    class Meta:
        name = "COCT_MT090000UV01.Member"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    code: Ce | None = field(
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
    status_code: Cs | None = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    group: CoctMt090000Uv01Group | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassMutualRelationship | RoleClassPassive | str | RoleClassOntological | RoleClassPartitive | RoleClassRootValue | XAccommodationRequestorRole | XDocumentEntrySubject | XDocumentSubject | XInformationRecipientRole | XRoleClassAccommodationRequestor | XRoleClassCoverage | XRoleClassCoverageInvoice | XRoleClassCredentialedEntity | XRoleClassPayeePolicyRelationship = field(
        init=False,
        default=RoleClassPartitive.MBR,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class CoctMt090000Uv01Device:
    class Meta:
        name = "COCT_MT090000UV01.Device"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    manufacturer_model_name: Sc | None = field(
        default=None,
        metadata={
            "name": "manufacturerModelName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    software_name: Sc | None = field(
        default=None,
        metadata={
            "name": "softwareName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_licensed_entity: list[CoctMt090000Uv01LicensedEntity] = field(
        default_factory=list,
        metadata={
            "name": "asLicensedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_member: list[CoctMt090000Uv01Member] = field(
        default_factory=list,
        metadata={
            "name": "asMember",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_role_other: list[CoctMt090000Uv01RoleOther] = field(
        default_factory=list,
        metadata={
            "name": "asRoleOther",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_located_entity: CoctMt070000Uv01LocatedEntity | None = field(
        default=None,
        metadata={
            "name": "asLocatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    language_communication: list[CoctMt090000Uv01LanguageCommunication] = (
        field(
            default_factory=list,
            metadata={
                "name": "languageCommunication",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassDevice | None = field(
        default=None,
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


@dataclass
class CoctMt090000Uv01Organization:
    class Meta:
        name = "COCT_MT090000UV01.Organization"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    name: list[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_licensed_entity: list[CoctMt090000Uv01LicensedEntity] = field(
        default_factory=list,
        metadata={
            "name": "asLicensedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_member: list[CoctMt090000Uv01Member] = field(
        default_factory=list,
        metadata={
            "name": "asMember",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_role_other: list[CoctMt090000Uv01RoleOther] = field(
        default_factory=list,
        metadata={
            "name": "asRoleOther",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_located_entity: CoctMt070000Uv01LocatedEntity | None = field(
        default=None,
        metadata={
            "name": "asLocatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    language_communication: list[CoctMt090000Uv01LanguageCommunication] = (
        field(
            default_factory=list,
            metadata={
                "name": "languageCommunication",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassOrganization | None = field(
        default=None,
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


@dataclass
class CoctMt090000Uv01Person:
    class Meta:
        name = "COCT_MT090000UV01.Person"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    name: list[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    as_licensed_entity: list[CoctMt090000Uv01LicensedEntity] = field(
        default_factory=list,
        metadata={
            "name": "asLicensedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_member: list[CoctMt090000Uv01Member] = field(
        default_factory=list,
        metadata={
            "name": "asMember",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_role_other: list[CoctMt090000Uv01RoleOther] = field(
        default_factory=list,
        metadata={
            "name": "asRoleOther",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_located_entity: CoctMt070000Uv01LocatedEntity | None = field(
        default=None,
        metadata={
            "name": "asLocatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    language_communication: list[CoctMt090000Uv01LanguageCommunication] = (
        field(
            default_factory=list,
            metadata={
                "name": "languageCommunication",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    null_flavor: NullFlavor | None = field(
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


@dataclass
class CoctMt090000Uv01AssignedEntity:
    class Meta:
        name = "COCT_MT090000UV01.AssignedEntity"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Ii | None = field(
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
    code: Ce | None = field(
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
    effective_time: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    certificate_text: EdExplicit | None = field(
        default=None,
        metadata={
            "name": "certificateText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_person: CoctMt090000Uv01Person | None = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    assigned_device: CoctMt090000Uv01Device | None = field(
        default=None,
        metadata={
            "name": "assignedDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    assigned_organization: CoctMt090000Uv01Organization | None = field(
        default=None,
        metadata={
            "name": "assignedOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    represented_organization: CoctMt150000Uv02Organization | None = field(
        default=None,
        metadata={
            "name": "representedOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: NullFlavor | None = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassAssignedEntity | None = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
