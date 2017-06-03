# start the service
osc = Runtime.start("osc","Osc")

# connect - which is not 'really' connecting - but
# specifying the host/port of where we'll be sending 
# the messages to
osc.connect("localhost", 12000);

# now start sending messages 
# the format is
# sendMsg(topic, arg1, arg2, arg3, ...)
osc.sendMsg("/test", "this is a string", 3, 7.5, "another string");
osc.sendMsg("/newTopic", 18, "hello", 4.5);
osc.sendMsg("/somewhere/else", "this", "is", 7, 3.3, "variable arguments");

# to listen we choose a port
osc.listen(6000)

# we want them sent to python so we subscribe to
# the publishOSCMessage method
python.subscribe("osc", "publishOSCMessage")

# the messages will come back to us in onOscMessage
def onOscMessage(message):
  print(message)
  data = messages.getArguments()
  for d in data:
    print("data - ", d)
    

