import pygame


class SoundManager:
    def __init__(self):
        # sound settings
        self.soundVolume = 0.5
        self.musicVolume = 0.25
        # Initialize
        pygame.mixer.init()

        self.sounds = {
            'select': pygame.mixer.Sound('assets/sounds/select.wav'),
            'attack': pygame.mixer.Sound('assets/sounds/attack.wav'),
            'start': pygame.mixer.Sound('assets/music/lapland2035gameplay.mp3'),
            'intro': pygame.mixer.Sound('assets/music/lapland_audio.mp3')
        }

        self.music = {
            # Better not forget this as final BG music. Delete file and burn computer before release
            'carnival': 'assets/music/FacelessCarnival.ogg',
            'game': 'assets/music/lapland2035gameplay.mp3',
        }

    def play_sound(self, sound_name):
        self.sounds[sound_name].set_volume(self.soundVolume)
        self.sounds[sound_name].play()

    def play_music(self, music_name):
        pygame.mixer.music.load(self.music[music_name])
        pygame.mixer.music.set_volume(self.musicVolume)
        pygame.mixer.music.play(-1)
