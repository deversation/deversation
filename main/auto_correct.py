# Working test of textblob
# https://www.geeksforgeeks.org/spelling-checker-in-python/

from textblob import TextBlob

message = "Hello confsion houes"
print("entered: "+str(message))

corrected = TextBlob(message)

# prints the corrected spelling
print("corrected: "+str(corrected.correct()))
