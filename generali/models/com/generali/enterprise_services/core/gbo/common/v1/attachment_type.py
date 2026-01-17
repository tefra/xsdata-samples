from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.binary_object_type import (
    BinaryObjectType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.uritype import (
    Uritype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.attachment_type_size_measure import (
    AttachmentTypeSizeMeasure,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class AttachmentType(BaseIdentifiedComponentType):
    """
    <description xmlns="">A type that specifies an attachment to a business
    object either as an embedded object or as a reference to an external
    document.</description>.

    :ivar size_measure: <description xmlns="">The size in Bytes of the
        of the document or attachment. If this component contains the
        embedded data then the size is the size of the embedded data, if
        it is a reference without the data then it is the size of the
        referenced document.</description>
    :ivar binary_object: <description xmlns="">Stores embedded base64
        encoded data. Used to carry documents, images, etc. within the
        parent business object.</description>
    :ivar reference_uri: <description xmlns="">A URI reference to an
        external document.</description>
    """

    size_measure: Optional[AttachmentTypeSizeMeasure] = field(
        default=None,
        metadata={
            "name": "SizeMeasure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    binary_object: Optional[BinaryObjectType] = field(
        default=None,
        metadata={
            "name": "BinaryObject",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    reference_uri: Optional[Uritype] = field(
        default=None,
        metadata={
            "name": "ReferenceURI",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
