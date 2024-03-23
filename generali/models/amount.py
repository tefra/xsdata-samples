from dataclasses import dataclass, field
from typing import List, Optional

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
from generali.models.mod import TypeType
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: Optional[object] = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    currency_id: Optional[int] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: Optional[object] = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: Optional[object] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class ErrorCode:
    class Meta:
        name = "error-code"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dialect: Optional[object] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Metadata:
    class Meta:
        name = "metadata"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Quantity:
    class Meta:
        name = "quantity"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: Optional[object] = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    unit_code: Optional[object] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TypeCode:
    class Meta:
        name = "type-code"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: Optional[object] = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: Optional[object] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data_ref: Optional[DataRef] = field(
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

    address: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reference_parameters: List[ReferenceParameters] = field(
        default_factory=list,
        metadata={
            "name": "reference-parameters",
            "type": "Element",
        },
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    text: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    code: Optional[Code] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    numeric: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    percent: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    indicator: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Failures:
    class Meta:
        name = "failures"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    failure: Optional[Failure] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Values:
    class Meta:
        name = "values"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Characteristic:
    class Meta:
        name = "characteristic"

    name_text: Optional[object] = field(
        default=None,
        metadata={
            "name": "name-text",
            "type": "Element",
        },
    )
    desc_text: Optional[object] = field(
        default=None,
        metadata={
            "name": "desc-text",
            "type": "Element",
        },
    )
    type_code: Optional[TypeCode] = field(
        default=None,
        metadata={
            "name": "type-code",
            "type": "Element",
        },
    )
    values: List[Values] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Characteristics:
    class Meta:
        name = "characteristics"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Optional["Properties"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    characteristic: Optional[Characteristic] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Properties:
    class Meta:
        name = "properties"

    ids: Optional["Ids"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name_text: Optional[NameText] = field(
        default=None,
        metadata={
            "name": "name-text",
            "type": "Element",
        },
    )
    desc_text: Optional[DescText] = field(
        default=None,
        metadata={
            "name": "desc-text",
            "type": "Element",
        },
    )
    type_code: Optional[TypeCode] = field(
        default=None,
        metadata={
            "name": "type-code",
            "type": "Element",
        },
    )
    categories: Optional["Categories"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    status_code: Optional["StatusCode"] = field(
        default=None,
        metadata={
            "name": "status-code",
            "type": "Element",
        },
    )
    version_id: Optional["VersionId"] = field(
        default=None,
        metadata={
            "name": "version-id",
            "type": "Element",
        },
    )
    created_date_time: Optional[CreatedDateTime] = field(
        default=None,
        metadata={
            "name": "created-date-time",
            "type": "Element",
        },
    )
    created_by_id: Optional["CreatedById"] = field(
        default=None,
        metadata={
            "name": "created-by-id",
            "type": "Element",
        },
    )
    last_modified_date_time: Optional[LastModifiedDateTime] = field(
        default=None,
        metadata={
            "name": "last-modified-date-time",
            "type": "Element",
        },
    )
    last_modified_by_id: Optional["LastModifiedById"] = field(
        default=None,
        metadata={
            "name": "last-modified-by-id",
            "type": "Element",
        },
    )
    validity_period: Optional["ValidityPeriod"] = field(
        default=None,
        metadata={
            "name": "validity-period",
            "type": "Element",
        },
    )
    text: Optional[Text] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    code: Optional[Code] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    numeric: Optional[Numeric] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    indicator: Optional[Indicator] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    from_date_time: Optional[FromDateTime] = field(
        default=None,
        metadata={
            "name": "from-date-time",
            "type": "Element",
        },
    )
    to_date_time: Optional[ToDateTime] = field(
        default=None,
        metadata={
            "name": "to-date-time",
            "type": "Element",
        },
    )
    duration: Optional[Duration] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time: Optional[Time] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date: Optional[Date] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date_time: Optional[DateTime] = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
        },
    )
    originator: Optional[Originator] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    error_code: Optional[ErrorCode] = field(
        default=None,
        metadata={
            "name": "error-code",
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fault_cause: Optional[FaultCause] = field(
        default=None,
        metadata={
            "name": "fault-cause",
            "type": "Element",
        },
    )
    characteristics: Optional[Characteristics] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    failures: Optional[Failures] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    values: Optional[Values] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: Optional[ListAgencyName] = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: Optional[ListName] = field(
        default=None,
        metadata={
            "name": "@list-name",
            "type": "Element",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reference_parameters: Optional[ReferenceParameters] = field(
        default=None,
        metadata={
            "name": "reference-parameters",
            "type": "Element",
        },
    )
    metadata: Optional[Metadata] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scheme_name: Optional[SchemeName] = field(
        default=None,
        metadata={
            "name": "@scheme-name",
            "type": "Element",
        },
    )
    scheme_agency_name: Optional[SchemeAgencyName] = field(
        default=None,
        metadata={
            "name": "@scheme-agency-name",
            "type": "Element",
        },
    )
    unit_code: Optional[UnitCode] = field(
        default=None,
        metadata={
            "name": "@unit-code",
            "type": "Element",
        },
    )
    currency_id: Optional[CurrencyId] = field(
        default=None,
        metadata={
            "name": "@currency-id",
            "type": "Element",
        },
    )
    value_expression: Optional["ValueExpression"] = field(
        default=None,
        metadata={
            "name": "value-expression",
            "type": "Element",
        },
    )
    query_expression: Optional["QueryExpression"] = field(
        default=None,
        metadata={
            "name": "query-expression",
            "type": "Element",
        },
    )
    identification: Optional["Identification"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    criteria: Optional["Criteria"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data_ref: Optional[DataRef] = field(
        default=None,
        metadata={
            "name": "data-ref",
            "type": "Element",
        },
    )
    failure: Optional[Failure] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    characteristic: Optional[Characteristic] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    category_code: Optional["CategoryCode"] = field(
        default=None,
        metadata={
            "name": "category-code",
            "type": "Element",
        },
    )
    id: Optional["Id"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Categories:
    class Meta:
        name = "categories"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Optional[Properties] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
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

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    required: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
