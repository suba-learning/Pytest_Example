# Pytest_Example
# 📚 API Testing with Pytest - OpenLibrary API

This repository contains example API tests written in **Python** using the **Pytest** framework. The tests interact with the [OpenLibrary API](https://openlibrary.org/developers/api) to perform basic search operations and extract information about books and authors.

## 🔧 Technologies Used
- **Python 3**
- **Pytest**
- **Requests**
- **JSON handling**

## 📂 Project Structure
```
├── test_openlibrary_api.py   # Contains the API tests
├── README.md                 # Project documentation
└── requirements.txt          # (Optional) Add required packages here
```

## ✅ Test Cases Overview
The following test cases are covered:
1. **Search Book by Name**  
   - Searches for the book *"The Lord of the Rings"*.
   - Verifies the status code is 200 (OK).

2. **Search Book by Title**
   - Searches for books related to *"API Testing"*.
   - Verifies the status code is 200 (OK).

3. **Extract Author Key**
   - Extracts the author name and author key from the search results.

4. **Search Book by Author**
   - Searches books by the extracted author name.
   - Validates the presence of the correct author key.

5. **Get Author Works**
   - Retrieves detailed information about the author's works using the `author_key`.

## 📌 Notes
- These tests use the **OpenLibrary public API**, which does not require authentication.
- The `extracted_data` dictionary is used to pass data between tests, demonstrating basic data extraction and chaining in API tests.

## 🔥 Improvements for Future
- Add **pytest fixtures** for setup and teardown.
- Use **parameterization** to run tests with multiple inputs.
- Validate response schema using **pydantic** or **jsonschema**.
- Add logging instead of print statements.
- Integrate with CI/CD tools like GitHub Actions.
