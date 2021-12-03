def Trap_integr(f, x):
    result = 0
    count = len(x)

    for i in range(count - 1):
        h = (x[i + 1] - x[i])
        result += h * (f[i] + f[i + 1]) / 2

    return result 


def Simpson_integr(f, x):
    result = 0
    count = len(x) // 2

    for i in range(count):
        result += (x[2*(i + 1)] - x[2*i]) * (f[2*i] + 2 * f[2*i+1] + f[2*i+2]) / 3

    return result

x_array_b = [0, 0.25 , 0.5  , 0.75 , 1  , 1.25, 1.5  , 1.75 , 2    ]
y_array_b = [0, 0.028, 0.054, 0.078, 0.1, 0.2 , 0.133, 0.145, 0.154]

print("trap = ", Trap_integr(y_array_b, x_array_b))

x_array_a = [-1, -0.75, -0.5  , -0.25, 0, 0.25 , 0.5  , 0.75  , 1     ]
y_array_a = [-1, -0.14, -0.032, 0.01 , 0, 0.002, 0.003, 0.0031, 0.0029]

print("Simpson gomer = ", Simpson_integr(y_array_a, x_array_a))
