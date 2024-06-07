# Phone-number-Tracer
This Python script is a simple tool that provides information about a given phone number. It utilizes the `phonenumbers` module to extract details such as timezone, carrier, and country information associated with the provided phone number.

### Steps to make it run
1. Install the `phonenumbers` module if not already installed:
   ```
   pip install phonenumbers
   ```

2. Run the script and enter the phone number when prompted. Make sure to include the country code (e.g., +254 for Kenya).

3. The script will then display the following details:
   - Parsed phone number
   - Timezone
   - Carrier (if available)
   - Country information

### Example
```
Enter your number (with +254): +254xxxxxxxxx
Details :
PhoneNumber(country_code=254, national_number=xxxxxxxxx)
['Africa/Nairobi']
Safaricom
Kenya
```
