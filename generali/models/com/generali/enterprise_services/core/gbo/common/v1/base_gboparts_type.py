from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_gboparts_type_notes import (
    BaseGbopartsTypeNotes,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.characteristics_type import (
    CharacteristicsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.status_history_type import (
    StatusHistoryType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseGbopartsType(BaseComponentType):
    """
    <description xmlns="">The base type for the business object parts
    components.</description>.

    :ivar notes: <description xmlns="">The set of notes or comments for
        the parent context.</description>
    :ivar characteristics: <description xmlns="">A type that provides a
        specification for the parent context. This is the set of
        characteristics (name-value pairs) used to specify the parent
        context.</description>
    :ivar status_history: <description xmlns="">The history of the
        lifecycle of the parent context.</description>
    """

    class Meta:
        name = "BaseGBOPartsType"

    notes: None | BaseGbopartsTypeNotes = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    characteristics: None | CharacteristicsType = field(
        default=None,
        metadata={
            "name": "Characteristics",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    status_history: None | StatusHistoryType = field(
        default=None,
        metadata={
            "name": "StatusHistory",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
