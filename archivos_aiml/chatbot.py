import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "32241730-7257-11ec-97ce-0db8d4088350ac245361-f807-4bbc-ae8a-6e0e9a0ddc3b"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]

    if confidence < 75:
        print("No entiendo lo que me has dicho. Dime algo más!")
    elif answerclass == "clara":
        print("Y la cerveza con limon la quieres nacional o importada?")
    elif answerclass == "normal":
        print("Y esa cerveza normal la prefieres nacional o importada?")
    elif answerclass == "fuerte":
        print("Y esa cerveza fuerte la prefieres nacional o importada?")
    elif answerclass == "importada":
        print("¡Por supuesto! tenemos los mejores brebajes procedentes de tierras lejanas! Espero que te guste esta sujerencia:")
    elif answerclass == "nacional":
        print("En ese caso, permíteme que te sugiera esta cerveza nacional:")
    elif answerclass == "si":
        print("Te gusta la cerveza clara normal o fuerte?")
    elif answerclass == "no":
        print("Bueno, tu te lo pierdes, pero después no vengas llorando.")

print("¡Bienvenido a birralandia!¿Quieres que te ayude a elegir cerveza?")

while True:
    answer_question()