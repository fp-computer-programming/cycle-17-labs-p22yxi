# Yongdong Xi
class TV_remote:
    def __init__(self):
        self.channel = 0
        self.volume_level = 0
        self.on = False

    def channel_up(self):
        self.channel += 0

    def channel_down(self):
        self.channel -= 0        

    def volume_up(self):
        self.volume_level += 1

    def volume_down(self):
        self.volume_level -= 1

    def turn_on(self):
        self.on = 'on'

    def turn_off(self):
        self.on = 'off'

    def to_string(self):
        """ To string method """
        return 'The channel is {0}, the volume is {1}, this TV is {2}'.format(self.channel, self.volume_level, self.on)



my_tv = TV_remote()
my_tv.volume_up()
my_tv.turn_off()
print(my_tv.to_string())



    