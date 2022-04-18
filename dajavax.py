state1 = 1
state2 = 1
state3 = 1
state4 = 1

prob1 = 2
prob2 = 2
prob3 = 2
prob4 = 2

transit1 = 3
transit2 = 3
transit3 = 3
transit4 = 3


from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                   # connect to the JVM
random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
#number1 = random.nextInt(10)              # call the Random.nextInt method
#number2 = random.nextInt(10)
#print(number1, number2)


addition_app = gateway.entry_point               # get the AdditionApplication instance
sum_state = addition_app.addition(state1, state2, state3, state4) # call the addition method
sum_prob = addition_app.addition(prob1, prob2, prob3, prob4) # call the addition method
sum_transit = addition_app.addition(transit1, transit2, transit3, transit4) # call the addition method

print(sum_state)
print(sum_prob)
print(sum_transit)

zjt="d"
sums_transit = addition_app.prismz(zjt) #
print(sums_transit)
