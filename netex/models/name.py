from dataclasses import dataclass
from netex.models.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Name(CodeType):
    class Meta:
        name = "name"
        namespace = "http://www.opengis.net/gml/3.2"
