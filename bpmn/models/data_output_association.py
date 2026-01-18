from __future__ import annotations

from dataclasses import dataclass

from .t_data_output_association import TDataOutputAssociation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class DataOutputAssociation(TDataOutputAssociation):
    class Meta:
        name = "dataOutputAssociation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
