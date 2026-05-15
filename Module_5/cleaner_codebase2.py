from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
import json

# ========== STRATEGY PATTERN ==========
# Define a family of algorithms for different notification types
class NotificationStrategy(ABC):
    """Abstract base class for notification strategies"""
    
    @abstractmethod
    def validate(self, recipient: str) -> bool:
        pass
    
    @abstractmethod
    def format_message(self, message: str) -> str:
        pass
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

class EmailNotification(NotificationStrategy):
    """Concrete strategy for email notifications"""
    
    def validate(self, recipient: str) -> bool:
        return "@" in recipient and "." in recipient.split("@")[-1]
    
    def format_message(self, message: str) -> str:
        return f"Dear User,\n\n{message}\n\nBest regards,\nOur Team"
    
    def send(self, recipient: str, message: str) -> bool:
        formatted_message = self.format_message(message)
        print(f"Sending email to {recipient}: {formatted_message[:50]}...")
        return True

class SMSNotification(NotificationStrategy):
    """Concrete strategy for SMS notifications"""
    
    def validate(self, recipient: str) -> bool:
        return len(recipient) == 10 and recipient.isdigit()
    
    def format_message(self, message: str) -> str:
        return f"Alert: {message}"
    
    def send(self, recipient: str, message: str) -> bool:
        formatted_message = self.format_message(message)
        print(f"Sending SMS to {recipient}: {formatted_message}")
        return True

class PushNotification(NotificationStrategy):
    """Concrete strategy for push notifications"""
    
    def validate(self, recipient: str) -> bool:
        return recipient.startswith("device_")
    
    def format_message(self, message: str) -> str:
        return message.upper()
    
    def send(self, recipient: str, message: str) -> bool:
        formatted_message = self.format_message(message)
        print(f"Sending push to {recipient}: {formatted_message}")
        return True

# ========== FACTORY PATTERN ==========
class NotificationFactory:
    """Factory for creating notification strategies"""
    
    _strategies = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification
    }
    
    @classmethod
    def create_strategy(cls, notification_type: str) -> NotificationStrategy:
        """Factory method to create notification strategies"""
        strategy_class = cls._strategies.get(notification_type.lower())
        if not strategy_class:
            raise ValueError(f"Unknown notification type: {notification_type}")
        return strategy_class()
    
    @classmethod
    def create_strategy_from_recipient(cls, recipient: str) -> NotificationStrategy:
        """Factory method that determines strategy from recipient"""
        if "@" in recipient:
            return EmailNotification()
        elif recipient.isdigit() and len(recipient) == 10:
            return SMSNotification()
        elif recipient.startswith("device_"):
            return PushNotification()
        else:
            raise ValueError(f"Cannot determine notification type for: {recipient}")

# ========== OBSERVER PATTERN ==========
class NotificationObserver(ABC):
    """Observer interface for notification events"""
    
    @abstractmethod
    def update(self, event: str, data: dict):
        pass

class Logger(NotificationObserver):
    """Concrete observer for logging"""
    
    def __init__(self):
        self.logs: List[str] = []
    
    def update(self, event: str, data: dict):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {event}: {json.dumps(data)}"
        self.logs.append(log_entry)
    
    def get_logs(self) -> List[str]:
        return self.logs.copy()
    
    def print_logs(self):
        for log in self.logs:
            print(log)

class AnalyticsTracker(NotificationObserver):
    """Concrete observer for analytics tracking"""
    
    def __init__(self):
        self.metrics = {
            "emails_sent": 0,
            "sms_sent": 0,
            "pushes_sent": 0,
            "failed_attempts": 0
        }
    
    def update(self, event: str, data: dict):
        if event == "notification_sent":
            notification_type = data.get("type", "unknown")
            if notification_type in self.metrics:
                self.metrics[f"{notification_type}s_sent"] += 1
        elif event == "notification_failed":
            self.metrics["failed_attempts"] += 1
    
    def get_metrics(self) -> dict:
        return self.metrics.copy()

