from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.measure_type import MeasureType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class AttachmentTypeSizeMeasure(MeasureType):
    class Meta:
        global_type = False
