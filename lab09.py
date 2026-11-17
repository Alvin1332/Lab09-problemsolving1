# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range (len(nums)):
        for j in range( i+1, len (nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    pass


def max_profit(prices):
    # Outline:
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.

    maxprofit = 0

    for i in range (len(prices)):
        for j in range (i+1, len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]

                if profit > maxprofit:
                    maxprofit = profit
    return maxprofit
    pass


def max_subarray(nums):
    # Outline:
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.

    max_sum = nums[0]

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
    pass


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    stack = []

    # Store each closing bracket with its matching opening bracket.
    pairs = {')': '(', ']': '[', '}': '{'}

    # Go through each character in the string.
    for char in s:

        # If it is an opening bracket, add it to the stack.
        if char in "([{":
            stack.append(char)

        # If it is a closing bracket, check for a match.
        elif char in pairs:

            # Return False if there's no opening bracket to match.
            if not stack:
                return False

            # Remove the most recent opening bracket.
            opening = stack.pop()

            # Check whether the opening and closing brackets match.
            if opening != pairs[char]:
                return False

    # Return True only if no unmatched opening brackets remain.
    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
