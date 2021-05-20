import timeit

test_code = '''
class Solution:
    def isValid(self, s: str):
        open = tuple('({[')
        close = tuple(')}]')
        legend = dict(zip(open, close))

        queue = []

        for bracket in s:
            if bracket in open:
                queue.append(legend[bracket])
            elif bracket in close:
                if not queue or bracket != queue.pop():
                    return False
        
        if not queue:
            return True
        
        return False


ret = Solution().isValid('[{}]')

'''

print(timeit.timeit(stmt=test_code, number=1))
