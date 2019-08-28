import ais.stream
with open("testset(copy).txt") as f:
    for msg in ais.stream.decode(f):
        print ('Vessel AIS Information \n\tMMSI = ' , msg['mmsi'])
        print ("\n\n")
