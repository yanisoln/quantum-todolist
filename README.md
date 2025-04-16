# 🧠 Quantum Todo List

> Because productivity decisions should be made by collapsing a wavefunction.

## What is this?

This is a to-do list powered by **AWS Braket** — yes, a quantum computing service — just to pick **what you should do today**.

It doesn’t try to optimize your calendar. It doesn’t use AI to prioritize your tasks.  
Instead, it leverages the raw power of quantum superposition to randomly select what the universe _wants_ you to focus on.

🌀 **It's chaotic. It's meaningless. It's beautiful.**

## How it works

- Your task list is encoded as binary indices.
- We create a quantum circuit with as many qubits as needed to cover the number of tasks.
- We put those qubits into superposition using Hadamard gates.
- We collapse the state by measuring them.
- And voilà: quantum randomness gives you your task(s) for the day.

## Example output

```bash
⚛️ Generating today's quantum to-do list...

✅ Your quantum-powered tasks for today:
→ Clean your email inbox with foxgate.io
→ Blink dramatically while typing
→ Work on my project
```

Yes, a quantum computer really told you to blink dramatically while typing.  
Who are you to argue with the multiverse?

## Why?

Because we could.

Also, because using a million-dollar quantum infrastructure to avoid making decisions yourself is peak 2025 energy.

## Run it locally

```bash
git clone git@github.com:yanisoln/quantum-todolist.git
cd quantum-todo
pip install -r requirements.txt
python quantum_todo.py
```

By default, it runs on the local simulator.  
If you're feeling spicy, you can switch to `AWS Braket` cloud simulator (SV1) and let Amazon’s quantum backend pick your fate.  
Just make sure your AWS credentials are configured and you’re in a supported region (like `us-east-1`).

Or if you are willing to pay (about 3-4$ per run), you can use a real quantum device, like rigetti ankaa-3 (arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3)

## Todo List Highlights

The task pool includes things like:

- “Reply to emails”
- “Read a book”
- “Stare at the wall for 3 minutes”
- “Email someone and only write ‘it has begun.’”
- “Drink some water”

You know... the essentials.

---

> _“Let randomness guide you, for structure is merely a prison.”_  
> — Probably Schrödinger (or maybe his cat)
