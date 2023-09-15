from fastapi import FastAPI

app = FastAPI()

BOOKS = [
  {
    "id": 1,
    "title": "It Ends with Us",
    "author": "Colleen Hoover",
    "price": "₹274"
  },
  {
    "id": 2,
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": "₹551"
  },
  {
    "id": 3,
    "title": "It Starts with Us",
    "author": "Colleen Hoover",
    "price": "₹384"
  },
  {
    "id": 4,
    "title": "The Psychology of Money",
    "author": "Morgan Housel",
    "price": "₹295"
  },
  {
    "id": 5,
    "title": "Ikigai",
    "author": "Francesc Miralles",
    "price": "₹391"
  },
  {
    "id": 6,
    "title": "My First Library: Boxset of 10 Board Books for Kids",
    "author": "Wonder House Books Editorial",
    "price": "₹517"
  },
  {
    "id": 7,
    "title": "Indian Polity For Civil Services and Other State Examinations| 6th Revised Edition",
    "author": "Laxmikanth, M",
    "price": "₹810"
  },
  {
    "id": 8,
    "title": "Bihar Diaries",
    "author": "AMIT LODHA",
    "price": "₹233"
  },
  {
    "id": 9,
    "title": "Life's Amazing Secrets: How to Find Balance and Purpose in your life",
    "author": "Gaur Gopal Das",
    "price": "₹233"
  },
  {
    "id": 10,
    "title": "World’s Greatest Books For Personal Growth \u0026 Wealth (Set of 4 Books) : Perfect Motivational Gift Set",
    "author": "Dale Carnegie, Napoleon Hill, Dr. Joseph Murphy \u0026 George S. Clason",
    "price": "₹482"
  },
  {
    "id": 11,
    "title": "You Can",
    "author": "George Matthew Adams",
    "price": "₹89"
  },
  {
    "id": 12,
    "title": "My First Book of Patterns Pencil Control; Pattern Practice Book for Kids",
    "author": "Wonder House Books Editorial",
    "price": "₹83"
  },
  {
    "id": 13,
    "title": "The Subtle Art of Not Giving a F*ck",
    "author": "Mark Manson",
    "price": "₹358"
  },
  {
    "id": 14,
    "title": "The Power of Your Subconscious Mind",
    "author": "Joseph Murphy",
    "price": "₹1,382"
  },
  {
    "id": 15,
    "title": "Do Epic Shit",
    "author": "Ankur Warikoo",
    "price": "₹293"
  },
  {
    "id": 16,
    "title": "Your Time Will Come",
    "author": "Saranya Umakanthan",
    "price": "₹119"
  },
  {
    "id": 17,
    "title": "My First 4 In 1 Alphabet Numbers Colours Shapes: Padded Board Books",
    "author": "Wonder House Books",
    "price": "₹233"
  },
  {
    "id": 18,
    "title": "Fruits - My First Early Learning Wall Chart: For Preschool, Kindergarten, Nursery And Homeschooling (19 Inches X 29 Inches)",
    "author": "Wonder House Books",
    "price": "₹105"
  },
  {
    "id": 19,
    "title": "Grandma's Bag of Stories",
    "author": "Sudha Murty",
    "price": "₹200"
  },
  {
    "id": 20,
    "title": "Do It Today: Overcome procrastination, improve productivity and achieve more meaningful things",
    "author": "Foroux, Darius",
    "price": "₹119"
  },
  {
    "id": 21,
    "title": "General Knowledge",
    "author": "Lucent Publications",
    "price": "₹309"
  },
  {
    "id": 22,
    "title": "Atlas of Vascular \u0026 Endovascular Surgical",
    "author": "M Ashraf Mansour",
    "price": "₹20,212"
  }
]

@app.get("/books")
def get_all_books():
    return BOOKS


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in BOOKS:
        if book.get("id") == book_id:
            return book