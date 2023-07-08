import urllib.request
from datetime import datetime

polrschdURL = "https://noaasis.noaa.gov/cemscs/polrschd.txt"
file = open("GACDumps.md", 'w')

file.write("---\ntitle: GAC Predictor\nicon: fas fa-hourglass\norder: 4\n---\n\n")
file.write("This site contains all currently scheduled NOAA15/18/19 GAC transmissions.\n\n")
file.write("| Type | Time [UTC] | Satellite | Frequency | Polarization | Location |\n")
file.write("| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |\n")

for line in urllib.request.urlopen(polrschdURL):
    text = line.decode('utf-8')
    text = text[:-1]
    date = text[0:17]
    dateParsed = datetime.strptime(date, '%Y/%j/%H:%M:%S')
    satID = text[23:25]

    # Parse Satellite Name
    if(satID == "15"):
        Satellite = "NOAA 15"
    elif(satID == "18"):
        Satellite = "NOAA 18"
    elif(satID == "19"):
        Satellite = "NOAA 19"
    else:
        Satellite = satID

    # Parse Frequency and Polirization
    if "LSB" in text:
        Freq = "1698.0MHz"
        Pol = "RHCP"
    elif "MSB" in text:
        Freq = "1702.5MHz"
        Pol = "LHCP"
    elif "HSB" in text:
        Freq = "1707.0MHz"
        Pol = "RHCP"
    elif "ESB" in text:
        Freq = "2247.5MHz"
        Pol = "RHCP"
    else:
        Freq = "Unknown"
        Pol = "Unknown"

    # Parse Location
    if "SVL" in text:
        Loc = "Svalbard"
    elif "WAL" in text:
        Loc = "Wallops"
    elif "FBK" in text:
        Loc = "Fairbanks"
    else:
        Loc = "Unknown"

    #Is the text line actually anything of interest?
    if "PBK,START,GAC" in text:
        eventType = "Start"
    elif "PBK,END,GAC" in text:
        eventType = "End"
    else:
        eventType = "Unknown"

    if ((eventType == "Start") | (eventType == "End")):
        file.write("| " + eventType + " | " + str(dateParsed) + " | " + Satellite + " | " + Freq + " | " + Pol + " | " + Loc + " |\n")
file.close()