from braket.circuits.gate import Gate as BraketGate

from qbraid.transpiler.gate import GateWrapper
from qbraid.transpiler.utils import get_braket_gate_data


class BraketGateWrapper(GateWrapper):
    def __init__(self, gate: BraketGate):

        super().__init__()

        self.gate = gate
        self.name = None

        data = get_braket_gate_data(gate)

        self.matrix = data["matrix"]
        self.params = data["params"]

        if "base_gate" in data.keys():
            self.base_gate = BraketGateWrapper(data["base_gate"])
            # self.base_gate = data['base_gate']
            self.num_controls = data["num_controls"]

        self._gate_type = data["type"]
