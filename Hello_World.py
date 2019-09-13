# -*- coding: utf-8 -*-
# See PEG 263. This Python file uses the following encoding: utf-8
"""Quantum Computing Hello World Script

## module metatdata
Author: karstdiver
Copyright: Copyright 2019, Quantum Computing
Credits: Lots of resuse code from IBM documentation
License: None
Version: {major}.{minor}.{rel} 1.1.1
Maintainer: None
Email: Not provided
Status: experimental use at own risk

## brief description of the module and its purpose
A simple example that entangles two qubits then measures both qubits.
Output is a circuit display.
Output is a histogram of mutiple run measurement results.
A 50/50 histogram is expected for these entangled bits (a 1 or 0 are equally likely to occur).
Note: simulator does not have noise errors like the real quantum computer.
    
## list of any classes, exception, functions, and any other objects exported by the module
None

## arguments (both required and optional) that are passed including keyword arguments
None

## label any arguments that are considered optional
None

## side effects that occur when executing the function
None on simulator
Changes to the quantum universe on the real quantum computer ;)

## exceptions that are raised
None expected :)

## restrictions on when the function can be called
Written for the IBM Q Experience Qiskit Notebook software development environment
"""

%matplotlib inline
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()

## Define a two-qubit quantum circuit
q = QuantumRegister(2, 'q')
c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(q, c)

## Apply the quantum gates
circuit.h(q[0])
circuit.cx(q[0], q[1])

## Finish off with the measurements
circuit.measure(q, c)

## Draw the circuit
%matplotlib inline
print("\n*** Circuit Drawing Output ***\n")
circuit.draw(output="mpl")

## execute the circuit
#TODO: add code to allow real quantum computer
quantum_computer_name = 'qasm_simulator'  # SDE specific name?
print("\n*** Start: Quantum computer \"", quantum_computer_name, "\" Output ***")
computer = Aer.get_backend(quantum_computer_name)
job = execute(circuit, backend=computer, shots=1024)
result = job.result()
print("*** Run Results Details ***")
print(result)

## plot a histogram of the results
counts = result.get_counts(circuit)
print("\nQubits measurement state counts", counts)
print("\n*** Quantum computer \"", quantum_computer_name, "\" Histogram Output ***")
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)

#print("\n*** End: Quantum computer \"", quantum_computer_name, "\" Output ***")
