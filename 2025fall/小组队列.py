from collections import deque, defaultdict
import sys
def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0]); ind = 1

    g = {}
    for i in range(1, t+1):
        members = data[ind].split(); ind += 1
        for member in members:
            g[member] = i

    q = deque()
    group_q = defaultdict(deque)

    while len(data) > ind:
        order = data[ind].split();ind+=1

        if order[0] == "ENQUEUE":
            people = order[1]
            _id = g.get(people, -1)

            if _id == -1:
                q.append((True, people))
            else:
                group_q[_id].append(people)
                if len(group_q[_id]) == 1:
                    q.append((False, _id))
        elif order[0] == "STOP":
            break
        else:
            if not q:
                continue
            type, _id = q[0]
            if type:
                q.popleft()
                print(str(_id))
            else:
                member = group_q[_id].popleft()
                print(member)
                if not group_q[_id]:
                    q.popleft()

if __name__ == "__main__":
    main()


