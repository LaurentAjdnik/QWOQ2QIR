# QWOQ2QIR

Qiskit without Qiskit to Quantum Intermediate Representation.

Input file = `qwoq2qir_parse_me.py` (Bernstein-Vazirani algorithm)

Parsing engine = `qwoq2qir.py`

Qiskit source code is parsed without using the Qiskit library.
Rather, we use Python Abstract Syntax Tree (AST) and pyqir-generator.

## While walking the tree

The parser will display:
```
== Walk the tree ==
Hadamard gate on qubit 0
Hadamard gate on qubit 1
Hadamard gate on qubit 2
Hadamard gate on qubit 3
Hadamard gate on qubit 4
Hadamard gate on qubit 5
Hadamard gate on qubit 6
Z gate on qubit 6
CX gate on qubits 1 (control) and 6 (target)
CX gate on qubits 3 (control) and 6 (target)
CX gate on qubits 5 (control) and 6 (target)
Hadamard gate on qubit 5
Hadamard gate on qubit 4
Hadamard gate on qubit 3
Hadamard gate on qubit 2
Hadamard gate on qubit 1
Hadamard gate on qubit 0
Measurement on qubit 0 into bit 0
Measurement on qubit 1 into bit 1
Measurement on qubit 2 into bit 2
Measurement on qubit 3 into bit 3
Measurement on qubit 4 into bit 4
Measurement on qubit 5 into bit 5
```

## Resulting QIR

```
; ModuleID = 'QWOW2QIR'
source_filename = "QWOW2QIR"

%Qubit = type opaque
%Result = type opaque

define void @main() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 5 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 6 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* inttoptr (i64 6 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 1 to %Qubit*), %Qubit* inttoptr (i64 6 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 3 to %Qubit*), %Qubit* inttoptr (i64 6 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* inttoptr (i64 5 to %Qubit*), %Qubit* inttoptr (i64 6 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 5 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 4 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 3 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* null)
  %result0 = call %Result* @__quantum__qis__m__body(%Qubit* null)
  %result1 = call %Result* @__quantum__qis__m__body(%Qubit* inttoptr (i64 1 to %Qubit*))
  %result2 = call %Result* @__quantum__qis__m__body(%Qubit* inttoptr (i64 2 to %Qubit*))
  %result3 = call %Result* @__quantum__qis__m__body(%Qubit* inttoptr (i64 3 to %Qubit*))
  %result4 = call %Result* @__quantum__qis__m__body(%Qubit* inttoptr (i64 4 to %Qubit*))
  %result5 = call %Result* @__quantum__qis__m__body(%Qubit* inttoptr (i64 5 to %Qubit*))
  ret void
}

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__z__body(%Qubit*)

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

declare %Result* @__quantum__qis__m__body(%Qubit*)

attributes #0 = { "EntryPoint" "requiredQubits"="7" }
```

