from collections import deque
import sys用法
def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    index = 1

    group_map = {}
    for group_id in range(1, 1+t):
        members = list(map(int, data[index].split()))
        index += 1
        for member in members:
            group_map[member] = group_id

    group_queues = {}
    mainq = deque()
    result = []

    while index < len(data):
        line = data[index].split()
        index += 1

        if line[0] == "STOP":
            break
        elif line[0] == "ENQUEUE":
            x = int(line[1])
            group_id = group_map.get(x, -1)

            if group_id == -1:
                mainq.append((True, x))
            else:
                if group_id not in group_queues:
                    mainq.append((False, group_id))
                    group_queues[group_id] = deque()
                group_queues[group_id].append(x)
        elif line[0] == "DEQUEUE":
            if not mainq:
                continue

            item_type, iden = mainq[0]
            if item_type:
                mainq.popleft()
                result.append(str(iden))
            else:
                member = group_queues[iden].popleft()
                result.append(str(member))
                if not group_queues[iden]:
                    mainq.popleft()
                    del group_queues[iden]

    print("\n".join(result))

if __name__ =="__main__":
    main()