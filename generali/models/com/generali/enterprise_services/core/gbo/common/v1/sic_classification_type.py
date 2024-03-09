from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.sictype_enum import (
    SictypeEnum,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class SicClassificationType:
    code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
    type_value: Optional[SictypeEnum] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
    short_description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "ShortDescription",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
