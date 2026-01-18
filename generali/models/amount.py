from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration

from generali.models.address import Address
from generali.models.created_date_time import CreatedDateTime
from generali.models.currency_id import CurrencyId
from generali.models.date import Date
from generali.models.date_time import DateTime
from generali.models.desc_text import DescText
from generali.models.description import Description
from generali.models.duration import Duration
from generali.models.from_date_time import FromDateTime
from generali.models.indicator import Indicator
from generali.models.last_modified_date_time import LastModifiedDateTime
from generali.models.list_agency_name import ListAgencyName
from generali.models.list_name import ListName
from generali.models.mod import Type
from generali.models.name_text import NameText
from generali.models.numeric import Numeric
from generali.models.percent import Percent
from generali.models.scheme_agency_name import SchemeAgencyName
from generali.models.scheme_name import SchemeName
from generali.models.text import Text
from generali.models.time import Time
from generali.models.to_date_time import ToDateTime
from generali.models.unit_code import UnitCode


@dataclass
class Amount:
    class Meta:
        name = "amount"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: object | None = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    currency_id: int | None = field(
        default=None,
        metadata={
            "name": "@currency-id",
            "type": "Element",
        },
    )


@dataclass
class Code:
    class Meta:
        name = "code"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: object | None = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: str | None = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: object | None = field(
        default=None,
        metadata={
            "name": "@list-name",
            "type": "Element",
        },
    )


@dataclass
class DataRef:
    class Meta:
        name = "data-ref"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ErrorCode:
    class Meta:
        name = "error-code"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dialect: object | None = field(
        default=None,
        metadata={
            "name": "@dialect",
            "type": "Element",
        },
    )


@dataclass
class FaultCause:
    class Meta:
        name = "fault-cause"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Metadata:
    class Meta:
        name = "metadata"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Quantity:
    class Meta:
        name = "quantity"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: object | None = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    unit_code: object | None = field(
        default=None,
        metadata={
            "name": "@unit-code",
            "type": "Element",
        },
    )


@dataclass
class ReferenceParameters:
    class Meta:
        name = "reference-parameters"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TypeCode:
    class Meta:
        name = "type-code"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: object | None = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: str | None = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: object | None = field(
        default=None,
        metadata={
            "name": "@list-name",
            "type": "Element",
        },
    )


@dataclass
class Failure:
    class Meta:
        name = "failure"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data_ref: DataRef | None = field(
        default=None,
        metadata={
            "name": "data-ref",
            "type": "Element",
        },
    )


