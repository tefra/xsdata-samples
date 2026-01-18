from __future__ import annotations

from dataclasses import dataclass, field

from ..core.datatypes_base import (
    AdExplicit,
    AnyType,
    Ce,
    Cs,
    Cv,
    EnExplicit,
    Ii,
    Int,
    IvlTsExplicit,
    PnExplicit,
    Sc,
    St,
    StExplicit,
    TelExplicit,
    TsExplicit,
)
from ..core.voc import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class PrpaMt201306Uv02LivingSubjectAdministrativeGender:
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectAdministrativeGender"

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
    value: list[Ce] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02LivingSubjectBirthPlaceAddress:
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectBirthPlaceAddress"

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
    value: list[AdExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02LivingSubjectBirthPlaceName:
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectBirthPlaceName"

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
    value: list[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02LivingSubjectBirthTime:
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectBirthTime"

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
    value: list[IvlTsExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02LivingSubjectDeceasedTime:
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectDeceasedTime"

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
    value: list[IvlTsExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: St = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02LivingSubjectId:
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectId"

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
    value: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02LivingSubjectName:
    class Meta:
        name = "PRPA_MT201306UV02.LivingSubjectName"

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
    value: list[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02MatchAlgorithm:
    class Meta:
        name = "PRPA_MT201306UV02.MatchAlgorithm"

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
    value: StExplicit = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02MatchWeight:
    class Meta:
        name = "PRPA_MT201306UV02.MatchWeight"

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
    value: AnyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    semantics_text: St = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02MinimumDegreeMatch:
    class Meta:
        name = "PRPA_MT201306UV02.MinimumDegreeMatch"

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
    value: Int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02MothersMaidenName:
    class Meta:
        name = "PRPA_MT201306UV02.MothersMaidenName"

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
    value: list[PnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02OtherIdsScopingOrganization:
    class Meta:
        name = "PRPA_MT201306UV02.OtherIDsScopingOrganization"

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
    value: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: St = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02PatientAddress:
    class Meta:
        name = "PRPA_MT201306UV02.PatientAddress"

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
    value: list[AdExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02PatientStatusCode:
    class Meta:
        name = "PRPA_MT201306UV02.PatientStatusCode"

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
    value: Cv = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    semantics_text: St = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02PatientTelecom:
    class Meta:
        name = "PRPA_MT201306UV02.PatientTelecom"

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
    value: list[TelExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02PrincipalCareProviderId:
    class Meta:
        name = "PRPA_MT201306UV02.PrincipalCareProviderId"

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
    value: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: None | StExplicit = field(
        default=None,
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02PrincipalCareProvisionId:
    class Meta:
        name = "PRPA_MT201306UV02.PrincipalCareProvisionId"

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
    value: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: StExplicit = field(
        metadata={
            "name": "semanticsText",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02SortControl:
    class Meta:
        name = "PRPA_MT201306UV02.SortControl"

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
    element_name: None | Sc = field(
        default=None,
        metadata={
            "name": "elementName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    direction_code: None | Cs = field(
        default=None,
        metadata={
            "name": "directionCode",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02MatchCriterionList:
    class Meta:
        name = "PRPA_MT201306UV02.MatchCriterionList"

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
    match_algorithm: None | PrpaMt201306Uv02MatchAlgorithm = field(
        default=None,
        metadata={
            "name": "matchAlgorithm",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    match_weight: None | PrpaMt201306Uv02MatchWeight = field(
        default=None,
        metadata={
            "name": "matchWeight",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    minimum_degree_match: None | PrpaMt201306Uv02MinimumDegreeMatch = field(
        default=None,
        metadata={
            "name": "minimumDegreeMatch",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02ParameterList:
    class Meta:
        name = "PRPA_MT201306UV02.ParameterList"

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
    living_subject_administrative_gender: list[
        PrpaMt201306Uv02LivingSubjectAdministrativeGender
    ] = field(
        default_factory=list,
        metadata={
            "name": "livingSubjectAdministrativeGender",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    living_subject_birth_place_address: list[
        PrpaMt201306Uv02LivingSubjectBirthPlaceAddress
    ] = field(
        default_factory=list,
        metadata={
            "name": "livingSubjectBirthPlaceAddress",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    living_subject_birth_place_name: list[
        PrpaMt201306Uv02LivingSubjectBirthPlaceName
    ] = field(
        default_factory=list,
        metadata={
            "name": "livingSubjectBirthPlaceName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    living_subject_birth_time: list[PrpaMt201306Uv02LivingSubjectBirthTime] = (
        field(
            default_factory=list,
            metadata={
                "name": "livingSubjectBirthTime",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "nillable": True,
            },
        )
    )
    living_subject_deceased_time: list[
        PrpaMt201306Uv02LivingSubjectDeceasedTime
    ] = field(
        default_factory=list,
        metadata={
            "name": "livingSubjectDeceasedTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    living_subject_id: list[PrpaMt201306Uv02LivingSubjectId] = field(
        default_factory=list,
        metadata={
            "name": "livingSubjectId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    living_subject_name: list[PrpaMt201306Uv02LivingSubjectName] = field(
        default_factory=list,
        metadata={
            "name": "livingSubjectName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    mothers_maiden_name: list[PrpaMt201306Uv02MothersMaidenName] = field(
        default_factory=list,
        metadata={
            "name": "mothersMaidenName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    other_ids_scoping_organization: list[
        PrpaMt201306Uv02OtherIdsScopingOrganization
    ] = field(
        default_factory=list,
        metadata={
            "name": "otherIDsScopingOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    patient_address: list[PrpaMt201306Uv02PatientAddress] = field(
        default_factory=list,
        metadata={
            "name": "patientAddress",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    patient_status_code: list[PrpaMt201306Uv02PatientStatusCode] = field(
        default_factory=list,
        metadata={
            "name": "patientStatusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    patient_telecom: list[PrpaMt201306Uv02PatientTelecom] = field(
        default_factory=list,
        metadata={
            "name": "patientTelecom",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    principal_care_provider_id: list[
        PrpaMt201306Uv02PrincipalCareProviderId
    ] = field(
        default_factory=list,
        metadata={
            "name": "principalCareProviderId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    principal_care_provision_id: list[
        PrpaMt201306Uv02PrincipalCareProvisionId
    ] = field(
        default_factory=list,
        metadata={
            "name": "principalCareProvisionId",
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


@dataclass(kw_only=True)
class PrpaMt201306Uv02QueryByParameter:
    class Meta:
        name = "PRPA_MT201306UV02.QueryByParameter"

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
    query_id: Ii = field(
        metadata={
            "name": "queryId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    status_code: Cs = field(
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    modify_code: None | Cs = field(
        default=None,
        metadata={
            "name": "modifyCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    response_element_group_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "responseElementGroupId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    response_modality_code: None | Cs = field(
        default=None,
        metadata={
            "name": "responseModalityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    response_priority_code: None | Cs = field(
        default=None,
        metadata={
            "name": "responsePriorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    initial_quantity: None | Int = field(
        default=None,
        metadata={
            "name": "initialQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    initial_quantity_code: None | Ce = field(
        default=None,
        metadata={
            "name": "initialQuantityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    execution_and_delivery_time: None | TsExplicit = field(
        default=None,
        metadata={
            "name": "executionAndDeliveryTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    match_criterion_list: None | PrpaMt201306Uv02MatchCriterionList = field(
        default=None,
        metadata={
            "name": "matchCriterionList",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    parameter_list: PrpaMt201306Uv02ParameterList = field(
        metadata={
            "name": "parameterList",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    sort_control: list[PrpaMt201306Uv02SortControl] = field(
        default_factory=list,
        metadata={
            "name": "sortControl",
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
