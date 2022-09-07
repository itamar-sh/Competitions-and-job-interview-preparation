class StringHelp:
    # remove all alphanumeric 1
    def remove_all_non_alphanumeric1(self, s: str) -> str:
        return "".join([c for c in s if c.isalnum()])

    # remove all alphanumeric 2
    def remove_all_non_alphanumeric2(self, s: str) -> str:
        return "".join(filter(str.isalnum, s))
    # remove first non alphanumeric 1
    def remove_first_non_alphanumeric(self, s: str) -> str:
        new_str = []
        flag = True
        for c in s:
            if not c.isalnum() and flag:
                flag = False
            else:
                new_str.append(c)
        return "".join(new_str)

    # remove first non alphanumeric 1
    def remove_first_non_alphanumeric2(self, s: str) -> str:
        return s.replace()
