class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False

        def sametree(s, t):
            if not s and not t:
                return True

            if not s or not t:
                return False

            if s.val != t.val:
                return False

            return sametree(s.left, t.left) and sametree(s.right, t.right)

        if sametree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)