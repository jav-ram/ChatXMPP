# ChatXMPP

Is a client that implements XMPP protocol, which connects to a server with the intention of sending information, both texts and files. **This is a console chat client**.

## Functionalities 

* Register account                      :white_check_mark:
* Log in                                :white_check_mark:
* Log out                               :large_orange_diamond:
* Delete my account                     :white_check_mark:
* List all users in my contacts         :white_check_mark:
* Get information of specific user      :large_orange_diamond:
* Comunication 1 to 1                   :white_check_mark:
* Room comunication                     :x:
* Change presence status                :large_orange_diamond:
* Notifications                         :x:
* Send/Recive files                     :large_orange_diamond:


## Instalation

This project is on Python 3 and with python with venv (venv isn't obligatory). 

[Install python 3](https://realpython.com/installing-python/)

[Install venv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

1. Clone the repositorie
    ```console
    $ git clone https://github.com/ram16230/ChatXMPP
    ```
2. Install requirements
    ```console
    $ cd ChatXMPP
    # Optional
    $ python3 -m venv ./venv
    $ pip install -r requirements.txt
    ```
3. Run project
    ```console
    $ python ./main.py 
    ```

**Extras**
* If you want to add something else to the run try this:
    ```console
    $ python ./main.py -h
    ```