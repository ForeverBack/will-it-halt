# will-it-halt

A tiny Python experiment about the **Halting Problem**.

The question sounds simple:

> Given any program and its input, can we always determine whether it will eventually stop?

Alan Turing showed that there is no algorithm that can correctly answer that question for **every possible program**.

This project does **not** try to solve the Halting Problem.  
Instead, it shows why a practical timeout-based checker can only say:

- `HALTED` — we actually observed the program finish.
- `UNKNOWN` — it did not finish within our time limit.

`UNKNOWN` does **not** mean "runs forever".

## Example

The program tests a few simple functions:

```text
WILL IT HALT?
================================================
Observation limit: 1.0 second

halt_immediately       -> HALTED
count_to_a_million     -> HALTED
halt_later             -> UNKNOWN
loop_forever           -> UNKNOWN
```

`halt_later` is the important example.

It really does stop after 2 seconds, but if we only watch it for 1 second,
we cannot distinguish it from a program that runs forever.

## The paradox

Imagine a perfect function called `HALTS(P)` that can always tell whether
a program will stop.

Now define:

```text
PARADOX(P):
    if HALTS(P):
        loop forever
    else:
        stop
```

What happens when we run:

```text
PARADOX(PARADOX)
```

- If `HALTS` says it will stop, `PARADOX` deliberately loops forever.
- If `HALTS` says it will loop forever, `PARADOX` immediately stops.

Either answer contradicts the detector.

That is the core idea behind the undecidability of the Halting Problem.

## Run

Python 3 is enough. No external packages are required.

```bash
python main.py
```

## Why I made this

I wanted a small program that turns an abstract idea from theoretical
computer science into something visible and runnable.

It cannot prove that an arbitrary running program will never stop — and
that limitation is exactly the point.
