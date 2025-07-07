class Spreadsheet:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.sheet = [[0] * cols for _ in range(rows)]
    
    def new(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.sheet = [[0] * cols for _ in range(rows)]

    def set(self, row, col, value):
        self.sheet[row][col] = value
    
    def get(self, row, col):
        return self.sheet[row][col]
    
    def sort_rows_by_column(self, col):
        self.sheet.sort(key=lambda row: row[col])
    
    def sort_columns_by_row(self, row):
        columns_with_values = []
        for col in range(self.cols):
            columns_with_values.append((col, self.sheet[row][col]))

        sorted_columns = sorted(columns_with_values, key=lambda x: x[1])

        sorted_sheet = []
        
        for r in range(self.rows):
            new_row = []
            for col, _ in sorted_columns:
                new_row.append(self.sheet[r][col])
            sorted_sheet.append(new_row)
        self.sheet = sorted_sheet


    

def run_tests():
    tests = [
        # Example from the book
        (lambda s: [
            s.new(3, 3),
            s.set(0, 0, 5),
            s.set(0, 1, 3),
            s.set(0, 2, 8),
            s.set(1, 0, 6),
            s.set(2, 1, 1),
            s.sort_columns_by_row(0),
            s.sort_rows_by_column(1),
            s.get(1, 1)
        ], 5),

        # Edge case - 1x1 spreadsheet
        (lambda s: [
            s.new(1, 1),
            s.set(0, 0, 42),
            s.get(0, 0)
        ], 42),

        # Edge case - sort empty rows
        (lambda s: [
            s.new(3, 2),
            s.sort_rows_by_column(0),
            s.get(0, 0)
        ], 0),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Spreadsheet Tests...\n")

    for i, (operation_fn, expected) in enumerate(tests, 1):
        s = Spreadsheet(0, 0)
        operations = operation_fn(s)
        result = operations[-1]  # Last value is the one to check

        if result == expected:
            status = "✅ PASSED"
            passed += 1
        else:
            status = "❌ FAILED"
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}\n")

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")

run_tests()
