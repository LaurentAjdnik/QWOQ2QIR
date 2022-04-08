#!/usr/bin/env python3

# QWOQ2QIR: Qiskit (without Qiskit) to Quantum Intermediate Representation
# This file will parse Qiskit without Qiskit

# astpretty for nicer display of Python AST: pip install astpretty
import ast, astpretty
from pyqir.generator import BasicQisBuilder, SimpleModule


def main():
    with open("qwoq2qir_parse_me.py", "r") as source:
        tree = ast.parse(source.read())

    print("\n\n== Dump the whole source code ==")

    # print(ast.dump(tree)) # Ugly version, by default
    astpretty.pprint(tree)  # Nicer version

    print("\n\n== Walk the tree ==")

    analyzer = Analyzer()
    analyzer.visit(tree)

    print("\n\n== Output QIR ==")
    print(analyzer.module.ir())


class Analyzer(ast.NodeVisitor):
    module: SimpleModule
    builder: BasicQisBuilder

    def __init__(self):
        pass

    def visit_Call(self, node: ast.Call):
        # astpretty.pprint(node)
        if isinstance(node.func, ast.Name):
            name: ast.Name = node.func
            if name.id == "QuantumCircuit":
                num_qubits = node.args[0].value
                num_results = node.args[1].value
                self.module = SimpleModule("QWOW2QIR", num_qubits, num_results)
                self.builder = BasicQisBuilder(self.module.builder)

        if isinstance(node.func, ast.Attribute):
            attribute: ast.Attribute = node.func
            if attribute.attr == "cx":
                control = node.args[0].value
                target = node.args[1].value
                print(
                    "CX gate on qubits "
                    + str(control)
                    + " (control) and "
                    + str(target)
                    + " (target)"
                )
                self.builder.cx(self.module.qubits[control], self.module.qubits[target])
            if attribute.attr == "h":
                qubit = node.args[0].value
                print("Hadamard gate on qubit " + str(qubit))
                self.builder.h(self.module.qubits[qubit])
            if attribute.attr == "measure":
                qubit = node.args[0].value
                bit = node.args[1].value
                print("Measurement on qubit " + str(qubit) + " into bit " + str(bit))
                self.builder.m(self.module.qubits[qubit], self.module.results[bit])

            if attribute.attr == "z":
                qubit = node.args[0].value
                print("Z gate on qubit " + str(qubit))
                self.builder.z(self.module.qubits[qubit])
        self.generic_visit(node)


if __name__ == "__main__":
    main()
