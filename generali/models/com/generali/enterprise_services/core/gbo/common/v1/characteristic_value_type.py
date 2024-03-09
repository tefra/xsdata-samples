from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_type import (
    DateType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.duration_type import (
    DurationType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.indicator_type import (
    IndicatorType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.percent_type import (
    PercentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.quantity_type import (
    QuantityType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.time_type import (
    TimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class CharacteristicValueType(BaseComponentType):
    """
    <description xmlns="">A value of the characteristic.</description>
    """

    text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    amount: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    quantity: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    numeric: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "Numeric",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    percent: Optional[PercentType] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    indicator: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    duration: Optional[DurationType] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    time: Optional[TimeType] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    date: Optional[DateType] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
