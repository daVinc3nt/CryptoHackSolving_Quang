import math
from math import gcd

# ========== UTILS ==========

def mod_inv(a, m):
    """Tính nghịch đảo modular bằng Extended Euclid."""
    r0, r1, s0, s1 = a, m, 1, 0
    while r1:
        q = r0 // r1
        r0, r1, s0, s1 = r1, r0 - q * r1, s1, s0 - q * s1
    if r0 != 1:
        raise ValueError("Không tồn tại nghịch đảo modular")
    return s0 % m

def prime_factors(n):
    """Phân tích thừa số nguyên tố."""
    out, f = {}, 2
    while f * f <= n:
        while n % f == 0:
            out[f] = out.get(f, 0) + 1
            n //= f
        f += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

# ========== BABY STEP GIANT STEP ==========

def baby_giant(p, g, a):
    """Giải log_a(g) mod p bằng Baby-step Giant-step."""
    m = math.isqrt(p - 1) + 1
    # Baby step
    table = {pow(g, j, p): j for j in range(m)}
    g_m_inv = pow(pow(g, m, p), -1, p)
    val = a
    # Giant step
    for i in range(m):
        if val in table:
            return i * m + table[val]
        val = (val * g_m_inv) % p
    return None

# ========== POHLIG-HELLMAN ==========

def pohlig(p, g, a):
    """Pohlig–Hellman: chia nhỏ theo thừa số nguyên tố."""
    n = p - 1
    factors = prime_factors(n)
    results = []

    for q, e in factors.items():
        mod_qe = q ** e
        g1 = pow(g, n // mod_qe, p)
        a1 = pow(a, n // mod_qe, p)
        x = 0
        for j in range(e):
            t = pow(a1 * pow(pow(g, -x, p), 1, p), n // (q ** (j + 1)), p)
            # tìm k sao cho g1^k = t mod p
            k = next((k for k in range(q) if pow(g1, k, p) == t), None)
            if k is None: return None
            x += k * (q ** j)
        results.append((x, mod_qe))

    # Chinese Remainder Theorem
    total_mod = n
    x = 0
    for r, mod_i in results:
        Ni = total_mod // mod_i
        x += r * Ni * mod_inv(Ni, mod_i)
    return x % total_mod

# ========== POLLARD-RHO ==========

def pollard(p, g, a):
    """Pollard's Rho giải DLP."""
    n = p - 1
    def f(x, alpha, beta):
        case = x % 3
        if case == 0:  # nhóm 1
            return (x * g) % p, (alpha + 1) % n, beta
        elif case == 1:  # nhóm 2
            return (x * a) % p, alpha, (beta + 1) % n
        else:  # nhóm 3
            return (x * x) % p, (2 * alpha) % n, (2 * beta) % n

    x1, a1, b1 = f(1, 0, 0)
    x2, a2, b2 = f(*f(1, 0, 0))
    while x1 != x2:
        x1, a1, b1 = f(x1, a1, b1)
        x2, a2, b2 = f(*f(x2, a2, b2))

    num, den = (a2 - a1) % n, (b1 - b2) % n
    if den == 0:
        return None

    d = gcd(den, n)
    if d == 1:
        return (num * mod_inv(den, n)) % n
    if num % d:  # vô nghiệm
        return None

    n_ = n // d
    x0 = (num // d) * mod_inv(den // d, n_) % n_
    for i in range(d):
        cand = x0 + i * n_
        if pow(g, cand, p) == a:
            return cand
    return None

# ========== MAIN DISPATCH ==========

def discrete_log(p, g, a, method='bsgs'):
    method = method.lower()
    algs = {
        'bsgs': baby_giant,
        'pohlig-hellman': pohlig,
        'pollard-rho': pollard
    }
    if method not in algs:
        raise ValueError("Thuật toán không hợp lệ")
    return algs[method](p, g, a)

# ========== TEST ==========

if __name__ == "__main__":
    p, g, a = 48611, 19, 36904
    for name in ['bsgs', 'pohlig-hellman', 'pollard-rho']:
        ans = discrete_log(p, g, a, name)
        print(f"{name.upper()} ➜ x = {ans}")
