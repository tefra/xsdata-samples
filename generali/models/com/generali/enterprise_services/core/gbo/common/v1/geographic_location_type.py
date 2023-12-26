from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.measure_type import (
    MeasureType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_simple_component_type import (
    BaseSimpleComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class GeographicLocationType(BaseSimpleComponentType):
    """
    <description xmlns="">A geographic location, latitude and
    longitude</description>

    :ivar altitude_measure: <description xmlns="">The measure of the
        altitude that reflects the vertical elevation of an object above
        a surface for this geographical coordinate (Reference ISO
        6709</description>
    :ivar latitude_measure: <description xmlns="">The measure of the
        latitude as an angular distance north or south from the Equator
        meridian to the meridian of a specific place for this
        geographical coordinate. (Reference ISO 6709)</description>
    :ivar longitude_measure: <description xmlns="">The measure of the
        longitude as an angular distance east or west from the Greenwich
        meridian to the meridian of a specific place (Reference ISO
        6709)</description>
    :ivar latitude_direction_code: <description xmlns="">The indication
        of whether the latitude compass direction from the Equator
        meridian to the meridian of a specific place is North (+) or
        South (-). (Reference ISO 6709)</description>
    :ivar longitude_direction_code: <description xmlns="">The indication
        of whether the longitude as a compass direction from the
        Greenwich meridian to the meridian of a specific place is East
        (-) or West (+) for this geographical coordinate. (Reference ISO
        6709)</description>
    :ivar system_id: <description xmlns="">A unique identifier of the
        system used for measuring a geographical coordinate other than
        Global Positioning System</description>
    """

    altitude_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "AltitudeMeasure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    latitude_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "LatitudeMeasure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    longitude_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "LongitudeMeasure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    latitude_direction_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "LatitudeDirectionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    longitude_direction_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "LongitudeDirectionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    system_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "SystemID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
