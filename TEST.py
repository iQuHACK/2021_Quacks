import random
import matplotlib
import numpy as np
from qiskit import (QuantumCircuit,execute,Aer)
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_state_city, plot_bloch_multivector
from qiskit.visualization import plot_state_paulivec, plot_state_hinton
from qiskit.visualization import plot_state_qsphere

def quantum_gen():
    n = np.linspace(0,4,5) #Total amount of different quantum gates
    nrand = np.random.randint(0,4,5) #Random generated identifiers for the quantum gates

    #imulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2,2)

    #Gates to be used: 
    # 0: Rx(pi/4)
    # 1: Ry(pi/4)
    # 2: Hadamard
    # 3: CNOT
    # 4: SWAP

    for i in range(4):
        if nrand[i] == 0:
            circuit.rx(np.pi/4,0)
        if nrand[i] == 1:
            circuit.ry(np.pi/4, 0)
        if nrand[i] == 2:
            circuit.h(0)
        if nrand[i] == 3:
            circuit.cnot(0, 1)
        if nrand[i] == 4:
            circuit.swap(0, 1)

    backend = Aer.get_backend('statevector_simulator')
    result = execute(circuit, backend).result()
    statevector = result.get_statevector()
    #print(statevector)
    plot_bloch_multivector(statevector).savefig('out.png')
    circuit.draw(output='mpl').savefig('out2.png')

    return nrand