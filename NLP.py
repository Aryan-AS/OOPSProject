import requests



class NLPapp:
    def __init__(self):
        self.__database = {}
        self.__first_menu()
    def __first_menu(self):
        first_input = input("""Hello! How would you like to proceed?
              1. Not a member? Register
              2. Already a member? Log in
              3. Exit
              """)
        if first_input =="1":
          self.__register()
        elif first_input=="2":
          self.__login()
        else:
           exit()
    def __second_menu(self):
        second_input = input("""Hello! How would you like to proceed?
              1. Grammar Check
              2. Language Detection
              3. Sentiment Analysis
              4. Paraphrase 
              5. Entities Extraction
              6. Exit
              """)
        if second_input=="1":
         self.__ner()
        elif second_input == "2":
           self.__language_detection()
        elif second_input =="3":
           self.__sentiment_anaylysis()
        elif second_input=="4":
           self.__paraphrase_tool()
        elif second_input=="5":
           self.__extraction()
        else:
           exit()

    def __register(self):
        name = input("Enter Name:\t")
        email = input("Enter Email:\t")
        password = input("Enter Password:\t")
        if email in self.__database:
           print("Email already exists! Please log in")
           self.__login()
        else:
           self.__database[email]= [name,password]
           print("Congratulations! Your registeration is succesfful")
           self.__first_menu()

           
    def __login(self):
        email = input("Enter your email:\t")
        password = input("Enter your password:\t")
        if email in self.__database:
           if self.__database[email][1]==password:
              print("LOGIN SUCCESSFUL!")
              self.__second_menu()
           else:
              print("ERROR: INCORRECT PASSWORD")
              self.__login()
        else:
           print("ERROR: This email is not registered. Please register yourself with us")
           self.__first_menu()
    def __ner(self):
       para = input("Enter your text\t")
       

       url = "https://grammar-genius.p.rapidapi.com/dev/grammar/"
       
       payload = {"text": para}
 
       headers = {
       	"content-type": "application/json",
       	"X-RapidAPI-Key": "e595913211msh89f5988df939177p1a0427jsn8076c2e4d727",
       	"X-RapidAPI-Host": "grammar-genius.p.rapidapi.com"
       }
       
       response = requests.post(url, json=payload, headers=headers)
       if response.ok:
        print("NER results:", response.json())
       else:
        print("Error:", response.status_code, response.text)
       
       print(response.json())       
    def __language_detection(self):
       para = input("Enter your text\n")
      
       url = "https://language-detection4.p.rapidapi.com/language-detection"
       
       payload = [
       	{
       		 "id": "1",
       		"language": "en",
       		 "text": para
       	}
       ]
       headers = {
       	"content-type": "application/json",
       	"Accept": "application/json",
       	"X-RapidAPI-Key": "e595913211msh89f5988df939177p1a0427jsn8076c2e4d727",
       	"X-RapidAPI-Host": "language-detection4.p.rapidapi.com"
       }
       
       response = requests.post(url, json=payload, headers=headers)
       
       print(response.json())
    def __sentiment_anaylysis(self):
       para = input("Enter the paragraph\t")
          
       url = "https://sentiment-analysis9.p.rapidapi.com/sentiment"
       
       payload = [
       	{
       		"id": "1",
       		"language": "en",
       		"text": para
       	}
       ]
       headers = {
       	"content-type": "application/json",
       	"Accept": "application/json",
       	"X-RapidAPI-Key": "e595913211msh89f5988df939177p1a0427jsn8076c2e4d727",
       	"X-RapidAPI-Host": "sentiment-analysis9.p.rapidapi.com"
       }
       
       response = requests.post(url, json=payload, headers=headers)
       
       print(response.json())
    def __paraphrase_tool(self):
       para = input("Enter your text\t")
       url = "https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/"

       payload = {
       	"text": para,
       	"result_type": "multiple"
       }
       headers = {
       	"content-type": "application/json",
       	"X-RapidAPI-Key": "e595913211msh89f5988df939177p1a0427jsn8076c2e4d727",
       	"X-RapidAPI-Host": "paraphrase-genius.p.rapidapi.com"
       }
       response = requests.post(url, json=payload, headers=headers)

       print(response.json())
    def __extraction(self):
       para = input("Enter your text\t")
       url = "https://ai-textraction.p.rapidapi.com/textraction"

       payload = {
       	"text": para,
       	"entities": [
       		{
       			"var_name": "first_name",
       			"type": "string",
       			"description": "first name of the person"
       		},
       		{
       			"var_name": "last_name",
       			"type": "string",
       			"description": "last name of the person"
       		},
       		{
       			"var_name": "years_of_experience",
       			"type": "integer",
       			"description": "years of experience"
       		},
       		{
       			"var_name": "programming_languages",
       			"type": "array[string]",
       			"description": "programming languages experienced with"
       		},
       		{
       			"var_name": "hobbies",
       			"type": "array[string]",
       			"description": "hobbies"
       		}
       	]
       }
       headers = {
       	"content-type": "application/json",
       	"X-RapidAPI-Key": "e595913211msh89f5988df939177p1a0427jsn8076c2e4d727",
       	"X-RapidAPI-Host": "ai-textraction.p.rapidapi.com"
       }
       
       response = requests.post(url, json=payload, headers=headers)
       
       print(response.json())
          

meow = NLPapp()


