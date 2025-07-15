class Solution:
    def merge(self, nums1: List[int], m: int,
                    nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 as one sorted array in-place.
        Assumes nums1 has enough space at the end to hold nums2.
        """
        # Pointers for the last elements in the initialized parts
        index1 = m - 1  # Last initialized element in nums1
        index2 = n - 1  # Last element in nums2
        insert_pos = m + n - 1  # Position to insert into nums1 (from the end)

        # Merge in reverse order to avoid overwriting
        while index2 >= 0:
            if index1 >= 0 and nums1[index1] >= nums2[index2]:
                nums1[insert_pos] = nums1[index1]
                index1 -= 1
            else:
                nums1[insert_pos] = nums2[index2]
                index2 -= 1
            insert_pos -= 1
