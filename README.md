# Distributed ICMP ping

Distributed ICMP ping program with Redis and RQ

## Description

Distributed ICMP ping program with Redis and RQ. Scale your pings.


## Dependencies

pip install redis

pip install rq

other standard modules (see import clause)


## Installation

Everything is in the repo , so just drop the files to where you want to use it.

## Usage

Setup Redis on localhost (https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04). Run workers with "rq worker" command in project directory. Execute ping-rq.py to start pinging from your distributed system.

```
root@marcin-lap:~/ping-rq# ./ping-rq.py -i ips.txt -o out.txt -s yes
root@marcin-lap:~/ping-rq# more out.txt
www.google.com,is up!
8.8.8.8,is up!
4.4.4.4,is down!
www.yahoo.com,is up!
```

Redis worker output

2 workers

1 worker

```
root@marcin-lap:~/ping-rq# rq worker

12:06:33 *** Listening on default...
13:50:44 default: ping_module.isUp('www.google.com') (0535431e-aaf9-49bb-af4c-242660a6cecd)
13:50:44 default: Job OK (0535431e-aaf9-49bb-af4c-242660a6cecd)
13:50:44 Result is kept for 500 seconds
13:50:44 Cleaning registries for queue: default
13:50:44 
13:50:44 *** Listening on default...
13:50:44 default: ping_module.isUp('www.yahoo.com') (e6ed7cd7-d58b-4668-bd7b-f12844a809f1)
13:50:44 default: Job OK (e6ed7cd7-d58b-4668-bd7b-f12844a809f1)
13:50:44 Result is kept for 500 seconds
13:50:44 
13:50:44 *** Listening on default...

```

2 worker

```
root@marcin-lap:~/ping-rq# rq worker

12:06:34 *** Listening on default...
13:50:44 default: ping_module.isUp('8.8.8.8') (20e53198-ae37-4faf-ba6d-0c45f9cb2d16)
13:50:44 default: Job OK (20e53198-ae37-4faf-ba6d-0c45f9cb2d16)
13:50:44 Result is kept for 500 seconds
13:50:44 Cleaning registries for queue: default
13:50:44 
13:50:44 *** Listening on default...
13:50:44 default: ping_module.isUp('4.4.4.4') (ba72492c-1b03-4562-bb97-9f1560d75532)
13:50:45 default: Job OK (ba72492c-1b03-4562-bb97-9f1560d75532)
13:50:45 Result is kept for 500 seconds
13:50:45 
13:50:45 *** Listening on default...
```

Worker 1 and Worker 2 can be distributed among hosts. We can scale amount of workers to n amount of workers.


## Website

Repository is at: https://gitlab.com/marcinguy/ping-rq

## Author, Copyright and License

(C) 2016 Marcin Kozlowski <marcinguy@gmail.com>

pscanner is licensed under the terms of the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

