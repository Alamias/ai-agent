from functions.write_file import write_file


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
        'write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):',
        "Result for 'lorem.txt' file:",
        write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    )
    _print_case(
        'write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):',
        "Result for 'morelorem.txt' file:",
        write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    )
    _print_case(
        'write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):',
        "Result for '/tmp/temp.txt' file:",
        write_file("calculator", "/tmp/temp.txt", "this should not be allowed"),
    )
