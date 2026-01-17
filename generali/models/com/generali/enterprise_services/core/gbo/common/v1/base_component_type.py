from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseComponentType:
    """
    <description xmlns="">Base type for all business objects and
    components.</description>.

    :ivar action_code: <description xmlns="">The @actionCode attribute
        is used within a modification operation to indicate the action
        (add, update, delete) intended on a component.</description>
    """

    action_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "actionCode",
            "type": "Attribute",
        },
    )
