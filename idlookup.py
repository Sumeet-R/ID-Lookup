import time, requests,re
from pyfiglet import Figlet

class idlookup:

    def extractdata(self,rawcombo,searchtype):
        try:
            if searchtype == "fnlm":
                inputData = '"'+rawcombo+'@"'
                self.search(inputData,rawcombo,"no")
                if withyear=='y':
                    for year in range(1980, 2020):
                        inputdatawithyear = '"' + rawcombo + str(year) + "@" + '"'
                        self.search(inputdatawithyear,rawcombo,"no")

            if searchtype == "eml":
                inputData = '"'+rawcombo+'"'
                self.search(inputData, rawcombo, "no")
            if searchtype == "dm":
                inputData = '"@'+rawcombo+'"'
                self.search(inputData, rawcombo, "no")
            if searchtype == "pnum":
                inputData = '"+'+rawcombo+'"'
                self.search(inputData, rawcombo, searchtype)
        except Exception as e:
            print(e)
            pass

    def search(self,squery,rawquery,isphone):
            for i in range(0, int(level), 10):
                time.sleep(3)
                print("\n....................................................................................")
                print("\nSearch on-going. Be patience and do not interrupt...")
                response = requests.get("https://www.google.com/search?q=" + squery + "&start="+str(i))
                if (response.text.__contains__("Make sure that all words are spelled correctly") or response.text.__contains__("No results found")):
                    pass
                if (response.text.__contains__("Our systems have detected unusual traffic")):
                    print("\n Search Engine not allowing your python user-agent and Source IP to communicate. Check after some time when block is uplifted or use VPN to change IP")
                    exit(0)
                else:
                    print("\nWe found some possible sources to look around.")
                    listresults = re.findall("url\?q=(http[0-9a-zA-Z\-\%\/\:\.\_]+)", response.text)
                    for i in listresults:
                        try:
                            if isphone == "pnum":
                                print("\nNow peeping at URL:" + i)
                                listemail = (re.findall("([+0-9]+[- (0)]+[0-9 ]+|[+0-9]+[0-9]+)",requests.get(i, timeout=5).text))
                                for j in listemail:
                                    if str(j).__contains__(rawquery):
                                        if j not in output:
                                            output.append(j)
                                        if i not in links:
                                            links.append(i)
                            else:
                                print("\nNow peeping at URL:" + i)
                                listemail = (re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", requests.get(i,timeout=10).text))
                                if i not in links:
                                    links.append(i)
                                for j in listemail:
                                    if str(j).__contains__(rawquery):
                                        if j not in output:
                                            output.append(j)
                                        if i not in linkstodomain:
                                            linkstodomain.append(i)
                        except Exception as e:
                            pass

if __name__== "__main__":
    banner = Figlet(font='drpepper')
    name = Figlet(font='small')
    output = []
    links = []
    linkstodomain =[]
    obj=idlookup()
    print(banner.renderText("ID-Lookup"))
    print("\t\t\t\t\tBetter know if your emails or phone numbers are exposed!")
    print("\n#########################################################")
    print("\t\t\tAuthor:\tSumeet-R")
    print("###########################################################")
    print("\nHow do you want to perform search:")
    print("1: Search by First and Last Name")
    print("2: Search by Email Address")
    print("3: Search by Domain Name")
    print("4: Search by Phone Number")
    print("5: Search by Self. Press 5 to exit!")
    inputvalue=input("\n>>")
    if inputvalue == "1":
        fn = input("\nEnter First Name:")
        if fn == "" or fn.__contains__(" "):
            print("No First name provided or String contains two words, exiting the program!!!")
            exit(0)
        ln = input("Enter Last Name:")
        if ln == "" or fn.__contains__(" "):
            print("No First name provided or String contains two words, exiting the program!!!")
            exit(0)
        print("\n")
        withyear=input("Do you want to perform search with years? This would take longer time (y/n):")
        level = input("\nWhat level of search you want(10,20,30,40,50?):")
        if str(re.findall("10|20|30|40|50", level)).__contains__("[]"):
            print("Incorrect level provided. Exiting program")
            exit(0)
        print("\nYour search item:\n" + name.renderText((fn + " " + ln)))
        print("\n")
        obj.extractdata(fn+ln,"fnlm")
        obj.extractdata(fn + ln[0],"fnlm")
        obj.extractdata(fn[0] + ln,"fnlm")
        obj.extractdata(fn + '.' + ln,"fnlm")
        obj.extractdata(fn + '.' + ln[0],"fnlm")
        obj.extractdata(fn[0] + '.' + ln,"fnlm")
        obj.extractdata(fn + '_' + ln,"fnlm")
        obj.extractdata(fn + '_' + ln[0],"fnlm")
        obj.extractdata(fn[0] + '_' + ln,"fnlm")
        obj.extractdata(fn + '-' + ln,"fnlm")
        obj.extractdata(fn + '-' + ln[0],"fnlm")
        obj.extractdata(fn[0] + '-' + ln,"fnlm")
        print("\n###################### Possible email accounts related to person "+fn + " " + ln+" found are below ######################\n")
        for i in output:
            print(i)
        print("\n\nand website links where above instances were found:")
        for j in linkstodomain:
            print(j)
        print("\n#######################################################################################################################\n\n")

    if inputvalue == "2":
        em = input("\nEnter Email Address:")
        if str(re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", em)).__contains__("[]"):
            print("No valid email address was inputted, exiting the program!!!")
            exit(0)
        level = input("\nWhat level of search you want(10,20,30,40,50?):")
        if str(re.findall("10|20|30|40|50", level)).__contains__("[]"):
            print("Incorrect level provided. Exiting program")
            exit(0)
        print("\nYour search item:\n" + name.renderText((em)))
        obj.extractdata(em,"eml")
        print("\n########################## Your given email address "+em+" found on below websites ##########################\n")
        for i in links:
            print(i)
        print("\n#############################################################################################################\n\n")

    if inputvalue == "3":
        dm = input("\nEnter Domain:")
        if str(re.findall("[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", dm)).__contains__("[]"):
            print("No valid domain was inputted, exiting the program!!!")
            exit(0)
        level = input("\nWhat level of search you want(10,20,30,40,50?):")
        if str(re.findall("10|20|30|40|50", level)).__contains__("[]"):
            print("Incorrect level provided. Exiting program")
            exit(0)
        print("\nYour search item:\n" + name.renderText((dm)))
        obj.extractdata(dm, "dm")
        print("\n########################## Possible email accounts found related to domain "+dm+ " ##########################\n")
        for i in output:
            print(i)
        print("\nand website links where above instances were found:")
        for j in linkstodomain:
            print(j)
        print("\n#############################################################################################################\n\n")
    if inputvalue == "4":
        cc = input("\nEnter numerical country calling code:")
        if str(re.findall("[0-9]+", cc)).__contains__("[]"):
            print("Incorrect code provided. Exiting program")
            exit(0)
        pn = input("\nEnter 10 digit mobile number:")
        if str(re.findall("[0-9]+", pn)).__contains__("[]"):
            print("Incorrect number provided. Exiting program")
            exit(0)
        level = input("\nWhat level of search you want(10,20,30,40,50?):")
        if str(re.findall("10|20|30|40|50", level)).__contains__("[]"):
            print("Incorrect level provided. Exiting program")
            exit(0)
        print("\nYour search item:\n" + name.renderText(("+"+cc + "-" + pn)))
        obj.extractdata(cc + pn, "pnum")
        obj.extractdata(cc +" "+ pn, "pnum")
        obj.extractdata(cc +"-"+ pn, "pnum")
        print("\n########################## Your given phone number +" + cc+"-"+pn + " found on below websites ##########################\n")
        for i in links:
            print(i)
        print(
            "\n#############################################################################################################\n\n")
    if inputvalue == "5":
        print(name.renderText(("Good Bye :)")))






