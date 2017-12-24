# Wofie Forum

This is a simple forum system to something like Reddit.
Clients are able to browse posts, groups and subscribe to whichever sub-forum they are interested.
Subscribed members are able to contribute by creating their own threads for others to interact with them.
Server side implements a multithread process to handle multiple clients simultaneously and save all the previous posts
and user data in a file locally.

## How to Run It

1. Run Server (Python 2.7)
   - Python Server.py
2. Run Client
   - Python Client.py

##Client Usage
- login \<userid>: login with userid
- help: display all commands with a brief description
- logout: logout from the application
- ag \<N>: takes an optional argument N and lists the names of all existing discussion groups, N groups at a time, numbered 1 to N.
    If N is not specified, a default value is used.
    -  s - It takes one or more numbers between 1 and N as arguments. Example:
       - s 1 - subscribe to an unsubscribed group, say #1 in the current list (page 1)
       - s 2 3 - subscribe to two unsubscribed groups in page 2
    - u - unsubscribe. It has the same syntax as the s command, except that it is used to unsubscribe from one or more groups.
    - n - show next five groups (page 2). Initially must have 15-20 groups
    - q - exit from ag command
- sg \<N>: It takes an optional argument N and lists the names of all subscribed groups, N groups at a time, numbered 1 to N.
    If N is not specified, a default value is used.
    - u - unsubscribe. It has the same syntax as the s command, except that it is used to unsubscribe from one or more groups.
    - n - list next 5 groups if there are any. Pick a group, say comp.lang.c
    - q - exit from sg command

- rg \<group name> \<max_lines> post_id: will read the corresponding post
id : will redisplay the post with at most max_lines per post
    - r : r integer or r integer-integer, this will mark the corresponding post as read
    - n : list next N post, N is giving by the optional number when you get into the rg menu, if not default is 5.
    - p : create a new post
    - q : quit the rg menu go back to main menu

- p : make a post to this group. <br>
   Prompted for post subject line
   (subject) (content)

  \# enter post subject line. Prompted for post content <br>
  \# enter post content. It should have at least two paragraphs <br>
  \# enter a dot by itself on a line at the same time as each <br>
  \# show post list, two new posts shown on top as unread <br>
  \# interact with server by press n, to see next page. <br>
