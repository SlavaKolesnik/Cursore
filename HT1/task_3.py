# 3.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports,
# Dynamics And create an HP Laptop class by using your interface.

from abc import ABC, abstractmethod


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        print('Displays an image')

    @abstractmethod
    def keyboard(self):
        print('Receives input from the user')

    @abstractmethod
    def touchpad(self):
        print('Allows you to move the cursor')

    @abstractmethod
    def webcam(self):
        print('Receives video input, and transmits to the PC')

    @abstractmethod
    def ports(self):
        print('Allows you to connect devices and data carriers to the PC')

    @abstractmethod
    def dynamics(self):
        print('Emits sound')


class HPlaptop(Laptop):

    def screen(self):
        print('HP Laptop: 1900x1600')

    def keyboard(self):
        print('HP Laptop: backlit mechanical keyboard')

    def touchpad(self):
        print('HP Laptop: Allows you to move the cursor')

    def webcam(self):
        print('HP Laptop: Receives video input, and transmits to the PC')

    def ports(self):
        print('HP Laptop:  3x USB Type-A, 2x Thunderbolt 4, 1x Mini DisplayPort 1.4, 1x HDMI 2.0b')

    def dynamics(self):
        print('HP Laptop: SuperSens2.0')


hp_laptop = HPlaptop()


hp_laptop.screen()
hp_laptop.keyboard()
hp_laptop.touchpad()
hp_laptop.webcam()
hp_laptop.ports()
hp_laptop.dynamics()
