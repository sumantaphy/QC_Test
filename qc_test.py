from qiskit import QuantumCircuit 
qc = QuantumCircuit(2)
qc.h(0)
qc.x(1)
qc.cx(0,1)

qc.draw (output='mpl')

from qiskit.quantum_info import Pauli

zz = Pauli('ZZ')
zi = Pauli('ZI')
iz = Pauli('IZ')
xx = Pauli('XX')
xi = Pauli('XI')
ix = Pauli('IX')

observables = [zz,zi,iz,xx,xi,ix]

from qiskit_aer.primitives import Estimator

estimator = Estimator()

job = estimator.run([qc] * len(observables),observables)
job.result()

import matplotlib.pyplot as plt

data = ['zz', 'zi', 'iz', 'xx', 'xi','ix']
values = job.result().values

plt.plot(data, values, '-o')
plt.xlabel('observables')
plt.ylabel('exp values')

plt.show()
