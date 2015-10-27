import requests
import sys
import collections

def pi_digit_count(exclude_before_decimal=True):
    total_digits = 0
    no_dict = collections.OrderedDict()
    no_dict["0"] = 0
    no_dict["1"] = 0
    no_dict["2"] = 0
    no_dict["3"] = 0
    no_dict["4"] = 0
    no_dict["5"] = 0
    no_dict["6"] = 0
    no_dict["7"] = 0
    no_dict["8"] = 0
    no_dict["9"] = 0
    url = "https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt"
    r = requests.get(url, stream=True)
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            for item in str(chunk):
                try:
                   varn = int(item)
                   if varn == 0:
                       no_dict["0"] = no_dict["0"] + 1
                       total_digits = total_digits + 1
                   elif varn == 1:
                       no_dict["1"] = no_dict["1"] + 1
                       total_digits = total_digits + 1
                   elif varn == 2:
                       no_dict["2"] = no_dict["2"] + 1
                       total_digits = total_digits + 1
                   elif varn == 3:
                       no_dict["3"] = no_dict["3"] + 1
                       total_digits = total_digits + 1
                   elif varn == 4:
                       no_dict["4"] = no_dict["4"] + 1
                       total_digits = total_digits + 1
                   elif varn == 5:
                       no_dict["5"] = no_dict["5"] + 1
                       total_digits = total_digits + 1
                   elif varn == 6:
                       no_dict["6"] = no_dict["6"] + 1
                       total_digits = total_digits + 1
                   elif varn == 7:
                       no_dict["7"] = no_dict["7"] + 1
                       total_digits = total_digits + 1
                   elif varn == 8:
                       no_dict["8"] = no_dict["8"] + 1
                       total_digits = total_digits + 1
                   elif varn == 9:
                       no_dict["9"] = no_dict["9"] + 1
                       total_digits = total_digits + 1
                except ValueError:
                    pass
    if exclude_before_decimal:
        no_dict["3"] = no_dict["3"] - 1
        total_digits = total_digits - 1
    print("Count of All: " + str(no_dict))
    print("Total Digits Counted: " + str(total_digits))
    print("Percentages: ")
    for key, value in no_dict.items():
        print(str(key))
        print(str((value / total_digits) * 100))
        print("\n")
    with open("pi_stats.txt", 'w+') as openFile:
        write_string = ""
        write_string = write_string + str(total_digits) + "\n"
        write_string = write_string + str(no_dict) + "\n"
        openFile.write(write_string)

pi_digit_count()
