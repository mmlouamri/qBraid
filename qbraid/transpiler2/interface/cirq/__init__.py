"""
==============================================================
 Cirq Transpiler2  (:mod:`qbraid.transpiler2.interface.cirq`)
==============================================================

.. currentmodule:: qbraid.transpiler2.interface.cirq

Wrapping Strategy
------------------

Cirq's circuit layer stores all circuit data in a bottom up fashion. Qubit objects are stored
locally as part of an instruction object (called an "operation" in cirq). Additionally, abstract
parameters are stored locally as attributes of gates. Circuit objects have methods that can
generate of a comprehensive list of qubits or parameters, but these are inefficient.

The qBraid transpiler changes this paradigm, storing qubit and parameter representations globally.
For this reason, all instructions and moments must be parsed from within the same function
to efficiently generate these global lists.

Note:
   the ``all_qubits`` method returns a set of all qubits in the circuit. This set has no particular
   order, so the intermediate serialization of this list can lead to different output circuits
   depending on the issue.

Cirq's moment object is relatively unique amongst major packages. For the most detailed control,
the transpiler has a decicated wrapper object for moments, though this object is not used for any
other package.

Output Strategy
---------------

.. autosummary::
   :toctree: ../stubs/

   CirqCircuitWrapper
   compute_density_matrix
   execute
   execute_with_depolarizing_noise
   execute_with_shots
   execute_with_shots_and_depolarizing_noise
   sample_bitstrings

"""
from qbraid.transpiler2.interface.cirq.cirq_utils import (
    compute_density_matrix,
    execute,
    execute_with_depolarizing_noise,
    execute_with_shots,
    execute_with_shots_and_depolarizing_noise,
    sample_bitstrings,
)

from .circuit_wrapper import CirqCircuitWrapper
