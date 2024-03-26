import uvicorn

if __name__ == '__main__':
    uvicorn.run("fast_api_book_review_system.main:app", port = 9000, reload = True)