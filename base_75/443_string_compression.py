class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        count = 0  # 统计连续字符的个数
        write = 0     # 指向存储压缩后字符串的字符的指针
        for read in range(n):
            count += 1    # 累加
            if read == n - 1 or chars[read] != chars[read+1]:   
                chars[write] = chars[read]     # 先存储当前字符
                write += 1
                if count > 1:      
                    start = write     # 暂存起点，用于反转数字
                    str_t = str(count)  # 先倒序存储count
                    for i in str_t:
                        chars[write] = i
                        write += 1
                count = 0  # 清零重新计算
        return write  # 最终write的位置即为压缩后字符串的长度