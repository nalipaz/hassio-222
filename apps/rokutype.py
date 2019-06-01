import appdaemon.plugins.hass.hassapi as hass

#
# Roku Remote Typing App
#
# Args:
#

class RokuType(hass.Hass):

  def initialize(self):
     self.log("Hello from Roku Remote Typing")
