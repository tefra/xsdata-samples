from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.binary_object_type import BinaryObjectType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import BaseIdentifiedComponentType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.simple_uom_amount_of_information_code_type import SimpleUomAmountOfInformationCodeType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class AttachmentType(BaseIdentifiedComponentType):
    """
    <description xmlns="">A type that specifies an attachment to a business
    object either as an embedded object or as a reference to an external
    document.</description>

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
    size_measure: Optional["AttachmentType.SizeMeasure"] = field(
        default=None,
        metadata={
            "name": "SizeMeasure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    binary_object: Optional[BinaryObjectType] = field(
        default=None,
        metadata={
            "name": "BinaryObject",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    reference_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceURI",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )

    @dataclass
    class SizeMeasure:
        """
        :ivar value:
        :ivar unit_code:
        :ivar unit_code_list_version_id: <ns1:Name
            xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Measure
            Unit. Code List Version. Identifier</ns1:Name>
            <ns1:Definition
            xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
            version of the measure unit code list.</ns1:Definition>
            <ns1:PrimitiveType
            xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
        """
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit_code: Optional[SimpleUomAmountOfInformationCodeType] = field(
            default=None,
            metadata={
                "name": "unitCode",
                "type": "Attribute",
                "required": True,
            }
        )
        unit_code_list_version_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "unitCodeListVersionID",
                "type": "Attribute",
            }
        )
