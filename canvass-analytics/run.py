import argparse

import problem_1
import problem_2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run challenge solutions")
    parser.add_argument("--challenge", type=int, required=False)
    parser.add_argument("--test", type=str, required=False)

    args = parser.parse_args()
    challenge = args.challenge
    test = args.test

    if challenge == 1:
        problem_1.all_even_digits()
    elif challenge == 2:
        problem_2.main()
    elif test == "test_make_chunks":
        problem_2.test_make_chunks()
    elif test == "test_merge_chunks":
        problem_2.test_merge_chunks()
    else:
        raise Exception(f"Non existing challenge {challenge}")
