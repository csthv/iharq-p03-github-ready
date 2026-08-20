"""Typed fail-closed exceptions used by the P03 implementation."""

class P03Error(RuntimeError):
    """Base class for governed P03 failures."""


class GateBlocked(P03Error):
    """A precondition was not met and downstream work must not run."""

    def __init__(self, gate_id: str, reason_code: str, detail: str):
        super().__init__(f"{gate_id}:{reason_code}: {detail}")
        self.gate_id = gate_id
        self.reason_code = reason_code
        self.detail = detail


class ContractViolation(P03Error):
    """An input, score, schema, or lineage contract was violated."""


class LeakageBlocked(ContractViolation):
    """An operation was blocked before computation by the leakage firewall."""


class IneligibleMethod(ContractViolation):
    """A method was requested outside its declared score/support contract."""


class ResumeRejected(P03Error):
    """A checkpoint does not match the current immutable fingerprints."""


class SecurityViolation(P03Error):
    """A secret-like literal or unsafe path was detected."""

