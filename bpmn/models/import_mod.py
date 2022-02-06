from dataclasses import dataclass
from .t_import import TImport

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Import(TImport):
    class Meta:
        name = "import"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
