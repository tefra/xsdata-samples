from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import BaseComponentType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.characteristics_type import CharacteristicsType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.note_type import NoteType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.status_history_type import StatusHistoryType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseGbopartsType(BaseComponentType):
    """
    <description xmlns="">The base type for the business object parts
    components.</description>

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

    notes: Optional["BaseGbopartsType.Notes"] = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    characteristics: Optional[CharacteristicsType] = field(
        default=None,
        metadata={
            "name": "Characteristics",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    status_history: Optional[StatusHistoryType] = field(
        default=None,
        metadata={
            "name": "StatusHistory",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )

    @dataclass
    class Notes:
        """
        :ivar note: <description xmlns="">Notes related to the
            entity.</description>
        """
        note: List[NoteType] = field(
            default_factory=list,
            metadata={
                "name": "Note",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
                "min_occurs": 1,
            }
        )
