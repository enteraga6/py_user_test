load("@io_bazel_rules_python//python:defs.bzl", "py_library")

py_library(
    name = "hello_world",
    srcs = ["hello.py"],
)

py_library(
    name = "fibonacci",
    srcs = ["fib.py"],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        ":hello_world",
        ":fibonacci",
    ],
)
