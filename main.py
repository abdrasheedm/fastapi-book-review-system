import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    # Run FastAPI application using uvicorn
    uvicorn.run("fast_api_book_review_system.main:app", port = 9000, reload = True)