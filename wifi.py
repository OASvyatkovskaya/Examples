import json


file = open("Святковская.dat", "r")

encodedBitsCounter = 0  # Counter of one encoded bit values (Ranges from 0 to 55)
decodedByteCounter = 0  # Counter of decoded bytes of one letter (Ranges from 0 to 8)
bitsIsEqualToOne = 0  # Counter which check how many bits is 1 in first 15 values (of 55) of encoded bit
resultLetter = 0  # Result letter from 8 decoded byte
Message = ""  # Message from result letters


# Read all values from file
for line in file:
    # check first 15 of 55 encoded bytes
    # If value not negative increase bitsIsEqualToOne
    if encodedBitsCounter < 15 and line[0] != "-":
        bitsIsEqualToOne += 1

    encodedBitsCounter += 1  # Go to next value

    # If we checked all value of encoded bit
    if encodedBitsCounter == 55:
        decodedByteCounter += 1
        # if 7 of 15 bits equals 1, most likely that encoded bit is 1
        if bitsIsEqualToOne >= 7:
            resultLetter += 2 ** (8 - decodedByteCounter)  # Increase letter
        bitsIsEqualToOne = 0
        encodedBitsCounter = 0
        # If we checked 8 decoded bits (or 1 decoded byte)
        if decodedByteCounter == 8:
            Message += chr(resultLetter)  # Adding new letter to string
            decodedByteCounter = 0
            resultLetter = 0
            
data = {"message": Message}
with open('wifi.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
