def plusOne(self, digits):
        carry = 0
        nums_rev = digits[::-1]
        prev = 0
        for i in range(len(nums_rev)): #9,9,9
            prev = nums_rev[i]
            if i == 0:
                nums_rev[i] = (prev + 1) % 10


                carry = (prev + 1) // 10
            else:
                if carry == 1:
                    nums_rev[i] = (prev + 1) % 10

                    carry = (prev + carry) // 10

        if carry == 1:
            nums_rev.append(1)
        return nums_rev[::-1]