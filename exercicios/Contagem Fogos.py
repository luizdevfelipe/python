from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('Happy New Year \033[33m:fireworks: :fireworks: :fireworks: :fireworks:'))
