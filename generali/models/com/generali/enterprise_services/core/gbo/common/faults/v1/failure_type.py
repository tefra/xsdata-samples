from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.faults.v1.data_ref_type import (
    DataRefType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/faults/v1"
)


@dataclass
class FailureType:
    """
    <description xmlns="">A component that describes individual failures
    within the fault.

    This component is used to support multiple causes to the fault, i.e.
    where the fault is generated from one or more API calls or one or more
    validation failures.</description>.

    :ivar code: <description xmlns="">The code identifying the specific
        failure.</description>
    :ivar text: <description xmlns="">The human-readable text of the
        specific failure.</description>
    :ivar data_ref: <description xmlns="">A reference to the specific
        field or component within the GBO that generated the
        failure.</description>
    """

    code: str | None = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/faults/v1",
        },
    )
    text: str | None = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/faults/v1",
            "required": True,
        },
    )
    data_ref: DataRefType | None = field(
        default=None,
        metadata={
            "name": "DataRef",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/faults/v1",
        },
    )
