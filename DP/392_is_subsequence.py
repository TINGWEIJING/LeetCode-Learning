class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        s_ind = 0
        t_ind = 0
        while t_ind < len(t):
            # print(f's_ind: {s_ind}')
            # print(f't_ind: {t_ind}\n')
            if s[s_ind] == t[t_ind]:
                s_ind += 1
                if s_ind == len(s):
                    return True
            t_ind += 1

        return s_ind == len(s)


if __name__ == "__main__":
    input_list = [
        # ['abc', 'ahbgdc'],
        # ['axc', 'ahbgdc'],
        ['b', 'abc'],
    ]
    sol = Solution()
    for input_data in input_list:
        s, t = input_data
        print(sol.isSubsequence(s=s, t=t))
