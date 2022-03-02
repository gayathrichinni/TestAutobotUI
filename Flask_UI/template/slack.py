import requests
import sys
import getopt

#send message using slack API

def send_slack_message(message):
    payload = '{"text" : "%s"}' % message
    response = requests.post("https://hooks.slack.com/services/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",
                             data=payload)
    print(response.text)
def main(argv):
    message = ' '
    try: opts, args = getopt.getopt(argv, "hm:", ["message="])
    except getopt.GetoptError:
        print('slack.py -m <message>')
        sys.exit(2)
    if len(opts) == 0:
        message = "@TestAutot"
    for opt, arg in opts:
        if opt == '-h':
            print('slack.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
    send_slack_message(message)

if __name__ == "__main__":
    main(sys.argv[1:])
