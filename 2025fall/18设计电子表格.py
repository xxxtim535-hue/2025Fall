class Spreadsheet:
    def __init__(self, _):
        self.data = {}

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value

    def resetCell(self, cell: str) -> None:
        self.data.pop(cell, None)

    def getValue(self, formula: str) -> int:
        ans = 0
        for cell in formula[1:].split("+"):
            # 注：如果用 defaultdict(int)，访问 self.data[cell] 也会把 cell 插入哈希表，增加空间复杂度
            ans += self.data.get(cell, 0) if cell[0].isupper() else int(cell)
        return ans

if __name__ == "__main__":
        print("\n--- 手动演示 ---")
        ss = Spreadsheet(5)
        ss.setCell("A1", 100)
        ss.setCell("A2", 200)
        print("A1 + A2 =", ss.getValue("=A1+A2"))  # 输出: 300
        ss.resetCell("A1")
        print("重置 A1 后，A1 + A2 =", ss.getValue("=A1+A2"))