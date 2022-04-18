import json
import ast

from dajavax import sum_state, sum_prob, sum_transit, sums_transit

dell = """
{
    "intents": [
         {
        "tag": "greeting",
        "patterns": [
          "Hi",
          "Hey",
          "How are you",
          "Is anyone there?",
          "Hello",
          "Good day",
          "How's it going?"
        ],
        "responses": [
          "Hello, how can i help you?",
          "Hello, thanks for using my service. How can i help you?",
          "Hi there, what can I do for you?",
          "Hi there, how can I help?"
        ]
      },
       {
        "tag": "states",
        "patterns": [
          "How many states are in my process?", 
          "What is the number of states in my process?",
          "Number of states?"
        ],
        "responses": [
          
        ]
      },
      {
        "tag": "probability",
        "patterns": [
            "What is the probability?", 
            "Probability of my process reaching the end state?", 
            "End state probability?"
            ],
        "responses": [
          
        ]
      },
    {
        "tag": "transitions",
        "patterns": [
            "What is the transitions?", 
            "How many transitions?", 
            "Total number of transitions?",
            "How many transitions are in my process?"
            ],
        "responses": [
          
        ]
      },
       {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye"],
        "responses": [
          "See you soon, thanks for using my service",
          "Have a nice day",
          "Bye! Feel free to use my service again."
        ]
      },
       {
        "tag": "harry",
        "patterns": [
            "What is the harry?", 
            "How many harry?", 
            "Total number of harry?",
            "How many harry are in my process?"
            ],
        "responses": [
          
        ]
      }
    ]
  }
"""


bell = ast.literal_eval(dell)
#val1 = json.loads(json.dumps(val))

#print(bell)
#print(val1)
#print(value)

#print(wer)


for intent in bell['intents']:
    tag = intent['tag']
    rezpon = intent['responses']

    #if tag == "greeting":
        #print("greeting responses: ",intent['responses'])

    if tag == "states":
        rezpon.append("The number of states is: " + str(sum_state))
        print("states responses: ",intent['responses'])

    if tag == "probability":
        rezpon.append("The probability of reaching final state is: " + str(sum_prob) + "%")
        print("probability responses: ",intent['responses'])

    if tag == "transitions":
        rezpon.append("The total number of transitions is: " + str(sum_transit))
        print("transitions responses: ",intent['responses'])

            
    if tag == "harry":
        rezpon.append("The total number of harry is: " + str(sums_transit))
        print("harry responses: ",intent['responses'])

    # rezpon = intent['responses']
    # rezpon.append(sum_state)
    # rezpon.append(sum_prob)
    # rezpon.append(sum_transit)
  


print(bell)