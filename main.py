import multiprocessing as mp
import time


def halt_immediately():
    return 42


def count_to_a_million():
    total = 0
    for i in range(1_000_000):
        total += i
    return total


def halt_later():
    # This program DOES halt, just not immediately.
    time.sleep(2)
    return "done"


def loop_forever():
    while True:
        pass


PROGRAMS = [
    ("halt_immediately", halt_immediately),
    ("count_to_a_million", count_to_a_million),
    ("halt_later", halt_later),
    ("loop_forever", loop_forever),
]


def _runner(program):
    program()


def observe(program, timeout=1.0):
    """
    Run a program for at most `timeout` seconds.

    Returns:
        "HALTED"  - we observed the program finish.
        "UNKNOWN" - it did not finish within the time limit.

    Important:
    UNKNOWN does NOT mean "runs forever".
    """
    process = mp.Process(target=_runner, args=(program,))
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        return "UNKNOWN"

    return "HALTED"


def print_paradox():
    print("\nWhy can't we make a perfect halting detector?")
    print("-" * 48)
    print(
        """
Suppose a perfect function HALTS(P) existed.

PARADOX(P):
    if HALTS(P):
        loop forever
    else:
        stop

Now ask what happens to:

    PARADOX(PARADOX)

If HALTS says "yes", PARADOX loops forever.
If HALTS says "no", PARADOX stops.

Either answer makes HALTS wrong.
"""
    )


def main():
    timeout = 1.0

    print("WILL IT HALT?")
    print("=" * 48)
    print(f"Observation limit: {timeout:.1f} second\n")

    for name, program in PROGRAMS:
        result = observe(program, timeout)
        print(f"{name:<22} -> {result}")

    print(
        "\nUNKNOWN only means: "
        "\"we did not see it halt within the time limit.\""
    )

    print_paradox()


if __name__ == "__main__":
    mp.freeze_support()
    main()
