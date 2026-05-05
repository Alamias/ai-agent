from functions.get_file_content import get_file_content


def _print_case(call_line: str, result_label: str, result: str) -> None:
    print(call_line)
    print(result_label)
    if result.startswith("Error:"):
        print(f"    {result}")
    else:
        for line in result.split("\n"):
            if line:
                print(f"  {line}")
    print()


if __name__ == "__main__":
    _print_case(
        'get_file_content("calculator", "lorem.txt"):',
        "Result for 'lorem.txt' file:",
        get_file_content("calculator", "lorem.txt"),
    )
    _print_case(
        'get_file_content("calculator", "main.py"):',
        "Result for 'main.py' file:",
        get_file_content("calculator", "main.py"),
    )
    _print_case(
        'get_file_content("calculator", "pkg/calculator.py"):',
        "Result for 'pkg/calculator.py' file:",
        get_file_content("calculator", "pkg/calculator.py"),
    )
    _print_case(
        'get_file_content("calculator", "/bin/cat"):',
        "Result for '/bin/cat' file:",
        get_file_content("calculator", "/bin/cat"),
    )
    _print_case(
        'get_file_content("calculator", "does_not_exist.txt"):',
        "Result for 'does_not_exist.txt' file:",
        get_file_content("calculator", "does_not_exist.txt"),
    )
