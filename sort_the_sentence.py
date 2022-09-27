class Solution:
    def sortSentence(self, s: str) -> str:
        splitted_string = s.split()

        for i in range(0, len(splitted_string)):
            length_of_string = len(splitted_string[i])
            one_string = splitted_string[i]
            last_number = one_string[length_of_string-1]
            min_num = last_number
            for j in range(i+1, len(splitted_string)):
                len_of_str = len(splitted_string[j])
                one_str = splitted_string[j]
                last_num = one_str[len_of_str-1]
                if(min_num > last_num):
                    min_num = last_num
                    temp = splitted_string[i]
                    splitted_string[i] = splitted_string[j]
                    splitted_string[j] = temp

        final_string = " ".join(str(x.rstrip(x[-1])) for x in splitted_string)
        return final_string
