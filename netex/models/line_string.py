from dataclasses import dataclass
from netex.models.line_string_type import LineStringType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LineString(LineStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
