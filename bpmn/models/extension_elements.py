from __future__ import annotations

from dataclasses import dataclass

from .t_extension_elements import TExtensionElements

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ExtensionElements(TExtensionElements):
    class Meta:
        name = "extensionElements"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
