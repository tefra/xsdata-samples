from dataclasses import dataclass, field
from typing import Optional

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


@dataclass
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
    value: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: St | None = field(
        default=None,
        metadata={
            "name": "semanticsText",
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
    value: list[Cv] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: St | None = field(
        default=None,
        metadata={
            "name": "semanticsText",
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
    value: IvlTsExplicit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    semantics_text: St | None = field(
        default=None,
        metadata={
            "name": "semanticsText",
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
    value: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: St | None = field(
        default=None,
        metadata={
            "name": "semanticsText",
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
    value: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    semantics_text: St | None = field(
        default=None,
        metadata={
            "name": "semanticsText",
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
    sequence_number: Int | None = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    element_name: Sc | None = field(
        default=None,
        metadata={
            "name": "elementName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    direction_code: Cs | None = field(
        default=None,
        metadata={
            "name": "directionCode",
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
    value: Cd | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    semantics_text: St | None = field(
        default=None,
        metadata={
            "name": "semanticsText",
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
    query_id: Ii | None = field(
        default=None,
        metadata={
            "name": "queryId",
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
            "required": True,
        },
    )
    modify_code: Cs | None = field(
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
    response_modality_code: Cs | None = field(
        default=None,
        metadata={
            "name": "responseModalityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    response_priority_code: Cs | None = field(
        default=None,
        metadata={
            "name": "responsePriorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    initial_quantity: Int | None = field(
        default=None,
        metadata={
            "name": "initialQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    initial_quantity_code: Ce | None = field(
        default=None,
        metadata={
            "name": "initialQuantityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    care_event_id: PrpaMt900300Uv02CareEventId | None = field(
        default=None,
        metadata={
            "name": "careEventID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    encounter_status: PrpaMt900300Uv02EncounterStatus | None = field(
        default=None,
        metadata={
            "name": "encounterStatus",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    encounter_timeframe: PrpaMt900300Uv02EncounterTimeframe | None = field(
        default=None,
        metadata={
            "name": "encounterTimeframe",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    patient_id: PrpaMt900300Uv02PatientId | None = field(
        default=None,
        metadata={
            "name": "patientId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    responsible_organization: PrpaMt900300Uv02ResponsibleOrganization | None = field(
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
    type_of_encounter: PrpaMt900300Uv02TypeOfEncounter | None = field(
        default=None,
        metadata={
            "name": "typeOfEncounter",
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
