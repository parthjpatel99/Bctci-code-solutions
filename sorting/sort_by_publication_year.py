class Book:
    def __init__(self, title, author, pages, genre, year_published):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.year_published = year_published

def bucket_sort(books):
    if not books:
        return []
    
    min_year = min(book.year_published for book in books)
    max_year = max(book.year_published for book in books)
    buckets = [[] for _ in range(max_year - min_year + 1)]

    for book in books:
        index = book.year_published - min_year
        buckets[index].append(book)
    
    res = []

    for bucket in buckets:
        for book in bucket:
            res.append(book)
    return res

def run_tests():
    tests = [
        # Example from the book
        ([
            Book("Shadow of Tomorrow", "Elliot Greyson", 350, "Science Fiction", 2020),
            Book("Whispers in the Wind", "Lila Hart", 280, "Romance", 2018),
            Book("Echoes of Eternity", "Mara Vance", 420, "Fantasy", 2018),
            Book("Fragments of Dawn", "Cora Blake", 310, "Mystery", 2019),
            Book("Beneath the Starlit Sky", "Aria Monroe", 270, "Drama", 2020)
        ], [2018, 2018, 2019, 2020, 2020]),

        ([], []),
        ([Book("Solo", "Author", 100, "Genre", 2000)], [2000]),
        ([
            Book("A", "Author1", 100, "Genre", 2000),
            Book("B", "Author2", 200, "Genre", 2000),
        ], [2000, 2000]),
        ([
            Book("A", "Author1", 100, "Genre", 2020),
            Book("B", "Author2", 200, "Genre", 2019),
            Book("C", "Author3", 300, "Genre", 2018),
        ], [2018, 2019, 2020]),
        ([
            Book("A", "Author1", 100, "Genre", 2018),
            Book("B", "Author2", 200, "Genre", 2019),
            Book("C", "Author3", 300, "Genre", 2020),
        ], [2018, 2019, 2020]),
        ([Book("A", "Author1", 100, "Genre", 1000)], [1000]),
        ([Book("A", "Author1", 100, "Genre", 3000)], [3000]),
        ([
            Book("A", "Author1", 100, "Genre", 1000),
            Book("B", "Author2", 200, "Genre", 3000),
        ], [1000, 3000]),
        ([Book(f"Book{i}", f"Author{i}", 100, "Genre", 2000) for i in range(10)],
         [2000] * 10),
    ]

    passed = 0
    failed = 0

    print("🔍 Running Bucket Sort Book Tests...\n")

    for i, (books, expected_years) in enumerate(tests, 1):
        got = bucket_sort(books)
        got_years = [book.year_published for book in got]
        input_titles = [b.title for b in books]

        status = "✅ PASSED"
        error = None

        try:
            assert got_years == expected_years, "Year order mismatch"
            assert len(got) == len(books), "Book count mismatch"
            assert set(b.title for b in got) == set(b.title for b in books), "Books were lost or duplicated"
            passed += 1
        except AssertionError as e:
            failed += 1
            status = "❌ FAILED"
            error = str(e)

        print(f"Test {i}: {status}")
        print(f"  Input Titles:   {input_titles}")
        print(f"  Expected Years: {expected_years}")
        print(f"  Got Years:      {got_years}")
        if error:
            print(f"  ⚠️ Error: {error}")
        print()

    print("📊 Summary")
    print(f"  Total:  {len(tests)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")

run_tests()

