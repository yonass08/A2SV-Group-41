class Solution:
    def compress(self, chars: List[str]) -> int:
        chars += ' '
        left = 0
        compress_end = 0

        for right in range(len(chars)):
            if chars[left] != chars[right]:
                chars[compress_end] = chars[left]
                compress_end += 1

                count = right - left
                if count > 1:
                    str_count = str(count)
                    chars[compress_end: compress_end + len(str_count)] = str_count
                    compress_end += len(str_count)

                left = right
        
        return compress_end
