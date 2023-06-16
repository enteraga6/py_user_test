py_binary(
    name = "hello",
    srcs = ["hello.py"],
)

py_binary(
    name = "fib",
    srcs = ["fib.py"],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        ":hello",
        ":fib",
    ],
)
