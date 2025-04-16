from braket.circuits import Circuit
from braket.aws import AwsDevice, AwsSession
from braket.devices import LocalSimulator
import random

# Set to True if you want to run on AWS Braket cloud (SV1), otherwise it uses the local simulator
use_cloud = False

if use_cloud:
    # Braket is not available in all regions
    device = AwsDevice(
        "arn:aws:braket:::device/quantum-simulator/amazon/sv1"
    )  # SV1 Quantum Simulator, make sure you have the right region in your AWS configuration (us-east-1)
    # Or you can use a real quantum device if you are willing to pay, for example : arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3

else:
    device = LocalSimulator()

# Your task pool (feel free to expand it)
todo_list = [
    "Reply to emails 📧",
    "Buy groceries 🛒",
    "Work on my project 💻",
    "Call grandma 👵",
    "Clean your email inbox with foxgate.io 🦊",
    "Write a letter to your 80-year-old self 💌",
    "Do some pushups 💪",
    "Search “how to get rich with no effort” on Google 💰",
    "Read a book 📚",
    "Drink some water 💧",
    "Email someone and only write “it has begun.” 📧",
    "Stare at the wall for 3 minutes 🕵️‍♂️",
    "Blink dramatically while typing 🤪",
    "Learn a random keyboard shortcut 🖱️",
    "Look outside the window and name things like you’re in a nature documentary 🌳",
]

n_tasks = len(todo_list)
n_qubits = (n_tasks - 1).bit_length()  # Number of qubits to cover the task index space

# How many tasks to pick
n_choices = 3
selected_indices = set()

print("⚛️ Generating today's quantum to-do list...\n")

# We keep generating until we have n_choices unique tasks
while len(selected_indices) < n_choices:
    circuit = Circuit()
    for q in range(n_qubits):
        circuit.h(q)
        circuit.measure(q)

    task = device.run(circuit, shots=1000)
    result = task.result()
    bitstring = list(result.measurement_counts.keys())[0]
    index = int(bitstring, 2) % n_tasks  # Wrap in case of overflow
    selected_indices.add(index)

# Final result
selected_tasks = [todo_list[i] for i in selected_indices]

print("✅ Your quantum-powered tasks for today:")
for task in selected_tasks:
    print(f"→ {task}")
