from __future__ import annotations

from dataclasses import dataclass, field

from ..core.datatypes_base import (
    Cs,
    Ii,
    St,
    TsExplicit,
)
from ..core.voc import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PrpaMt201307Uv02DataSource:
    class Meta:
        name = "PRPA_MT201307UV02.DataSource"

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
            "required": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )


@dataclass
class PrpaMt201307Uv02PatientIdentifier:
    class Meta:
        name = "PRPA_MT201307UV02.PatientIdentifier"

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
            "required": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )


@dataclass
class PrpaMt201307Uv02ParameterList:
    class Meta:
        name = "PRPA_MT201307UV02.ParameterList"

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
    data_source: list[PrpaMt201307Uv02DataSource] = field(
        default_factory=list,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    patient_identifier: list[PrpaMt201307Uv02PatientIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "patientIdentifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )


@dataclass
class PrpaMt201307Uv02QueryByParameter:
    class Meta:
        name = "PRPA_MT201307UV02.QueryByParameter"

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
            "required": True,
        },
    )
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
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
    response_priority_code: None | Cs = field(
        default=None,
        metadata={
            "name": "responsePriorityCode",
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
    parameter_list: None | PrpaMt201307Uv02ParameterList = field(
        default=None,
        metadata={
            "name": "parameterList",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
