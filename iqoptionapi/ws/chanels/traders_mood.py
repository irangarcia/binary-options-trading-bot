import datetime
import time
from iqoptionapi.ws.chanels.base import Base


class Traders_mood_subscribe(Base):
   
    name = "subscribeMessage"

    def __call__(self,active):
       
         
        data = {
            "name": "traders-mood-changed",
            "params":
                    {
                    "routingFilters":
                                    {
                                        "instrument":"turbo-option",
                                        "asset_id":active
                                    }
                    }

        }

        self.send_websocket_request(self.name, data)

class Traders_mood_unsubscribe(Base):
   
    name = "unsubscribeMessage"

    def __call__(self,active):
       
         
        data = {
            "name": "traders-mood-changed",
            "params":
                    {
                    "routingFilters":
                                    {
                                        "instrument":"turbo-option",
                                        "asset_id":active
                                    }
                    }

        }

        self.send_websocket_request(self.name, data)

