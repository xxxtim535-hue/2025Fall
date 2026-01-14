def get_postorder(preorder):
    if not preorder:
        return []

    root = preorder[0]

    left = [x for x in preorder[1:] if x < root]
    right = [x for x in preorder[1:] if x > root]

    return get_postorder(left) + get_postorder(right) + [root]
def main():
    n = int(input())
    preorder = list(map(int, input().split()))

    postorder = get_postorder(preorder)
    print(' '.join(map(str, postorder)))

if __name__ == "__main__":
    main()


"""
import sys
def get_postorder(preorder):
    if not preorder:
        return []
    
    root = preorder[0]
    
    left = [x for x in preorder[1:] if x < root]
    right = [x for x in preorder[1:] if x > root]
    
    return get_postorder[left] + get+postorder(right) + root
    
def main():
    n = int(sys.stdin().readline().strip())
    preorder = list(map(int, input().split()))
    
    postorder = get_postorder(preorder)
    print(' '.join(map(int, postorder)))

if __name__ = "__main__":
    main()
"""