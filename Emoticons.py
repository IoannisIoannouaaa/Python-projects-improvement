emoticon = 'v.v'
emoji = 'Λ.Λ'

def main():
    global emoticon
    say ('Hey is anyone in there?')
    emoticon = ':D'
    say('Oh it is you!')
    
def say(phrase):
    print(phrase + " " + emoticon)



main()