from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.duration_type import (
    DurationType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class TimePeriodType:
    """
    <description xmlns="">A component that states the date and time from
    which this business object is effective (or valid) and the date and
    time to which it is effective.

    Again the ISO8601 standard must be used.</description>.

    :ivar from_date_time: <description xmlns="">The timestamp from which
        the business object or component is effective.</description>
    :ivar to_date_time: <description xmlns="">The timestamp to which the
        business object or component is effective.</description>
    :ivar duration: <description xmlns="">The duration from the start
        date of the time period.</description>
    """

    from_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "FromDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    to_date_time: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "ToDateTime",
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
