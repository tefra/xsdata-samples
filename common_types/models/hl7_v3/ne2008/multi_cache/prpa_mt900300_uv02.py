from __future__ import annotations

from dataclasses import dataclass, field

from ..core.datatypes_base import (
    Cd,
    Ce,
    Cs,
    Cv,
    Ii,
    Int,
    IvlTsExplicit,
    Sc,
    St,
)
from ..core.voc import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class PrpaMt900300Uv02CareEventId:
    class Meta:
        name = "PRPA_MT900300UV02.CareEventID"

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
    semantics_text: None | St = field(
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
class PrpaMt900300Uv02EncounterStatus:
    class Meta:
        name = "PRPA_MT900300UV02.EncounterStatus"

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
    value: list[Cv] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: None | St = field(
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
class PrpaMt900300Uv02EncounterTimeframe:
    class Meta:
        name = "PRPA_MT900300UV02.EncounterTimeframe"

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
    value: IvlTsExplicit = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    semantics_text: None | St = field(
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
class PrpaMt900300Uv02PatientId:
    class Meta:
        name = "PRPA_MT900300UV02.PatientId"

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
    semantics_text: None | St = field(
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
class PrpaMt900300Uv02ResponsibleOrganization:
    class Meta:
        name = "PRPA_MT900300UV02.ResponsibleOrganization"

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
    semantics_text: None | St = field(
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
class PrpaMt900300Uv02SortControl:
    class Meta:
        name = "PRPA_MT900300UV02.SortControl"

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
class PrpaMt900300Uv02TypeOfEncounter:
    class Meta:
        name = "PRPA_MT900300UV02.TypeOfEncounter"

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
    value: Cd = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    semantics_text: None | St = field(
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
class PrpaMt900300Uv02QueryByParameterPayload:
    class Meta:
        name = "PRPA_MT900300UV02.QueryByParameterPayload"

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
    query_id: None | Ii = field(
        default=None,
        metadata={
            "name": "queryId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
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
    care_event_id: None | PrpaMt900300Uv02CareEventId = field(
        default=None,
        metadata={
            "name": "careEventID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    encounter_status: None | PrpaMt900300Uv02EncounterStatus = field(
        default=None,
        metadata={
            "name": "encounterStatus",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    encounter_timeframe: None | PrpaMt900300Uv02EncounterTimeframe = field(
        default=None,
        metadata={
            "name": "encounterTimeframe",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    patient_id: PrpaMt900300Uv02PatientId = field(
        metadata={
            "name": "patientId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    responsible_organization: (
        None | PrpaMt900300Uv02ResponsibleOrganization
    ) = field(
        default=None,
        metadata={
            "name": "responsibleOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    sort_control: list[PrpaMt900300Uv02SortControl] = field(
        default_factory=list,
        metadata={
            "name": "sortControl",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    type_of_encounter: None | PrpaMt900300Uv02TypeOfEncounter = field(
        default=None,
        metadata={
            "name": "typeOfEncounter",
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
