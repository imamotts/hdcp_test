

if __name__ == "__main__":

    transmitter = HdcpSource()
    receiver = HdcpSink()

    while(1):
        response = transmitter.process_command(request)
        request = response
        response = receiver.process_command(request)


