from alert_service import AlertService


class SMSAlert(AlertService):

    def update(self, message):
        self.send_alert(message)