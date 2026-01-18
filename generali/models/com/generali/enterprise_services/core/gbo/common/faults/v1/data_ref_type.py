from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/faults/v1"
)


@dataclass
class DataRefType:
    """
    <description xmlns="">A reference to the specific field or component
    within the GBO that generated the failure.</description>.

    :ivar path_name_text: <description xmlns="">The pseudo-XPath
        reference to the specific field or component within the
        GBO.</description>
    :ivar path_value_text: <description xmlns="">The value of the field
        referenced by the Path Name.</description>
    """

    path_name_text: None | str = field(
        default=None,
        metadata={
            "name": "PathNameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/faults/v1",
            "required": True,
        },
    )
    path_value_text: None | str = field(
        default=None,
        metadata={
            "name": "PathValueText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/faults/v1",
        },
    )
