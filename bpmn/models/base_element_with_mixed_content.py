from dataclasses import dataclass

from .t_base_element_with_mixed_content import TBaseElementWithMixedContent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class BaseElementWithMixedContent(TBaseElementWithMixedContent):
    class Meta:
        name = "baseElementWithMixedContent"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
