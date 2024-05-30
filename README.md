# Email Recipient Extractor

This Python script is designed to extract email recipients from incoming emails sent by a specific sender. It is particularly useful for individuals using a catchall domain or the Gmail "+" trick to redirect emails to their Gmail inbox. The script connects to a Gmail IMAP server, searches for emails from the specified sender, and extracts the recipient's email addresses. The extracted email addresses are then saved to a text file while ensuring that duplicates are removed.

## Usage

1. **Set Up Gmail Credentials**: Before running the script, make sure to replace the `username` and `password` variables with your Gmail credentials. Also, specify the email address of the sender whose emails you want to analyze.

2. **Run the Script**: Execute the script using a Python interpreter. Ensure that you have the necessary dependencies installed (e.g., `imaplib`, `email`).

3. **Review Output**: Once the script finishes processing emails, it will save the extracted email recipients to a file named `recipients.txt`. You can review this file to see the list of recipients.

## Use Case

This script can be particularly useful for individuals managing multiple accounts or subscriptions using a catchall domain or the Gmail "+" trick. For example, it can help identify which email addresses received a promotional offer from a specific sender. 

## Dependencies

- Python 3.x
- `imaplib`: The IMAP client library for accessing and manipulating email messages on an IMAP server.
- `subprocess`: Used for executing shell commands to sort and remove duplicates from the recipients file.

## Contributing

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
