def math_operations(*args, **kwargs):
    pos = 1
    kwargs["a"] = kwargs.get("a", 0)
    kwargs["s"] = kwargs.get("s", 0)
    kwargs["d"] = kwargs.get("d", 1)
    kwargs["m"] = kwargs.get("m", 1)

    [(
        kwargs.update({
            "a": kwargs["a"] + num if pos == 1 else kwargs["a"],
            "s": kwargs["s"] - num if pos == 2 else kwargs["s"],
            "d": kwargs["d"] / num if pos == 3 and num != 0 else kwargs["d"],
            "m": kwargs["m"] * num if pos == 4 else kwargs["m"]
        }),
        pos := pos + 1 if pos < 4 else 1
    ) for num in args]

    return "".join([f"{key}: {value:.1f}\n" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))