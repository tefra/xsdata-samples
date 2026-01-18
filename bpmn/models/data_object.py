from __future__ import annotations

from dataclasses import dataclass

from .t_data_object import TDataObject

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class DataObject(TDataObject):
    class Meta:
        name = "dataObject"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
