from dhooks import Webhook, Embed
from datetime import datetime

def send():
    hook = Webhook('https://REDACTED_WEBHOOK')

    embed = Embed(
        color=0x5CDBF0,
        timestamp='now'  # sets the timestamp to current time
        )

    image1 = 'https://i.imgur.com/CincZKI.jpg'

    timestamp = datetime.now().strftime("%H:%M:%S.%f %p")

    embed.set_author(name='Successful Reservation!')
    embed.add_field(name=':gem: Item', value='N/A')
    embed.add_field(name=':robot: Task', value='main')
    embed.add_field(name=':busts_in_silhouette: Account', value='main')
    embed.add_field(name=':clock1: Time', value=timestamp)
    embed.set_footer(text='VeVe Bot by feeniks#8412', icon_url=image1)

    hook.send(embed=embed)