# Quantum Mystery Flow

Quantum Mystery Flow is a quantum computing game written in Python that is intended to show newcomers how quantum circuits look and what their actions might result in when acting on a qubit. 

The premise is simple, once the game starts, a quantum circuit will be executed, and the final qubits on the Bloch Ssphere as well as the applied quantum gates will be shown to the user. The goal of the player is to determine the order in which the quantum gates were used. The qubits are always initialized as 0, and individual gates act only on the first qubit. 

Once you run the game, you will see the following image:

![QntmMysteryFlow.PNG](https://github.com/iQuHACK/2021_Quacks/blob/dev/sprites/QntmMysteryFlow.PNG)

Upon starting the game you will see the next grid

![cards.PNG](https://github.com/iQuHACK/2021_Quacks/blob/dev/sprites/cards.PNG)

Which means the game has already started. In the folder in which you are working, an image named "out.png" will be saved, this is the Bloch Sphere representation of the circuit, which is useful to then determine the order of the gates used. Another file named "out2.png" is created, this is the quantum circuit, thus, the answer. 

After placing the cards on the grids, press the button "check". This will generate images "try1.png" (the Bloch sphere created with your try) and "try2.png", which shows the result the player constructed. 


## Future work - Stuff we would like to do but did not have enought time
-Creating an option such that gates can also act on the first qubit

-Omitting gate combinations that might result in the qubit not being changed at all

-Omitting entangled states, which cannot be represented by a sphere
