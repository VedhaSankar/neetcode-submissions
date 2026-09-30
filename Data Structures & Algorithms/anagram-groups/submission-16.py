class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin = []
        cur_len = len(strs)

        # for i in range(cur_len):
        #     print("iteration i", i)

        #     temp_dict_a = {}
        #     sim = [strs[i]]

        #     for character in strs[i]:
        #         temp_dict_a[character] = temp_dict_a.get(character, 0)

        #     for j in range(i + 1, cur_len):
        #         print("iteration j", j)
        #         print(strs)
        #         print(cur_len)

        #         temp_dict_b = {}

        #         if len(strs[i]) == len(strs[j - 1]):
        #             for character in strs[j]:
        #                 temp_dict_b[character] = temp_dict_b.get(character, 0)
        #             if temp_dict_a == temp_dict_b:
        #                 sim.append(strs[j])
        #                 print("removing ", strs[j])
        #                 strs.remove(strs[j])

        #             fin.append(sim)

        #         cur_len = len(strs)

        #     strs.remove(strs[i])
        #     cur_len = len(strs)
        #     print("sim ", fin)

        return fin