# ========== SINGLETON PATTERN ==========
class NotificationManager:
    """Main notification manager using Singleton pattern"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        self._observers: List[NotificationObserver] = []
        self._factory = NotificationFactory()
        self._logger = Logger()
        self._analytics = AnalyticsTracker()
        
        # Register default observers
        self.register_observer(self._logger)
        self.register_observer(self._analytics)
        
        self._initialized = True
    
    def register_observer(self, observer: NotificationObserver):
        self._observers.append(observer)
    
    def notify_observers(self, event: str, data: dict):
        for observer in self._observers:
            observer.update(event, data)
    
    def send_notification(self, recipient: str, message: str, 
                         notification_type: Optional[str] = None) -> bool:
        """Send a notification using the appropriate strategy"""
        try:
            # Create strategy using factory
            if notification_type:
                strategy = self._factory.create_strategy(notification_type)
            else:
                strategy = self._factory.create_strategy_from_recipient(recipient)
            
            # Validate recipient
            if not strategy.validate(recipient):
                self.notify_observers("validation_failed", {
                    "recipient": recipient,
                    "type": notification_type or "auto"
                })
                return False
            
            # Send notification
            success = strategy.send(recipient, message)
            
            if success:
                self.notify_observers("notification_sent", {
                    "recipient": recipient,
                    "type": strategy.__class__.__name__.replace("Notification", "").lower(),
                    "message_length": len(message)
                })
            else:
                self.notify_observers("notification_failed", {
                    "recipient": recipient
                })
            
            return success
            
        except ValueError as e:
            self.notify_observers("error", {"error": str(e)})
            return False
    
    def broadcast(self, recipients: List[str], message: str,
                 notification_type: Optional[str] = None) -> List[bool]:
        """Send notification to multiple recipients"""
        results = []
        for recipient in recipients:
            result = self.send_notification(recipient, message, notification_type)
            results.append(result)
        return results
    
    def get_logs(self) -> List[str]:
        return self._logger.get_logs()
    
    def get_analytics(self) -> dict:
        return self._analytics.get_metrics()

# ========== FACADE PATTERN ==========
class NotificationService:
    """Facade for simplified notification operations"""
    
    @staticmethod
    def send(target: str, message: str, urgent: bool = False) -> bool:
        """Simplified notification sending with urgency support"""
        manager = NotificationManager()
        
        # Enhance message if urgent
        enhanced_message = f"URGENT: {message}" if urgent else message
        
        return manager.send_notification(target, enhanced_message)
    
    @staticmethod
    def get_service_summary() -> dict:
        """Get summary of notification service activity"""
        manager = NotificationManager()
        return {
            "logs_count": len(manager.get_logs()),
            "analytics": manager.get_analytics()
        }

# ========== USAGE EXAMPLE ==========
if __name__ == "__main__":
    print("=== CLEAN NOTIFICATION SYSTEM ===\n")
    
    # Get singleton instance
    manager = NotificationManager()
    
    # Send notifications using strategy pattern
    print("1. Sending individual notifications:")
    manager.send_notification("alice@example.com", "Welcome to our service!")
    manager.send_notification("1234567890", "Your verification code is 1234")
    manager.send_notification("device_001", "New update available")
    
    # Broadcast to multiple recipients
    print("\n2. Broadcasting to recipients:")
    recipients = ["bob@example.com", "0987654321", "device_002"]
    results = manager.broadcast(recipients, "System maintenance scheduled")
    print(f"Successfully sent to {sum(results)} out of {len(recipients)} recipients")
    
    # Use facade for simple operations
    print("\n3. Using facade for quick notifications:")
    NotificationService.send("charlie@example.com", "Reminder: Meeting tomorrow", urgent=True)
    
    # Get analytics
    print("\n4. Service Analytics:")
    analytics = manager.get_analytics()
    for metric, value in analytics.items():
        print(f"  {metric}: {value}")
    
    # Verify singleton pattern
    print("\n5. Verifying Singleton pattern:")
    manager2 = NotificationManager()
    print(f"  Are both references the same instance? {manager is manager2}")
    
    # Show service summary using facade
    print("\n6. Service Summary:")
    summary = NotificationService.get_service_summary()
    print(f"  Total logs: {summary['logs_count']}")
    print(f"  Analytics: {summary['analytics']}")
