class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits
        
        digits = digits[::-1]
        carry = 0
        
        digits[0] += 1
        
        for i in range(len(digits)):
            digit = digits[i] + carry
            if digit > 9:
                digit -= 10
                carry = 1
            else:
                carry = 0
            digits[i] = digit
        
        if carry == 1:
            digits.append(1)

        return digits[::-1]