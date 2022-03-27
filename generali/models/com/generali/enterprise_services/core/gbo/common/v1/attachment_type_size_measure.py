from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.simple_uom_amount_of_information_code_type import SimpleUomAmountOfInformationCodeType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class AttachmentTypeSizeMeasure:
    """
    :ivar value:
    :ivar unit_code:
    :ivar unit_code_list_version_id: <ns1:Name
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">Measure
        Unit. Code List Version. Identifier</ns1:Name> <ns1:Definition
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">The
        version of the measure unit code list.</ns1:Definition>
        <ns1:PrimitiveType
        xmlns:ns1="urn:un:unece:uncefact:documentation:standard:CoreComponentsTechnicalSpecification:2">string</ns1:PrimitiveType>
    """
    class Meta:
        global_type = False

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
