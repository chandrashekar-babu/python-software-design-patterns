class NotificationSystem:
    def __init__(self):
        self.users = []
        self.logs = []
        
    def send_email(self, user, message):
        # Multiple responsibilities in one method
        if "@" not in user:
            print(f"Invalid email: {user}")
            return False
            
        # Business logic mixed with email formatting
        formatted_message = f"Dear User,\n\n{message}\n\nBest regards,\nOur Team"
        
        # Simulate email sending
        print(f"Sending email to {user}: {formatted_message[:50]}...")
        
        # Logging mixed with business logic
        self.logs.append(f"Email sent to {user} at {self.get_current_time()}")
        
        return True
        
    def send_sms(self, user, message):
        # Similar issues as send_email
        if len(user) != 10 or not user.isdigit():
            print(f"Invalid phone: {user}")
            return False
            
        # Different formatting for SMS
        formatted_message = f"Alert: {message}"
        print(f"Sending SMS to {user}: {formatted_message}")
        
        self.logs.append(f"SMS sent to {user} at {self.get_current_time()}")
        
        return True
        
    def send_push(self, user, message):
        # Yet another implementation with same issues
        if not user.startswith("device_"):
            print(f"Invalid device ID: {user}")
            return False
            
        formatted_message = message.upper()  # Push notifications are uppercase
        print(f"Sending push to {user}: {formatted_message}")
        
        self.logs.append(f"Push sent to {user} at {self.get_current_time()}")
        
        return True
        
    def get_current_time(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def send_notification(self, notification_type, user, message):
        # Long if-else chain that violates Open/Closed principle
        if notification_type == "email":
            return self.send_email(user, message)
        elif notification_type == "sms":
            return self.send_sms(user, message)
        elif notification_type == "push":
            return self.send_push(user, message)
        else:
            print(f"Unknown type: {notification_type}")
            return False
            
    def broadcast(self, message, notification_type=None):
        # Hardcoded user list
        users = ["alice@example.com", "1234567890", "device_001", "bob@example.com"]
        
        # Nested conditionals and loops
        results = []
        for user in users:
            if notification_type:
                result = self.send_notification(notification_type, user, message)
            else:
                # Determine type based on user string (bad practice!)
                if "@" in user:
                    result = self.send_notification("email", user, message)
                elif user.isdigit():
                    result = self.send_notification("sms", user, message)
                else:
                    result = self.send_notification("push", user, message)
            results.append(result)
            
        return results
        
    def print_logs(self):
        # Simple method but placed in wrong class
        for log in self.logs:
            print(log)

# Even worse - a global function that does similar things
def quick_notify(target, msg, urgent=False):
    system = NotificationSystem()
    
    # String manipulation to determine type
    if "@" in target:
        ntype = "email"
    elif target.isdigit():
        ntype = "sms"
    else:
        ntype = "push"
        
    # Modify message based on urgency
    if urgent:
        msg = f"URGENT: {msg}"
        
    return system.send_notification(ntype, target, msg)

# Main execution with more mess
if __name__ == "__main__":
    # Creating multiple systems (no singleton pattern)
    system1 = NotificationSystem()
    system2 = NotificationSystem()
    
    # Inconsistent calls
    system1.send_email("test@example.com", "Hello via email")
    system2.send_notification("sms", "1234567890", "Hello via SMS")
    
    # Using the global function
    quick_notify("device_abc", "Quick notification", urgent=True)
    
    # Broadcast with mixed logic
    system1.broadcast("Important announcement!")
    
    # Print logs from different systems
    print("\nSystem 1 logs:")
    system1.print_logs()
