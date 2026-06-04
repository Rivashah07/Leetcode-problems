#3751. Waviness
class Solution(object):
    def totalWaviness(self, num1, num2):
        result = 0

        for i in range(num1, num2+1):
            if i < 100:
                continue

            number = i

            while number >= 100:
                right = number % 10
                center = (number % 100 - right) / 10
                left = (number % 1000 - center * 10 - right) / 100

                if (center > right and center > left) or (center < right and center < left):
                    result += 1
                
                number /= 10

        return result