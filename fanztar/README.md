# Mobile Factory API

This is a basic RESTful API for ordering customized mobile devices. It calculates the order's total price based on the components selected.

## How to Run


1. **Clone the respository using this command:**
    ```
    git clone 
    ```

2. **Install Flask using pip in your environment:**
    ```
    pip install Flask
    ```

3. **Run the `app.py` file in your project directory to launch the Flask application:**
    ```
    python3 app.py
    ```

4. **Use the `Invoke-RestMethod` in Windows powershell to test the API Endpoint:**
    ```
    Invoke-RestMethod -Method Post -Uri http://localhost:5000/orders -ContentType "application/json" -Body '{"components": ["I","A","D","F","K"]}'
    ```
   - This should give you a response containing the order information.

5. **Now go to your project directory and run the `test_order.py` file to begin the unit tests:**
    ```
    python3 test_order.py
    ```
    - The output of the test should indicate a 'Pass' or 'Fail'


## Requirements

- Python
- Flask

## Additional Notes

- This project does not rely on any external databases or libraries.


