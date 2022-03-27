"""BraketQuantumtaskWrapper Class"""

from qbraid.devices.localjob import LocalJobWrapper

from .result import BraketResultWrapper


class BraketLocalQuantumTaskWrapper(LocalJobWrapper):
    """Wrapper class for Amazon Braket ``LocalQuantumTask`` objects."""

    @property
    def id(self):
        """Return a unique id identifying the job."""
        return self.vendor_jlo.id

    def metadata(self):
        """Return the metadata regarding the job."""
        return dict(self.vendor_jlo.result().task_metadata)

    def result(self):
        """Return the results of the job."""
        return BraketResultWrapper(self.vendor_jlo.result())
