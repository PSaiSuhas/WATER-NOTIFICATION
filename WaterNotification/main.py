import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water Now ",
            message = "According to studies on an average a man should have a daily fluid intake of 15.5 cups that is 3.7 liters of fluid every day.",
            app_icon = "D:/3rd year II sem/WaterNotification/image.ico.ico",
            timeout = 6
        )
        time.sleep(6) 