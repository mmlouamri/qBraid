from braket.circuits.instruction import Instruction as BraketInstruction

from qbraid.transpiler.instruction import InstructionWrapper
from .gate import BraketGateWrapper


class BraketInstructionWrapper(InstructionWrapper):
    def __init__(self, instruction: BraketInstruction, qubits):

        super().__init__()

        self.instruction = instruction
        self.qubits = qubits
        self.gate = BraketGateWrapper(instruction.operator)
