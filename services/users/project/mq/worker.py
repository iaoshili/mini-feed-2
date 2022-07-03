import sys
sys.path.append('./')

import json
import traceback
from kafka import KafkaConsumer
from project.api.users.crud import add_to_timeline, get_fans, get_feed_by_id
from project import create_app

app = create_app()

# consumer = KafkaConsumer('sample', bootstrap_servers='kafka:9093')
# for msg in consumer:
#     print(msg)

class FeedFanout:
    def __init__(self):
        self.consumer = KafkaConsumer('feed_fanout', bootstrap_servers='kafka:9093', value_deserializer = lambda v: json.loads(v.decode('ascii')))

    def start(self):
        for msg in self.consumer:
            try:
                v = msg.value
                fan_out(v.get("feed_id"))
                print("success!")
            except Exception as exc:
                print(traceback.format_exc())


def fan_out(feed_id):
    with app.app_context():
        feed = get_feed_by_id(feed_id)
        idol_id = feed.user_id
        fans = get_fans(idol_id)
        for fan in fans:
            add_to_timeline(user_id=fan.id, feed=feed)


if __name__ == '__main__':
    feed_fanout = FeedFanout()
    feed_fanout.start()
