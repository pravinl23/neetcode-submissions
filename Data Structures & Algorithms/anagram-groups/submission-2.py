class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            frequency_chart = 26 * [0]
            for char in string:
                index = ord(char) - ord('a')
                frequency_chart[index] += 1
            
            freq = ''.join((str(x) + 'a') for x in frequency_chart)
            if freq in hashmap:
                hashmap[freq].append(string)
            else:
                hashmap[freq] = [string]
    
        outputlist = []
        for item in hashmap:
            outputlist.append(hashmap[item])

        return outputlist



        