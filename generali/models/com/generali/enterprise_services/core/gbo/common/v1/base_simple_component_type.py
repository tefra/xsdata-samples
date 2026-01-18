from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseSimpleComponentType(BaseComponentType):
    """
    <description xmlns="">A simple component that is not identified, it
    contains fields for a name, description and type.</description>.

    :ivar name_text: <description xmlns="">The name of the
        characteristic.</description>
    :ivar desc_text: <description xmlns="">The description of the
        characteristic.</description>
    :ivar full_name: <description xmlns="">Full Name of the
        characteristic.</description>
    :ivar type_code: <description xmlns="">The type of the
        characteristic.</description>
    """

    name_text: TextType | None = field(
        default=None,
        metadata={
            "name": "NameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    desc_text: TextType | None = field(
        default=None,
        metadata={
            "name": "DescText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    full_name: TextType | None = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    type_code: CodeType | None = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
