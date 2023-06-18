# Password Manager Application

This project is a Password Manager application built using Python and the Tkinter library. It provides a secure and convenient way to store and manage passwords for various accounts. The application encrypts the passwords and stores them in a JSON file, ensuring the privacy and security of your sensitive information.

## Features

1. Password Storage: Users can securely store and organize their account credentials, including usernames and passwords, for different platforms and services.

2. Password Generator: The application includes a password generator feature that generates strong and random passwords for enhanced security. Users can customize the length and character types included in the generated password.

3. Encryption: The passwords are encrypted using a strong encryption algorithm before being stored in a JSON file. This ensures that even if the file is accessed, the passwords remain unreadable.

4. Search and Sorting: Users can search for specific accounts by name or sort the accounts alphabetically to quickly find the desired entry.

5. Clipboard Management: The application includes a clipboard management feature that automatically clears the copied password from the clipboard after a specified time to prevent unauthorized access.

## Prerequisites

To run the Password Manager application, ensure you have the following:

- Python (version 3.7 or higher) installed on your computer.
- Tkinter library installed. You can install it using the following command:
  ```
  $ pip install tkinter
  ```

## Usage

1. Clone the GitHub repository or download the project files to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to start the Password Manager application:
   ```
   $ python main.py
   ```

4. The application window will open, showing the list of stored accounts.

5. To add a new account, click the "Add Account" button. Enter the account name, username, and password in the respective fields and click "Save" to add the account.

6. To generate a strong password, click the "Generate Password" button. Specify the desired length and select the character types to include in the generated password. Click "Copy" to copy the generated password to the clipboard.

7. To view the password of an account, select the account from the list. The password will be displayed in the "Password" field. Click the "Copy" button to copy the password to the clipboard.

8. To search for a specific account, enter the account name in the search field. The list will be filtered to show only matching accounts.

9. To sort the accounts alphabetically, click the "Sort Accounts" button. The accounts will be rearranged in alphabetical order.

10. The application automatically clears the copied password from the clipboard after a specified time (default is 30 seconds). This ensures the password is not accessible to others if the clipboard is left unattended.

11. To exit the application, click the "Quit" button or close the application window.

## Customization

You can customize the Password Manager application by modifying the code in the `main.py` file. You can change the appearance, add additional features, or enhance the functionality as per your requirements.
