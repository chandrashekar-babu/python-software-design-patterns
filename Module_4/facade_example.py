class Projector:
    def on(self): print("Projector: Warming up...")
    def set_input(self, source): print(f"Projector: Setting input to {source}")
    def off(self): print("Projector: Cooling down...")

class Amplifier:
    def on(self): print("Amp: Powering on...")
    def set_volume(self, level): print(f"Amp: Volume set to {level}")
    def off(self): print("Amp: Shutting down...")

class SmartLights:
    def dim(self): print("Lights: Dimming for the show...")
    def brighten(self): print("Lights: Turning back up.")

class StreamingApp:
    def login(self): print("App: Authenticating user...")
    def play(self, movie): print(f"App: Now streaming '{movie}'")
    def logout(self): print("App: Logging out.")

class HomeTheaterFacade:
    def __init__(self):
        self.amp = Amplifier()
        self.projector = Projector()
        self.lights = SmartLights()
        self.app = StreamingApp()
        
    def watch_movie(self, movie_title):  # The actual facade method
        print("\n--- Getting ready for the movie! ---")
        self.lights.dim()
        self.projector.on()
        self.projector.set_input("Streaming Box")
        self.amp.on()
        self.amp.set_volume(15)
        self.app.login()
        self.app.play(movie_title)
        print("--- Enjoy your film! ---\n")

    def end_movie(self):
        print("\n--- Shutting down theater... ---")
        self.app.logout()
        self.amp.off()
        self.projector.off()
        self.lights.brighten()
        print("Theater is off.")
    