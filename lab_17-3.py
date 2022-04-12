# Yongdong Xi
class TV_remote:
    def __init__(self, channel = 0, volume_level = 0, on = False):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

    def to_string(self):
        """ To string method """
        return 'The channel is {0}, the volume is {1}, this TV is {2}'.format(self.channel, self.volume_level, self.on)



my_tv = TV_remote()
print(my_tv.to_string())



    