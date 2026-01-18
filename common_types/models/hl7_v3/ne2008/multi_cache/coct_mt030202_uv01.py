from dataclasses import dataclass, field
from typing import Optional, Union

from ..core.datatypes_base import (
    AdExplicit,
    Ce,
    Cs,
    EdExplicit,
    EnExplicit,
    Ii,
    St,
    TsExplicit,
)
from ..core.voc import (
    EntityClass,
    EntityClassPlace,
    EntityDeterminer,
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

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt030202Uv01Place:
    class Meta:
        name = "COCT_MT030202UV01.Place"

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
    addr: AdExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    directions_text: EdExplicit | None = field(
        default=None,
        metadata={
            "name": "directionsText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    position_text: EdExplicit | None = field(
        default=None,
        metadata={
            "name": "positionText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    gps_text: St | None = field(
        default=None,
        metadata={
            "name": "gpsText",
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
    class_code: EntityClassPlace | None = field(
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
class CoctMt030202Uv01Birthplace:
    class Meta:
        name = "COCT_MT030202UV01.Birthplace"

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
    birthplace: CoctMt030202Uv01Place | None = field(
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
        default=RoleClassPassive.BIRTHPL,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class CoctMt030202Uv01Person:
    class Meta:
        name = "COCT_MT030202UV01.Person"

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
    name: list[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    administrative_gender_code: Ce | None = field(
        default=None,
        metadata={
            "name": "administrativeGenderCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    birth_time: TsExplicit | None = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    birthplace: CoctMt030202Uv01Birthplace | None = field(
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
