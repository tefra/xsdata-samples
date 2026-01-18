from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class Amount:
    class Meta:
        name = "amount"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
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
    dollar_sign: None | object = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    currency_id: None | int = field(
        default=None,
        metadata={
            "name": "@currency-id",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Code:
    class Meta:
        name = "code"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
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
    dollar_sign: None | object = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: None | str = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: None | object = field(
        default=None,
        metadata={
            "name": "@list-name",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DataRef:
    class Meta:
        name = "data-ref"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ErrorCode:
    class Meta:
        name = "error-code"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dialect: None | object = field(
        default=None,
        metadata={
            "name": "@dialect",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FaultCause:
    class Meta:
        name = "fault-cause"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Metadata:
    class Meta:
        name = "metadata"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Quantity:
    class Meta:
        name = "quantity"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
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
    dollar_sign: None | object = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    unit_code: None | object = field(
        default=None,
        metadata={
            "name": "@unit-code",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ReferenceParameters:
    class Meta:
        name = "reference-parameters"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TypeCode:
    class Meta:
        name = "type-code"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
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
    dollar_sign: None | object = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: None | str = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: None | object = field(
        default=None,
        metadata={
            "name": "@list-name",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Failure:
    class Meta:
        name = "failure"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data_ref: None | DataRef = field(
        default=None,
        metadata={
            "name": "data-ref",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Originator:
    class Meta:
        name = "originator"

    address: None | object = field(
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
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Value:
    class Meta:
        name = "value"

    text: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    code: None | Code = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    amount: None | Amount = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quantity: None | Quantity = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    numeric: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    percent: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    indicator: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    duration: None | XmlDuration = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Failures:
    class Meta:
        name = "failures"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    failure: None | Failure = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Values:
    class Meta:
        name = "values"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: None | Value = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Characteristic:
    class Meta:
        name = "characteristic"

    name_text: None | object = field(
        default=None,
        metadata={
            "name": "name-text",
            "type": "Element",
        },
    )
    desc_text: None | object = field(
        default=None,
        metadata={
            "name": "desc-text",
            "type": "Element",
        },
    )
    type_code: None | TypeCode = field(
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
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Characteristics:
    class Meta:
        name = "characteristics"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    characteristic: None | Characteristic = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Properties:
    class Meta:
        name = "properties"

    ids: None | Ids = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name_text: None | NameText = field(
        default=None,
        metadata={
            "name": "name-text",
            "type": "Element",
        },
    )
    desc_text: None | DescText = field(
        default=None,
        metadata={
            "name": "desc-text",
            "type": "Element",
        },
    )
    type_code: None | TypeCode = field(
        default=None,
        metadata={
            "name": "type-code",
            "type": "Element",
        },
    )
    categories: None | Categories = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    status_code: None | StatusCode = field(
        default=None,
        metadata={
            "name": "status-code",
            "type": "Element",
        },
    )
    version_id: None | VersionId = field(
        default=None,
        metadata={
            "name": "version-id",
            "type": "Element",
        },
    )
    created_date_time: None | CreatedDateTime = field(
        default=None,
        metadata={
            "name": "created-date-time",
            "type": "Element",
        },
    )
    created_by_id: None | CreatedById = field(
        default=None,
        metadata={
            "name": "created-by-id",
            "type": "Element",
        },
    )
    last_modified_date_time: None | LastModifiedDateTime = field(
        default=None,
        metadata={
            "name": "last-modified-date-time",
            "type": "Element",
        },
    )
    last_modified_by_id: None | LastModifiedById = field(
        default=None,
        metadata={
            "name": "last-modified-by-id",
            "type": "Element",
        },
    )
    validity_period: None | ValidityPeriod = field(
        default=None,
        metadata={
            "name": "validity-period",
            "type": "Element",
        },
    )
    text: None | Text = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    code: None | Code = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    amount: None | Amount = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quantity: None | Quantity = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    numeric: None | Numeric = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    percent: None | Percent = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    indicator: None | Indicator = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    from_date_time: None | FromDateTime = field(
        default=None,
        metadata={
            "name": "from-date-time",
            "type": "Element",
        },
    )
    to_date_time: None | ToDateTime = field(
        default=None,
        metadata={
            "name": "to-date-time",
            "type": "Element",
        },
    )
    duration: None | Duration = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    time: None | Time = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date: None | Date = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    date_time: None | DateTime = field(
        default=None,
        metadata={
            "name": "date-time",
            "type": "Element",
        },
    )
    originator: None | Originator = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    error_code: None | ErrorCode = field(
        default=None,
        metadata={
            "name": "error-code",
            "type": "Element",
        },
    )
    description: None | Description = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fault_cause: None | FaultCause = field(
        default=None,
        metadata={
            "name": "fault-cause",
            "type": "Element",
        },
    )
    characteristics: None | Characteristics = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    failures: None | Failures = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    values: None | Values = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dollar_sign: None | Type = field(
        default=None,
        metadata={
            "name": "$",
            "type": "Element",
        },
    )
    list_agency_name: None | ListAgencyName = field(
        default=None,
        metadata={
            "name": "@list-agency-name",
            "type": "Element",
        },
    )
    list_name: None | ListName = field(
        default=None,
        metadata={
            "name": "@list-name",
            "type": "Element",
        },
    )
    address: None | Address = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reference_parameters: None | ReferenceParameters = field(
        default=None,
        metadata={
            "name": "reference-parameters",
            "type": "Element",
        },
    )
    metadata: None | Metadata = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scheme_name: None | SchemeName = field(
        default=None,
        metadata={
            "name": "@scheme-name",
            "type": "Element",
        },
    )
    scheme_agency_name: None | SchemeAgencyName = field(
        default=None,
        metadata={
            "name": "@scheme-agency-name",
            "type": "Element",
        },
    )
    unit_code: None | UnitCode = field(
        default=None,
        metadata={
            "name": "@unit-code",
            "type": "Element",
        },
    )
    currency_id: None | CurrencyId = field(
        default=None,
        metadata={
            "name": "@currency-id",
            "type": "Element",
        },
    )
    value_expression: None | ValueExpression = field(
        default=None,
        metadata={
            "name": "value-expression",
            "type": "Element",
        },
    )
    query_expression: None | QueryExpression = field(
        default=None,
        metadata={
            "name": "query-expression",
            "type": "Element",
        },
    )
    identification: None | Identification = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    criteria: None | Criteria = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data_ref: None | DataRef = field(
        default=None,
        metadata={
            "name": "data-ref",
            "type": "Element",
        },
    )
    failure: None | Failure = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: None | Value = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    characteristic: None | Characteristic = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    category_code: None | CategoryCode = field(
        default=None,
        metadata={
            "name": "category-code",
            "type": "Element",
        },
    )
    id: None | Id = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Categories:
    class Meta:
        name = "categories"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CategoryCode:
    class Meta:
        name = "category-code"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CreatedById:
    class Meta:
        name = "created-by-id"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Criteria:
    class Meta:
        name = "criteria"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Id:
    class Meta:
        name = "id"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Identification:
    class Meta:
        name = "identification"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Ids:
    class Meta:
        name = "ids"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LastModifiedById:
    class Meta:
        name = "last-modified-by-id"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class QueryExpression:
    class Meta:
        name = "query-expression"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class StatusCode:
    class Meta:
        name = "status-code"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ValidityPeriod:
    class Meta:
        name = "validity-period"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ValueExpression:
    class Meta:
        name = "value-expression"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class VersionId:
    class Meta:
        name = "version-id"

    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    properties: Properties = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    required: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
