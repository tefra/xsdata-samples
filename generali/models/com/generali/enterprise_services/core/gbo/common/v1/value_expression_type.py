from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.query_operator_code_type import (
    QueryOperatorCodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class ValueExpressionType:
    """
    <description xmlns="">A component representing an expression of a query
    criteria used in a Get List.

    For example, find me the matching set of business objects where the
    Path Equals the Value. The Equals being the operator code, e.g. equals,
    less than, etc.</description>.

    :ivar value: <description xmlns="">The value to be matched in a
        query criteria. The repeating structure allows more than one
        value to be specified, these must be taken as an implict OR
        function, i.e. This Value-1 OR Value-2 OR Value-3.</description>
    :ivar operator_code: <description xmlns="">The value from the
        codelist representing the operator to apply between the Path and
        the Value. Examples include Equals, Less Than,
        etc.</description>
    :ivar path: <description xmlns="">The path to the field within the
        business object to be used in the query. This field must use an
        XPath notation as per the MBP to provide a unique
        reference.</description>
    """

    value: list[TextType] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    operator_code: None | QueryOperatorCodeType = field(
        default=None,
        metadata={
            "name": "operatorCode",
            "type": "Attribute",
        },
    )
    path: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
