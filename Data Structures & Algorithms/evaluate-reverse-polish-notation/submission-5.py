class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operation= set()
        operation.add("+")
        operation.add("-")
        operation.add("*")
        operation.add("/")


        for el in tokens:
            if el not in operation:
                stack.append(int(el))
            elif el == "+":
                stack[-2] = stack[-2] + stack[-1]
                stack.pop()
            elif el == "-":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()
            elif el == "*":
                stack[-2] = stack[-2] * stack[-1]
                stack.pop()
            elif el == "/":
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()

        return int(stack[-1])