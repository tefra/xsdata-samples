from __future__ import annotations

from dataclasses import dataclass

from .t_text_annotation import TTextAnnotation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TextAnnotation(TTextAnnotation):
    class Meta:
        name = "textAnnotation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
