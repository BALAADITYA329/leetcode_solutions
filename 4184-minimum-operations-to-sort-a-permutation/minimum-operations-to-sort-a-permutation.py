class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        rev = nums[::-1]

        if nums == list(range(n)):
            return 0

        target = [False] * (2 * n)

        for orientation, arr in enumerate([nums, rev]):
            p = arr.index(0)

            if all(arr[(p + i) % n] == i for i in range(n)):
                target[orientation * n + p] = True

        dist = [-1] * (2 * n)
        queue = [0]
        dist[0] = 0
        head = 0

        while head < len(queue):
            state = queue[head]
            head += 1

            if target[state]:
                return dist[state]

            orientation = state // n
            pos = state % n

            # Rotate left by one
            nxt = orientation * n + (pos + 1) % n

            if dist[nxt] == -1:
                dist[nxt] = dist[state] + 1
                queue.append(nxt)

            # Reverse the entire array
            nxt_orientation = 1 - orientation
            nxt_pos = (-pos) % n
            nxt = nxt_orientation * n + nxt_pos

            if dist[nxt] == -1:
                dist[nxt] = dist[state] + 1
                queue.append(nxt)

        return -1