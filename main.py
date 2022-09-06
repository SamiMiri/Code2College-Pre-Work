import cleverbot


cb = cleverbot.Cleverbot('YOUR_API_KEY', timeout=60)

text = input("Say to Cleverbot: ")
try:
    reply = cb.say(text)
except cleverbot.CleverbotError as error:
    print(error)
else:
    print(reply)
finally:
    cb.close()