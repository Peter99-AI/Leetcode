"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 1:
            result = ""
            str = strs[0]
            for i in range(len(str)):
                for st in strs[1:]:
                    try :
                        if str[i] != st[i]:
                            return result
                    except:
                        return result
                result = result + str[i]
            else :
               return result 
            
        else :
            return strs[0]

    def best_LongestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shost = min(strs,key=len)
        for i, ch in enumerate(shost):
            for other in strs:
                if other[i] != ch:
                    return shost[:i]
        return shost

s = Solution()
strs = ["flower","flow","flight"]
print(s.best_LongestCommonPrefix(strs))

