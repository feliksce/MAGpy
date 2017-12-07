def sum(a: int, b: int):
    return int(a + b)

# print possible parametres, here for \sigma_h, eigenvalue (-1)^(k+q) -> (k+q) must be even, program sort out these parametres for this sum to be even

print("k", "q", "sum(k,q)", sep="\t")

for k in range(6):
    for q in range(k + 1):
        if sum(k, q) % 2 == 0:
            print(k, q, sum(k, q), sep="\t")
        else:
            pass
#  TODO do it for every point group
# TODO hardcode every eigenvalue? maybe theres a way to calculate it

class eigenvalue:

    def __init__(self, k, q):
        self.k = k
        self.q = q

    def C1(self):
        return 1

    def Ci(self):
        pass

    def sigma_h(self):
        if sum(self.k, self.q) % 2 == 1: return 1
        else: return 0