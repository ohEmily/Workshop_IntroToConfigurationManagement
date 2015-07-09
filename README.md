# Configuration Management
_Slides available [here](https://docs.google.com/presentation/d/1raywAYD8A-TnVt1QdtiqO76xLtkqCwxU4-rr8oWJB1E/edit?usp=sharing). This repo covers the same concepts, but goes more in depth._
## 1. Intro
### 1.a What is configuration management?
**Configuration management** (CM) systems allow you to speed up (_automation_), regulate (_version control_), and repeat (_idempotency*_) processes that go into  machine setup and configuration.

_* = idempotency is a property that asserts that you can run the same set of commands more than once without breaking things._

**tl;dr:** CM takes you from a world of haphazard development and test environments to a world of quick and easy environment setup. 

## Demo

### Setting up SSH Keys
If you find yourself reusing a single SSH key for different servers, you might get a scary error message like this:
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
```

If you read a little further, it'll have a line along the lines of...
```
Offending RSA key in /Users/emily/.ssh/known_hosts:8
```
If you delete the offending line in your `known_hosts` file (in this case, delete line 8 in `Users/emily/.ssh/known_hosts`), the error will go away.

Alternatively, you can run `ssh-keygen -R <ip_address>`.

### DigitalOcean is Taking Long
In general, DO has excellent up time. But for your own sanity, feel free to check `check status.digitalocean.com`.
