#!/usr/bin/env python3

# QWOQ2QIR: Qiskit (without Qiskit) to Quantum Intermediate Representation
# This file will be used as an input to the parser

# Bernstein-Vazirani algorithm on 6 qubits (similar to the example with the Mock Language)

from qiskit import Aer, execute, QuantumCircuit

qc = QuantumCircuit(7, 6)

# Set first 6 qubits to |+>
qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
qc.h(4)
qc.h(5)

# Set ancilla qubit to |->
qc.h(6)
qc.z(6)

# Apply oracle
qc.cx(1, 6)
qc.cx(3, 6)
qc.cx(5, 6)

# Apply Hadamard to the first 6 qubits
qc.h(5)
qc.h(4)
qc.h(3)
qc.h(2)
qc.h(1)
qc.h(0)

# Measure the first 6 qubits
qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)
qc.measure(3, 3)
qc.measure(4, 4)
qc.measure(5, 5)

job = execute(qc, Aer.get_backend("qasm_simulator"), shots=1024)

# we can get the result of the outcome as follows
counts = job.result().get_counts(qc)
print(counts)