@dataclass
class Originator:
    class Meta:
        name = "originator"

    address: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reference_parameters: list[ReferenceParameters] = field(
        default_factory=list,
        metadata={
            "name": "reference-parameters",
            "type": "Element",
        },
    )
    metadata: list[Metadata] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    text: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    code: Code | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    amount: Amount | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    numeric: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    percent: int | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    indicator: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    duration: XmlDuration | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date: XmlDate | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Failures:
    class Meta:
        name = "failures"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    failure: Failure | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Values:
    class Meta:
        name = "values"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: Value | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Characteristic:
    class Meta:
        name = "characteristic"

    name_text: object | None = field(
        default=None,
        metadata={
            "name": "name-text",
            "type": "Element",
        },
    )
    desc_text: object | None = field(
        default=None,
        metadata={
            "name": "desc-text",
            "type": "Element",
        },
    )
    type_code: TypeCode | None = field(
        default=None,
        metadata={
            "name": "type-code",
            "type": "Element",
        },
    )
    values: list[Values] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Characteristics:
    class Meta:
        name = "characteristics"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    characteristic: Characteristic | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Properties:
    class Meta:
        name = "properties"

    ids: Ids | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name_text: NameText | None = field(
        default=None,
        metadata={
            "name": "name-text",
            "type": "Element",
        },
    )
    desc_text: DescText | None = field(
        default=None,
        metadata={
            "name": "desc-text",
            "type": "Element",
        },
    )
    type_code: TypeCode | None = field(
        default=None,
        metadata={
            "name": "type-code",
            "type": "Element",
        },
    )
    categories: Categories | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    status_code: StatusCode | None = field(
        default=None,
        metadata={
            "name": "status-code",
            "type": "Element",
        },
    )
    version_id: VersionId | None = field(
        default=None,
        metadata={
            "name": "version-id",
            "type": "Element",
        },
    )
    created_date_time: CreatedDateTime | None = field(
        default=None,
        metadata={
            "name": "created-date-time",
            "type": "Element",
        },
    )
    created_by_id: CreatedById | None = field(
        default=None,
        metadata={
            "name": "created-by-id",
            "type": "Element",
        },
    )
    last_modified_date_time: LastModifiedDateTime | None = field(
        default=None,
        metadata={
            "name": "last-modified-date-time",
            "type": "Element",
        },
    )
    last_modified_by_id: LastModifiedById | None = field(
        default=None,
        metadata={
            "name": "last-modified-by-id",
            "type": "Element",
        },
    )
    validity_period: ValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "validity-period",
            "type": "Element",
        },
    )
    text: Text | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    code: Code | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    amount: Amount | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    numeric: Numeric | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    percent: Percent | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    indicator: Indicator | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    from_date_time: FromDateTime | None = field(
        default=None,
        metadata={
            "name": "from-date-time",
            "type": "Element",
        },
    )
    to_date_time: ToDateTime | None = field(
        default=None,
        metadata={
            "name": "to-date-time",
            "type": "Element",
        },
    )
    duration: Duration | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time: Time | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date: Date | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date_time: DateTime | None = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
        },
    )
    originator: Originator | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    error_code: ErrorCode | None = field(
        default=None,
        metadata={
            "name": "error-code",
            "type": "Element",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fault_cause: FaultCause | None = field(
        default=None,
        metadata={
            "name": "fault-cause",
            "type": "Element",
        },
    )
    characteristics: Characteristics | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    failures: Failures | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    values: Values | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: Type | None = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: ListAgencyName | None = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: ListName | None = field(
        default=None,
        metadata={
            "name": "@list-name",
            "type": "Element",
        },
    )
    address: Address | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reference_parameters: ReferenceParameters | None = field(
        default=None,
        metadata={
            "name": "reference-parameters",
            "type": "Element",
        },
    )
    metadata: Metadata | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scheme_name: SchemeName | None = field(
        default=None,
        metadata={
            "name": "@scheme-name",
            "type": "Element",
        },
    )
    scheme_agency_name: SchemeAgencyName | None = field(
        default=None,
        metadata={
            "name": "@scheme-agency-name",
            "type": "Element",
        },
    )
    unit_code: UnitCode | None = field(
        default=None,
        metadata={
            "name": "@unit-code",
            "type": "Element",
        },
    )
    currency_id: CurrencyId | None = field(
        default=None,
        metadata={
            "name": "@currency-id",
            "type": "Element",
        },
    )
    value_expression: ValueExpression | None = field(
        default=None,
        metadata={
            "name": "value-expression",
            "type": "Element",
        },
    )
    query_expression: QueryExpression | None = field(
        default=None,
        metadata={
            "name": "query-expression",
            "type": "Element",
        },
    )
    identification: Identification | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    criteria: Criteria | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data_ref: DataRef | None = field(
        default=None,
        metadata={
            "name": "data-ref",
            "type": "Element",
        },
    )
    failure: Failure | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: Value | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    characteristic: Characteristic | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    category_code: CategoryCode | None = field(
        default=None,
        metadata={
            "name": "category-code",
            "type": "Element",
        },
    )
    id: Id | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Categories:
    class Meta:
        name = "categories"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CategoryCode:
    class Meta:
        name = "category-code"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CreatedById:
    class Meta:
        name = "created-by-id"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Criteria:
    class Meta:
        name = "criteria"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Id:
    class Meta:
        name = "id"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Identification:
    class Meta:
        name = "identification"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Ids:
    class Meta:
        name = "ids"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LastModifiedById:
    class Meta:
        name = "last-modified-by-id"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class QueryExpression:
    class Meta:
        name = "query-expression"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StatusCode:
    class Meta:
        name = "status-code"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ValidityPeriod:
    class Meta:
        name = "validity-period"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class ValueExpression:
    class Meta:
        name = "value-expression"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class VersionId:
    class Meta:
        name = "version-id"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
