import os.path
import subprocess


def test_clang_tidy(tmp_path):
    test_input = os.path.join(os.path.dirname(__file__), "testcase.cc")
    expected_output = (
        f"{test_input}:2:9: warning: unused variable 'answer' [clang-diagnostic-unused-variable]\n"
        "    int answer = 42;\n"
        "        ^\n"
    )

    output = subprocess.check_output(["clang-tidy", test_input], encoding="utf-8")
    assert output == expected_output
