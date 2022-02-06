from dataclasses import dataclass
from .t_input_output_binding import TInputOutputBinding

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class IoBinding(TInputOutputBinding):
    class Meta:
        name = "ioBinding"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
