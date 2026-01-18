from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.note_type import (
    NoteType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class BaseGbopartsTypeNotes:
    """
    :ivar note: <description xmlns="">Notes related to the
        entity.</description>
    """

    class Meta:
        global_type = False

    note: list[NoteType] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )
