from __future__ import annotations

from dataclasses import dataclass

from .t_extension import TExtension

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Extension(TExtension):
    class Meta:
        name = "extension"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
