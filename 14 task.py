class ReportGenerator:
    """Відповідає лише за створення звіту"""
    def generate_report(self):
        return "This is the report content."


class FileManager:
    """Відповідає лише за збереження звіту у файл"""
    def save_to_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Report saved to {filename}")


class EmailSender:
    """Відповідає лише за відправлення звіту на email"""
    def send_email(self, email, content):
        print(f"Sending report to {email}")
        # Імітація відправки email
        print(f"Email sent to {email} with content: {content}")


# Головна частина програми
if __name__ == "__main__":
    # Створюємо звіт
    report_generator = ReportGenerator()
    report_content = report_generator.generate_report()

    # Зберігаємо звіт у файл
    file_manager = FileManager()
    file_manager.save_to_file("report.txt", report_content)

    # Відправляємо звіт на email
    email_sender = EmailSender()
    email_sender.send_email("example@example.com", report_content)
