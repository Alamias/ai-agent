from functions.get_files_info import get_files_info


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
        'get_files_info("calculator", "."):',
        "Result for current directory:",
        get_files_info("calculator", "."),
    )
    _print_case(
        'get_files_info("calculator", "pkg"):',
        "Result for 'pkg' directory:",
        get_files_info("calculator", "pkg"),
    )
    _print_case(
        'get_files_info("calculator", "/bin"):',
        "Result for '/bin' directory:",
        get_files_info("calculator", "/bin"),
    )
    _print_case(
        'get_files_info("calculator", "../"):',
        "Result for '../' directory:",
        get_files_info("calculator", "../"),
    )
