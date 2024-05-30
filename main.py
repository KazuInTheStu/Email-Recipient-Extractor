import os
import subprocess
import imaplib
import email

def save_recipients_to_file(recipients):
    with open("recipients.txt", "w") as f:
        for recipient in recipients:
            f.write(f"{recipient}\n")

    # Sort the file and remove duplicates using sort and uniq commands
    subprocess.run(["sort", "recipients.txt", "-o", "recipients.txt"])
    subprocess.run(["uniq", "recipients.txt", "-u", "-i", "-w", "0", "-o", "recipients.txt"])

def load_cache():
    cache_file = "cache.txt"
    if not os.path.exists(cache_file):
        return set()
    
    with open(cache_file, "r") as f:
        return set(line.strip() for line in f.readlines())

def save_cache(cache):
    cache_file = "cache.txt"
    with open(cache_file, "w") as f:
        for item in cache:
            f.write(f"{item}\n")

def get_recipients_of_sender(username, password, sender_email, cache):
    recipients = set()

    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.select("inbox")

    # Search for emails from the specified sender
    _, email_data = mail.search(None, f'(FROM "{sender_email}")')
    email_ids = email_data[0].split()

    total_emails = len(email_ids)
    processed_emails = 0

    for email_id in email_ids:
        _, data = mail.fetch(email_id, "(BODY.PEEK[HEADER])")
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        receiver_email = email_message["To"]
        
        # Check if the email is not in the cache before adding to recipients
        if receiver_email not in cache:
            recipients.add(receiver_email)

        processed_emails += 1
        print(f"Processed {processed_emails}/{total_emails} emails", end="\r")

    mail.close()
    mail.logout()

    return recipients

# Main function
def main():
    username = "" # Gmail username
    password = "" # Use app passwords since google doesn't allow imap through traditional creds
    sender_email = "" # Replace this with the sender you want to look for

    # Load cache
    cache = load_cache()

    recipients = get_recipients_of_sender(username, password, sender_email, cache)

    # Remove duplicates from the recipients list
    recipients = list(set(recipients))

    save_recipients_to_file(recipients)
    print("\nEmail recipients saved to 'recipients.txt' file.")

    # Update the cache with the new recipients
    cache.update(recipients)
    save_cache(cache)

if __name__ == "__main__":
    main()
