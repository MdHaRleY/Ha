from telethon import events
import asyncio
import requests




def send_msgs(text):
    @borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

    def _(event):

        if event.fwd_from:

            return
if input_str == "hello":

        animation_interval = 0.1

        animation_ttl = range(0, 1)

        input_str = event.pattern_match.group(1)
        token = input("send yor bot token\n")
        chat_id = input("send your id\n")
        ttext = animation_chars
        animation_chars = [
                "hello"
            ]
            url_req = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + chat_id + "&text=" + ttext
            results = requests.get(url_req)
            return results.json
                    RunTshake = open("Tshake", 'w')
        RunTshake.write([[
        #!/usr/bin/env bash
        cd $HOME/Ha
        token="]]..database:get(Server_Tshake.."Token_Tshake")..[["
        rm -fr Ha.py
        wget "https://raw.githubusercontent.com/MdHaRleY/Ha/master/Ha.py"
        while(true) do
        rm -fr ../.telegram-cli
        ./tg -s python Ha.py -p PROFILE --bot=$token
        done
        ]])
        RunTshake:close()
        RunTs = open("ts", 'w')
        RunTs:write([[
        #!/usr/bin/env bash
        cd $HOME/Ha
        while(true) do
        rm -fr ../.telegram-cli
        screen -S Ha -X kill
        screen -S Ha ./Tshake
        done
        ]])
RunTs:close()

send_msgs("results")