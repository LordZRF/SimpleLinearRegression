def gradient_for_c(X, y, m, c):
    ans = 0
    for i in range(len(X)):
        ans += (y[i] - (m * x[i] + c))
    ans = (-2/len(X)) * ans
    return ans

def gradient_for_m(X, y, m, c):
    ans = 0
    for i in range(len(X)):
        ans += x[i] * (y[i] - (m * x[i] + c))
    ans = (-2/len(X)) * ans
    return ans

def one_step_gradient_descent(X, y, m, c, L):
    m_gradient = gradient_for_m(X, y, m, c)
    c_gradient = gradient_for_c(X, y, m, c)
    new_m = m - (L * m_gradient)
    new_c = c - (L * c_gradient)
    return [new_m, new_c]

def gradient_descent(X, y, L, epochs):
    m = 0
    c = 0
    for i in range(epochs):
        m, c = one_step_gradient_descent(X, y, m, c, L)
    return [m, c]